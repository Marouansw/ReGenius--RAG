from pipelines.rag_pipeline import rag_pipeline

# Ask the user to enter the query
query = input('Please enter the query to run through the RAG pipeline : ')

# Run the pipeline with the provided query
rag_pipeline(query)
