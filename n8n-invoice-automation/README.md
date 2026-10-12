# Invoice Automation (n8n)

An n8n workflow that reads supplier invoices from an email inbox, pulls out the details with AI, checks them, and either files them or sends them to a person for review.

This was a self-directed learning project built as a case study. Some parts are mocked on purpose (see "What I mocked, and why").

## What the workflow is really for

The distributor gets a huge number of supplier invoices every month. Right now each one has to be typed into the system by hand. That takes far too long.

The idea is that a person only has to hand the invoice to the system and the system does the rest. It reads the invoice and checks it. Then it either files it or sends it to a human when something looks off.

## The shape of the workflow

1. The workflow starts when an email with the subject "Invoice" lands in the inbox.
2. It downloads the attached file.
3. The file goes through OCR. The OCR scans the invoice, labels the fields and returns clean JSON.
4. The invoice number is checked against the database to see if it is a duplicate.
5. If it is a duplicate, it is logged, labelled as a duplicate and sent for review.
6. If it is new, it goes to a code node. That node checks the GST, the PO variance, the GST tolerance, the maths, the mock database and the confidence rating.
7. Every invoice is then logged with a status (approved or not). If it is not approved, the reason is logged too.

The database has two tables. One is for single-line-item invoices and one is for multi-line-item invoices. This keeps the line items tidy. Invoices marked for review are logged in a separate review table, and that table is sent to a human.

## Why I arranged it that way

The checks run in a sensible order. The duplicate check comes first. If an invoice has already been processed there is no point checking it again. Only a new invoice moves on to validation.

All the validation sits in one code node, so the logic stays in one place and is not spread across many nodes.

Every invoice is logged at the end. The log is also what the duplicate check reads from.

## How I did the extraction

An AI image analyzer reads the invoice image and pulls out its contents. I used a very specific prompt so the AI returns the data in the exact format I wanted. That output then goes through an information extractor node to become clean JSON.

I also told it to leave a field as null if something is unreadable. That way the model never makes up numbers.

## How the validation works

The JSON goes into a Python code node. It uses simple if-statements to check:

* the line-item maths
* the GST rate
* the GST tolerance
* the PO variance against the mock database
* the extraction confidence

If a check fails, the reason is added to a list. An invoice can come back with more than one reason.

The main settings are at the top of the code node so they are easy to change. These are the GST rate, the PO variance, the GST tolerance and the confidence threshold.

## What I mocked, and why

I mocked the parts that are not the main point so I could focus on the real logic.

* **Email inbox:** an email trigger that fires when an invoice is sent to one address with the subject "Invoice".
* **Accounting system:** Google Sheets, where the filed invoices are written.
* **Mock database:** a small hard-coded list to check against.
* **Notification:** an email node that sends the invoices that need review.

Each one does the same basic job as the real thing. That is enough for a case study.

## What went wrong

At first I tried to build the validation without a code node. I used separate n8n nodes instead. It quickly became much bigger and more complicated than it needed to be. I replaced all of those nodes with a single code node that does the whole validation step.

## What I would improve

* Add basic error handling, so a bad or unreadable file goes to review instead of stopping the whole run.
* Add a cost and time-saved estimate to show the value.

## Limitations

The whole workflow depends on the quality of the extraction. The confidence score comes from the AI itself. If the AI reads something wrong but is confident about it, an invalid invoice could get logged.

The main field used to identify an invoice is the invoice number. If that number is wrong, the system might wrongly approve the invoice.

## How to import it

1. In n8n, go to Workflows, then Import from file, and choose `workflow.json`.
2. Set up your own credentials. The file only contains references to credentials, not the keys themselves. You will need:
   * IMAP (the inbox that receives the invoices)
   * Google Drive OAuth2
   * Google Sheets OAuth2
   * Groq API
   * SMTP (for the review email)
   * A model for the "Analyze image" step. That node used an n8n-managed AI credential, which does not carry over. Pick your own vision model there.
3. Create a Google Sheet with four tabs named Parent Database, Child Database, Review Database and Mock Database. Then select your sheet in each Google Sheets node. The sheet ID in the file has been replaced with `YOUR_SHEET_ID`.
4. Change the email addresses in the "Send an Email" node. They are set to `you@example.com`.
