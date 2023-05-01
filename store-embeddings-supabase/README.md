# Document Embedding Storage

This script generates and stores embeddings for documents in a Supabase database. The provided script retrieves documents from a `documents` table, generates embeddings for each document using OpenAI's `text-embedding-ada-002` model, and stores the embeddings in an `embeddings` table.

## Table Structure

### Documents Table

The documents table has the following structure:

| Column   | Type                     | Description                                   |
| -------- | ------------------------ | --------------------------------------------- |
| id       | integer                  | The unique identifier for the document.       |
| title    | text                     | The title of the document.                    |
| body     | text                     | The content of the document.                  |
| category | public.document_category | The category of the document.                 |

### Embeddings Table

The embeddings table has the following structure:

| Column      | Type             | Description                                     |
| ----------- | ---------------- | ----------------------------------------------- |
| id          | integer          | The unique identifier for the embedding.        |
| embedding   | public.vector    | The vector representation of the document.      |
| document_id | integer          | Foreign key referencing the related document ID |

## Setup

1. Set up your OpenAI API key, Supabase URL, and Supabase API key in your environment variables. Add them to a `.env` file in the following format:

   ```ini
   OPENAI_KEY=your_openai_api_key_here
   SUPABASE_URL=your_supabase_url_here
   SUPABASE_ANON_KEY=your_supabase_api_key_here
   ```

2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your Supabase database has the `documents` and `embeddings` tables with the correct structure.

## Usage

To execute the script, run the following command:

```bash
python document_embedding.py
```

This will generate embeddings for all documents in the `documents` table and store them in the `embeddings` table, while handling validation errors.