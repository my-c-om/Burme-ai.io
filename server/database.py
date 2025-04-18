# server/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_SHARDS = {
    'shard1': 'postgresql://user:password@shard1.example.com:5432/db',
    'shard2': 'postgresql://user:password@shard2.example.com:5432/db'
}

class ShardedSession:
    def __init__(self):
        self.engines = {
            name: create_engine(url) 
            for name, url in DATABASE_SHARDS.items()
        }
        
    def get_session(self, shard_name: str):
        return sessionmaker(bind=self.engines[shard_name])()
        
    def get_all_sessions(self):
        return [self.get_session(name) for name in DATABASE_SHARDS]
