import asyncio
import logging

import grpc
from services.socials.socials_pb2_grpc import SocialsRequestServicer
from services.socials.socials_pb2 import Socials, SocialsRequestById



data_mock = [
    Socials(id=1, name="Fandi", twitter="@nunenuh"),
    Socials(id=2, name="Darmawan", twitter="@awan"),
    Socials(id=3, name="Toni", twitter="@toni"),
]


class SocialsService(SocialsRequestServicer):
    async def GetSocialById(self, request: SocialsRequestById, context: grpc.aio.ServicerContext) -> Socials:
        idx = request.id
        data: Socials = data_mock[idx-1]
        return data
        