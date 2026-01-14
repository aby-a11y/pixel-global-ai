from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os
import csv



print("🔹 Starting ingest.py")

load_dotenv()
print("🔹 ENV loaded")

FILE_PATH = "DATA/knowledge.txt"
CSV_PATH = "DATA/SERVICES.csv"

csv_text = ""

with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        csv_text += " | ".join(row) + "\n"

print("🔹 Checking file path:", FILE_PATH)

services_summary = """
SERVICES OFFERED:
- SEO (Micro, Small, Medium, Enterprise)
- Social Media Marketing (SMM)
- Website Development
- Ecommerce Development
- AI Chatbot Automation
"""

if not os.path.exists(FILE_PATH):
    print("❌ FILE NOT FOUND")
    exit()

with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()

print("🔹 Characters loaded:", len(text))

if len(text.strip()) == 0:
    print("❌ FILE EMPTY")
    exit()
combined_text = text + "\n\nSERVICE PRICING DATA:\n" + csv_text
doc = Document(page_content=combined_text)


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=150
)

chunks = splitter.split_documents([doc])
print("🔹 Chunks created:", len(chunks))

embedding = OpenAIEmbeddings()

print("🔹 Creating vector DB...")
db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="db"
)

db.persist()

print("✅ INGEST COMPLETE — VECTOR DB READY")
