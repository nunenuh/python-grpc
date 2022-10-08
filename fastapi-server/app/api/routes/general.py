from typing import Any

import joblib
from core.errors import PredictException
from fastapi import APIRouter, HTTPException, Request, status
from loguru import logger

from services import socials, books
import schema

router = APIRouter()



@router.get("/book/{book_id}", name="social:get-book")
async def get_social_by_id(request: Request, book_id: int):
    if not book_id:
        raise HTTPException(status_code=404, detail=f"'id' argument invalid!")
    
    book_resp = await books.get_book_by_id(book_id)
    book_data = schema.Books(id=book_resp.id, title=book_resp.title, 
                             author=book_resp.author, description=book_resp.description,
                             publisher=book_resp.publisher)
    
    return {
        'status': status.HTTP_200_OK,
        'message': 'success',
        'data':  book_data
    }

@router.get("/social/{social_id}", name="social:get-book")
async def get_social_by_id(request: Request, social_id: int):
    if not social_id:
        raise HTTPException(status_code=404, detail=f"'id' argument invalid!")
    social = await socials.get_social_by_id(social_id)
    social_dict = schema.Socials(id=social.id, name=social.name, twitter=social.twitter)
    
    
    return {
        'status': status.HTTP_200_OK,
        'message': 'success',
        'data': social_dict
    }
    
    
