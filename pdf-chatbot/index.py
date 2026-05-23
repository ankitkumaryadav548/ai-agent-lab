from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

# Load PDF
loader = PyPDFLoader("data/sample.pdf")
documents = loader.load()

# Split PDF into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

texts = text_splitter.split_documents(documents)

# Create embeddings
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# Create vector database
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings
)

# Create retriever
retriever = vectorstore.as_retriever()

# Load local LLM
llm = ChatOllama(
    model="phi3:mini"
)

print("\n📘 PDF Chatbot Ready!")
print("Type 'exit' to quit\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    # Search relevant chunks
    docs = retriever.invoke(query)

    # Combine retrieved text
    context = "\n\n".join([doc.page_content for doc in docs])

    # Create prompt
    prompt = f'''
Answer the question using the PDF context below.

Context:
{context}

Question:
{query}
'''

    # Generate response
    response = llm.invoke(prompt)

    print(f"\n🤖 AI: {response.content}\n")