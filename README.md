# Basic Projects

A collection of small projects I made while learning. They are simple on purpose. I keep them here as a record of my early practice.

## Projects

* `calculator/`: A calculator in a window (Tkinter). It uses `eval()` on the typed text. That is fine for practice but not safe for untrusted input.
* `games/shop.py`: A shop in the terminal. You start with a balance and buy items one at a time or add several to a cart.
* `games/snake_game.py`: The Snake game in a Tkinter window.
* `login-system/`: A toy login system in the terminal. You can log in or add a user. Users and passwords sit in plain lists in memory. This is not a real password manager and it is not secure.
* `basic-rag-pipeline/`: A short script that answers questions about a PDF. It splits the PDF into chunks, finds the closest ones to your question and sends them to Gemini. It has its own README with setup steps.
* `n8n-invoice-automation/`: An n8n workflow that reads supplier invoices from an email inbox, pulls out the details with AI, checks them and files them or sends them for review. It has its own README with setup steps.

## How to run the Python files

Install Python 3. Then run a file from the main folder, for example:

```
python calculator/calculator.py
```

Tkinter comes with Python on Windows and macOS.

The RAG script is different. It needs extra packages and an API key, so open the `basic-rag-pipeline` folder and follow its README.

## How to use the n8n workflow

Open the `n8n-invoice-automation` folder and follow its README.
