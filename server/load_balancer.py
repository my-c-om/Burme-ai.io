# server/load_balancer.py
from fastapi import Request
from databases import Database

async def get_shard(request: Request) -> Database:
    """Client IP-based shard selection"""
    client_ip = request.client.host
    shard_name = 'shard1' if hash(client_ip) % 2 == 0 else 'shard2'
    return sharded_session.get_session(shard_name)
