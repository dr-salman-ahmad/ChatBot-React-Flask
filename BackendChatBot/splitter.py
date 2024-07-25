from langchain.text_splitter import RecursiveCharacterTextSplitter
from loader import Loader


class DocumentProcessor:
    def __init__(self, chunk_size: int, chunk_overlap: int, separators: list):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators
        )
        self.loader = Loader()

    def load_documents(self):
        documents = self.loader.load()
        return documents

    def split_documents(self, documents):
        return self.text_splitter.split_documents(documents)

    def process_documents(self):
        documents = self.load_documents()
        return self.split_documents(documents)
