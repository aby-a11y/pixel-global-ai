from flask import Flask, request, jsonify, render_template
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Load components (same as chatbot.py)
embedding = OpenAIEmbeddings()
db = Chroma(persist_directory="db", embedding_function=embedding)
retriever = db.as_retriever(search_kwargs={"k": 10})
llm = ChatOpenAI(temperature=0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('message')
    
    docs = retriever.invoke(query)
    if not docs:
        return jsonify({'response': 'Not available in PixelGlobal data'})
    
    context = "\n".join([d.page_content for d in docs])
    prompt = f"""
You are PixelGlobal AI assistant.

You can summarize, rephrase, and combine information from the context.
If pricing is asked, list prices clearly in bullet format.
If services are asked, list available services even if prices are not asked.
If case studies are asked, respond in a clean structured format.
Each case study must be separated clearly.
If a case study link is present in the context, always show it at the end.
Do not mix multiple case studies into one.

If the answer is truly not present in the context, then say: Not available in PixelGlobal data.

Context:
{context}

Question:
{query}
"""
    
    response = llm.invoke(prompt)
    return jsonify({'response': response.content})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
