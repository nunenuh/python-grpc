
from core import config

import grpc

from proto.books import books_pb2_grpc
from proto.books import books_pb2

async def get_book_by_id(book_id: int):
    async with grpc.aio.insecure_channel(config.BOOKS_GRPC_ADDRESS) as channel:
        client = books_pb2_grpc.BooksRequestStub(channel)
        request = books_pb2.BooksRequestById(id=book_id)        
        response = await client.GetBookById(request)
        return response