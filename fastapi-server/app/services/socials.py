
from core import config

import grpc

from proto.socials import socials_pb2_grpc
from proto.socials import socials_pb2

async def get_social_by_id(social_id: int):
    async with grpc.aio.insecure_channel(config.SOCIALS_GRPC_ADDRESS) as channel:
        client = socials_pb2_grpc.SocialsRequestStub(channel)
        request = socials_pb2.SocialsRequestById(id=social_id)
        response = await client.GetSocialById(request)
        return response