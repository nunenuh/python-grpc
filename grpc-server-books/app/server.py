
import asyncio
import logging

import grpc

from services.books import books_pb2_grpc
from services.books.books_pb2_grpc import BooksRequestServicer
from services.books.books_pb2 import Books, BooksRequestById
from services.book_service import BooksService

async def serve() -> None:
    server = grpc.aio.server()
    books_pb2_grpc.add_BooksRequestServicer_to_server(BooksService(), server)
    listen_addr = '0.0.0.0:5058'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())