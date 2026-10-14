from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

#loading .env file for API keys
load_dotenv()

#document loader
loader=PyMuPDFLoader('your_document.pdf')
document=loader.load()

#chunking
chunker=RecursiveCharacterTextSplitter(chunk_size=1200,chunk_overlap=150)
chunks=chunker.split_documents(document)

#embedding process
embedder=HuggingFaceEmbeddings(model='sentence-transformers/multi-qa-MiniLM-L6-cos-v1')
vector_database=FAISS.from_documents(chunks,embedder)
#vector_database.save_local('faiss_index')


#prompt template
#chat_history=[]

template_prompt = ChatPromptTemplate([
    ('system', 'You are a professional Document analyzer and your job is to answer the question using the given content and use the memory of the previous chats if required.'),
#    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}\n{content}')
])

#retrieval
retriever=vector_database.as_retriever(search_kwargs={'k':3})

def document_format(output_chunks):
    return "\n\n".join(i.page_content for i in output_chunks)

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

rag_chain=({'content':retriever | document_format , 'query':RunnablePassthrough()}
           | template_prompt
           | model
           | StrOutputParser())

query=input('Q: ')
results=rag_chain.invoke(query)
print(results)