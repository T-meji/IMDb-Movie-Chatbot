# Import packages
import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone
from reader import csv_doc_loader, wiki_loader
from utils import PineconeCredentials, init_pinecone

# Check if env file exists
if os.path.exists("env.py"):
    import env

import pinecone

def ingest_docs(pinecone_env: PineconeCredentials, csv_file: str, wiki_query: str) -> None:
    """
    Ingest documents into Pinecone vector index after processing and embedding.

    Parameters:
    - pinecone_env (PineconeCredentials): Pinecone environment credentials.
    - csv_file (str): The path to the CSV file.
    - wiki_query (str): The Wikipedia query or article title.

    Returns:
    - None

    Side Effects:
    - Loads vectors into the Pinecone index.
    """
    pinecone.init(
        api_key=pinecone_env.api_key, environment=pinecone_env.environment_region
    )
    
    # Load CSV data
    raw_csv_docs = csv_doc_loader(csv_file)

    # Load and process Wikipedia data
    wiki_docs = wiki_loader(wiki_query)

    # Combine CSV and Wikipedia documents
    raw_docs = raw_csv_docs + wiki_docs

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 200, chunk_overlap = 50, separators=["\n\n", "\n", " ", ""]
    )

    documents = text_splitter.split_documents(raw_docs)

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    Pinecone.from_documents(
        documents=documents, embedding=embeddings, index_name=pinecone_env.index_name
    )

    print("Successfully loaded vectors in Pinecone.")

# Making sure wiki_query only returns information relevant to the dataset
if __name__ == "__main__":
    pinecone_env = init_pinecone()
    csv_file = "C:\\Users\\TolaniOladimeji\\IMDb-Movie-Chatbot\\IMDB_Cleaned_Data.csv"
    wiki_query = [
    "North by Northwest (film)",
    "The Godfather (film)",
    "The Dark Knight (film)",
    "The Godfather: Part II (film)",
    "The Lord of the Rings: The Return of the King (film)",
    "Schindler's List (film)",
    "C'era una volta il West (film)",
    "Inception (film)",
    "Fight Club (film)",
    "Forrest Gump (film)",
    "The Lord of the Rings: The Fellowship of the Ring (film)",
    "Sunset Blvd. (film)",
    "The Matrix (film)",
    "The Lord of the Rings: The Two Towers (film)",
    "Star Wars: Episode V - The Empire Strikes Back (film)",
    "Goodfellas (film)",
    "One Flew Over the Cuckoo's Nest (film)",
    "Interstellar (film)",
    "Se7en (film)",
    "The Silence of the Lambs (film)",
    "Star Wars (film)",
    "Saving Private Ryan (film)",
    "The Green Mile (film)",
    "Cidade de Deus (film)",
    "Sen to Chihiro no kamikakushi (film)",
    "La vita bella (film)",
    "Gisaengchung (film)",
    "Shichinin no samurai (film)",
    "Modern Times (film)",
    "Gladiator (film)",
    "The Departed (film)",
    "The Prestige (film)",
    "Back to the Future (film)",
    "Hotaru no haka (film)",
    "12 Angry Men (film)",
    "Terminator 2: Judgment Day (film)",
    "The Great Dictator (film)",
    "The Lion King (film)",
    "Joker (film)",
    "Intouchables (film)",
    "The Pianist (film)",
    "Whiplash (film)",
    "Psycho (film)",
    "Citizen Kane (film)",
    "Singin' in the Rain (film)",
    "Reservoir Dogs (film)",
    "Casablanca (film)",
    "Once Upon a Time in America (film)",
    "The Dark Knight Rises (film)",
    "Django Unchained (film)",
    "Memento (film)",
    "WALL·E (film)",
    "The Shining (film)",
    "Raiders of the Lost Ark (film)",
    "Avengers: Infinity War (film)",
    "Alien (film)",
    "Avengers: Endgame (film)",
    "Apocalypse Now (film)",
    "It's a Wonderful Life (film)",
    "Requiem for a Dream (film)",
    "Rear Window (film)",
    "Coco (film)",
    "Das Leben der Anderen (film)",
    "Spider-Man: Into the Spider-Verse (film)",
    "3 Idiots (film)",
    "Mononoke-hime (film)",
    "Vertigo (film)",
    "Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (film)",
    "Das Boot (film)",
    "Inglourious Basterds (film)",
    "American Beauty (film)",
    "Braveheart (film)",
    "Star Wars: Episode VI - Return of the Jedi (film)",
    "Nuovo Cinema Paradiso (film)",
    "Eternal Sunshine of the Spotless Mind (film)",
    "Toy Story (film)",
    "Good Will Hunting (film)",
    "Snatch (film)",
    "Per qualche dollaro in piu (film)",
    "Oldeuboi (film)",
    "Toy Story 3 (film)",
    "Scarface (film)",
    "Jagten (film)",
    "Le fabuleux destin d'Amalie Poulain (film)",
    "Full Metal Jacket (film)",
    "Aliens (film)",
    "2001: A Space Odyssey (film)",
    "Leon (film)",
    "1917 (film)",
    "Amadeus (film)",
    "Jodaeiye Nader az Simin (film)",
    "The Usual Suspects (film)",
    "American History X (film)",
    "Lawrence of Arabia (film)",
    "The Sting (film)",
    "Il buono, il brutto, il cattivo (film)",
    "A Clockwork Orange (film)",
    "Taxi Driver (film)",
    "The Shawshank Redemption (film)",
]

    ingest_docs(pinecone_env, csv_file, wiki_query)
