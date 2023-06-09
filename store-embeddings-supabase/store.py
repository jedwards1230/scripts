import json
from typing import Optional, TypedDict, List
from supabase import create_client
import os
from dotenv import load_dotenv
import openai
import asyncio

load_dotenv()

OPENAI_KEY = os.environ.get("OPENAI_KEY", "")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_API_KEY = os.environ.get("SUPABASE_ANON_KEY", "")

# Where the embeddings are stored
TABLE_EMBEDDINGS = "embeddings"
# Where the documents are stored (to be mapped to embeddings)
TABLE_DOCUMENTS = "documents"


openai.api_key = OPENAI_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_API_KEY)


class Document(TypedDict):
    id: int
    title: str
    body: str
    category: str


async def store_doc(doc: Document) -> None:
    """
    This function stores a document's embedding and ID in a Supabase table.

    :param doc: The `doc` parameter is a `Document` object that contains information about a document,
    including its `id` and `title`
    :type doc: Document
    """
    id = doc["id"]
    title = doc["title"]

    # Get the embedding for the document
    input = json.dumps(doc)
    model_id = "text-embedding-ada-002"
    embedding = openai.Embedding.create(input=input, model=model_id)["data"][0][
        "embedding"
    ]

    # Upsert (update or insert) the embedding into the embeddings table
    supabase.table(TABLE_EMBEDDINGS).upsert(
        {"embedding": embedding, "document_id": id},
        on_conflict="document_id",
    ).execute()

    print(f"Stored document {title}")


async def get_all_documents() -> Optional[List[Document]]:
    """
    This function retrieves all documents from a Supabase table and returns them as a list of Document
    objects, or None if there are no documents.
    :return: The function `get_all_documents()` returns an optional list of `Document` objects. If the
    Supabase query returns data, the function returns a list of `Document` objects. Otherwise, it
    returns `None`.
    """
    response = supabase.table(TABLE_DOCUMENTS).select("*").execute()
    if response.data:
        return response.data
    return None


async def store_docs() -> None:
    """
    This function retrieves all documents and stores them, while handling validation errors.
    :return: The function `store_docs()` returns `None`.
    """
    docs = await get_all_documents()
    if docs is None:
        return
    for doc in docs:
        try:
            await store_doc(doc)
        except ValueError as e:
            print(f"Error validating document: {e}")


asyncio.run(store_docs())
