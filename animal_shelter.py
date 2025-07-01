from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user='aacuser', password='pass', host='nv-desktop-services.apporto.com', port=33345, db='AAC', col='animals'):
        """Initialize MongoDB connection."""
        try:
            self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}/?authSource=admin')
            self.database = self.client[db]
            self.collection = self.database[col]
        except Exception as e:
            raise Exception(f"Could not connect to MongoDB: {e}")

    def create(self, data):
        """Insert a document into the collection."""
        if data:
            try:
                result = self.collection.insert_one(data)
                return True if result.inserted_id else False
            except Exception as e:
                print(f"Insert error: {e}")
                return False
        else:
            raise Exception("No data provided to insert.")

    def read(self, query):
        """Read documents matching the query."""
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print(f"Read error: {e}")
            return []
    def update(self, query, update_values):
        """Update document(s) matching query with new values"""
        try:
            result = self.collection.update_many(query, {'$set': update_values})
            return result.modified_count
        except Exception as e:
            print(f"Update error: {e}")
            return 0

    def delete(self, query):
        """Delete document(s) matching query"""
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Delete error: {e}")
            return 0

