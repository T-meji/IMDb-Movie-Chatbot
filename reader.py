from langchain.document_loaders import CSVLoader, WikipediaLoader

csv_file = "C:\\Users\\TolaniOladimeji\\IMDb-Movie-Chatbot\\IMDB_Cleaned_Data.csv"

def csv_doc_loader(csv_file):
    """
    Load CSV data from a given directory/path.

    Parameters:
    - csv_file (str): The file path where the csv data is located.

    Returns:
    - list: A list of loaded CSV documents.
    """
    loader = CSVLoader(csv_file)
    docs = loader.load()
    return docs

def wiki_loader(query):
    """
    Load Wikipedia content based on a query or article title.

    Parameters:
    - query (str): The query or article title to retrieve from Wikipedia.

    Returns:
    - list: A list of loaded Wikipedia information.
    """
    wloader = WikipediaLoader(query=query)
    wdocs = wloader.load()
    return wdocs