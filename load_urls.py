from langchain_community.document_loaders import WebBaseLoader

with open("DATA/urls.text", "r") as f:
    urls = f.read().splitlines()

loader = WebBaseLoader(urls)
docs = loader.load()

print(f"Total pages loaded: {len(docs)}")
print(docs[0].page_content[:500])
