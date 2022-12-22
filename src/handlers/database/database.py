# WE use mongodb cause it's the goat. better than Ronaldo
import os
import load_dotenv
from pymongo import MongoClient

load_dotenv()

class Database:
  def __init__(self):
    self.client = MongoClient(os.environ['MONGOSTRING'])
    self.db = self.client.replit
    self.collection = self.db.users
    self.collection.create_index('username', unique=True)
