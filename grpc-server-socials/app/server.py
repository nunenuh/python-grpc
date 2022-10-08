
import asyncio
import logging

import grpc

from services.socials import socials_pb2_grpc
from services.social_service import SocialsService

async def serve() -> None:
    server = grpc.aio.server()
    socials_pb2_grpc.add_SocialsRequestServicer_to_server(SocialsService(), server)
    listen_addr = '0.0.0.0:5059'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())