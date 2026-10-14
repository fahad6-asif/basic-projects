# Basic RAG Pipeline

A small question-answering script over a PDF. You give it a PDF, ask a question in the terminal, and it answers using only the parts of the PDF that match the question.

This was an early practice project to learn how RAG works from end to end. I wrote it myself. It is one short file on purpose.

## What it does

1. Loads your PDF with PyMuPDF.
2. Splits the text into chunks of 1200 characters, with 150 characters of overlap.
3. Turns each chunk into an embedding with a small local model (`multi-qa-MiniLM-L6-cos-v1`).
4. Stores the embeddings in a FAISS index in memory.
5. Takes your question and finds the 3 closest chunks.
6. Sends the question and those chunks to Gemini (`gemini-2.5-flash`) and prints the answer.

## How to run it

1. Install Python 3, then install the packages:

   ```
   pip install -r requirements.txt
   ```

2. Put your PDF in this folder and name it `your_document.pdf`. Or change the file name on line 15 of the script.

3. Make a file called `.env` in this folder with your Gemini API key:

   ```
   GOOGLE_API_KEY=your_key_here
   ```

   There is a `.env.example` you can copy. Do not upload your real `.env` to GitHub.

4. Run it from inside this folder:

   ```
   python basic_rag_pipeline.py
   ```

5. Type your question when it asks `Q:`.

The first run downloads the embedding model, so it takes a little longer.

## Limitations

* It answers one question and then stops. You have to run it again for the next question.
* It has no chat memory. The prompt mentions previous chats, but the part that would remember them is commented out in the code.
* It rebuilds the index from the PDF on every run. The line that would save the index to disk is commented out.
* It reads one PDF only.
* It always sends 3 chunks, even if the question needs more or fewer.
* It does not check that the answer is really in the PDF, so the model could still get something wrong.

## What I would improve

* Add a loop so I can ask many questions in one run.
* Add chat memory.
* Save the index so it is not rebuilt each time.
* Show which chunks the answer came from.

My later, bigger project has the question loop and shows its sources: [`zenith-field-service-rag`](https://github.com/fahad6-asif/zenith-field-service-rag).
