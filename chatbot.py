from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

# Load ENV (OpenAI key)
load_dotenv()

print("🔥 Chatbot starting...")

# Embeddings
embedding = OpenAIEmbeddings()

# Load existing Vector DB
db = Chroma(
    persist_directory="db",
    embedding_function=embedding
)

retriever = db.as_retriever()

# LLM
llm = ChatOpenAI(temperature=0)

print("✅ PixelGlobal Ai ready")

# Chat loop
while True:
    query = input("\nAsk PixelGlobal Ai: ")

    if query.lower() in ["exit", "quit"]:
        print("👋 Bye")
        break

    docs = retriever.invoke(query)


    if not docs:
        print("❌ Not available in PixelGlobal data")
        continue

    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are PixelGlobal AI assistant.

You can summarize, rephrase, and combine information from the context.
If pricing is asked, list prices clearly.
If services are asked, list available services even if prices are not asked.
If the answer is truly not present, then say:
Not available in PixelGlobal data.
You can summarize, rephrase, and combine information from the context.

IMPORTANT RULES:
- If case studies are asked, respond in a clean structured format.
- Each case study must be separated clearly.
- If a case study link is present in the context, always show it at the end.
- Do not mix multiple case studies into one.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)
    print("\n🤖", response.content)
    
    


