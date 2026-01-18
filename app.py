from src.data_loader import load_all_documents

from src.vectorstore import FaissVectorStore
#from src.search import RAGSearch

# Main
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    #print(docs)

    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)
    #store.load()
    #print(store.query("Tripura & Bangladesh View", top_k=3))

    #rag_search = RAGSearch()
    #query = "Tripura & Bangladesh View"
    
    #summary = rag_search.search_and_summarize(query, top_k=3)
    #print("Summary:", summary)
    