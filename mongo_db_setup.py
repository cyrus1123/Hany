from pymongo import MongoClient
from dotenv import load_dotenv
import os

def initialize_mongo_db():
    # Load environment variables from the .env file
    load_dotenv()

    # Get the MongoDB URI from the environment variables
    mongo_uri = os.getenv('MONGO_URI')

    if not mongo_uri:
        raise Exception("MongoDB URI not found in environment variables")

    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db_name = mongo_uri.split('/')[-1]

    # Create the database and collection if they don't exist
    db = client[db_name]

    # Create or verify the collection (e.g., 'image_files')
    collection_name = 'image_files'
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
        print(f"Collection '{collection_name}' created in database '{db_name}'")
    else:
        print(f"Collection '{collection_name}' already exists in database '{db_name}'")

    print(f"MongoDB setup complete for database: {db_name}")

if __name__ == "__main__":
    try:
        initialize_mongo_db()
    except Exception as e:
        print(f"Error during MongoDB setup: {e}")
