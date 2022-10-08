import asyncio
import logging

import grpc
from services.books.books_pb2_grpc import BooksRequestServicer
from services.books.books_pb2 import Books, BooksRequestById



data_mock = [
    Books(id=1, title="Livewired", author="David Eagleman", description="", publisher=""),
    Books(id=2, title="Start with Why", author="Simon Sinek", description="", publisher=""),
    Books(id=3, title="Infinite Game", author="Simon Sinek", description="", publisher=""),
]


class BooksService(BooksRequestServicer):

    async def GetBookById(self, request: BooksRequestById, context: grpc.aio.ServicerContext) -> Books:
        idx = request.id
        book: Books = data_mock[idx-1]
        return book
        