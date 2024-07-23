from pathlib import Path
import shutil
from langchain_chroma import Chroma
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from splitter import DocumentProcessor


class DocumentEmbedding:
    def __init__(self, persist_directory: Path, chunk_size: int = 100, chunk_overlap: int = 5):
        self.persist_directory = persist_directory
        self.embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        self.processor = DocumentProcessor(chunk_size=chunk_size, chunk_overlap=chunk_overlap,
                                           separators=["(?<=\. )", " "])
        self.vectordb = self.initialize_vectordb()

    def initialize_vectordb(self):
        """Initializes the Chroma vector database with processed documents, only if it doesn't already exist."""
        if self.persist_directory.exists():
            # Load existing vector database
            return Chroma(persist_directory=str(self.persist_directory))

        # Initialize and save new vector database
        splits = self.processor.process_documents()
        return Chroma.from_documents(
            documents=splits,
            embedding=self.embedding,
            persist_directory=str(self.persist_directory)
        )

    def delete_directory(self):
        """Deletes the persist directory."""
        if self.persist_directory.exists():
            try:
                shutil.rmtree(self.persist_directory)
                return {"message": "Directory deleted successfully"}, 200
            except Exception as e:
                return {"error": str(e)}, 500
        else:
            return {"error": "Directory does not exist"}, 404

    def get_document_count(self):
        """Returns the count of documents in the vector database."""
        return self.vectordb._collection.count()

    def get_vectordb(self):
        return self.vectordb
