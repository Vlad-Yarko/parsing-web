from typing import Optional
from aiohttp import ClientSession


class Request:
    def __init__(self, base_url: str):
        self.base_url = base_url
        
    async def request(self, url: str, query_params: Optional[dict] = None):
        self.url = url
        self.query_params = query_params
        async with ClientSession(base_url=self.base_url) as session:
            async with session.get(url=self.url, params=self.query_params) as response:
                return await response.text()
            
    # async def get_html(self, url: str, query_params: Optional[dict] = None) -> str:
    #     self.url = url
    #     self.query_params = query_params
    #     response = await self.request()
    #     return await response.text()
