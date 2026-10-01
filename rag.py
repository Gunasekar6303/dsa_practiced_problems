# 1. Document
document = "hr_policy.pdf"


# 2. Load document
loader = PDFLoader(document)
documents = loader.load()


# 3. Split document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)


# 4. Create embeddings
embedding_model = EmbeddingModel(
    model="embedding-model"
)

embeddings = embedding_model.embed_documents(chunks)


# 5. Store embeddings
vector_database = VectorDatabase()

vector_database.add(
    documents=chunks,
    embeddings=embeddings
)


# 6. Create retriever
retriever = vector_database.as_retriever(
    search_type="similarity",
    top_k=5
)


# 7. User query
query = "What is the leave policy?"


# 8. Retrieve relevant chunks
retrieved_documents = retriever.retrieve(query)


# 9. Create context
context = ""

for document in retrieved_documents:
    context += document.text + "\n"


# 10. Create prompt
prompt = f"""
Answer the question using only the provided context.

Context:
{context}

Question:
{query}
"""


# 11. Send context + question to LLM
llm = LLM(
    model="llm-model"
)

answer = llm.generate(prompt)


# 12. Final answer
print(answer)