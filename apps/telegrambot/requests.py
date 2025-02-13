import aiohttp
import asyncio

API_KEY = 'baw9pp5ghw4ffoewy3ovzfjnvdh4cco2eud5qcx6zcfx2218i'
BASE_URL = 'https://api.wordnik.com/v4'


class GetWord:
    @staticmethod
    async def fetch_data(url: str, params: dict) -> dict:
        """Helper function to make a GET request and return the response data."""    
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return(f"Error: {response.status}")

    @staticmethod
    async def get_word_definitions(word: str) -> dict:
        url = f"{BASE_URL}/word.json/{word}/definitions"
        
        params = {
        'limit': 5,                 
        'includeRelated': 'false',   
        'useCanonical': 'false',     
        'includeTags': 'false',      
        'api_key': API_KEY           
        }
        
        return await GetWord.fetch_data(url=url,params=params)
    
    @staticmethod
    async def get_word_audio(word: str) -> dict:
        '''Get word audio'''
        url = f"{BASE_URL}/word.json/{word}/audio"
        params = {'limit': 5, 'api_key': API_KEY}
        return await GetWord.fetch_data(url=url,params=params)
    
    @staticmethod    
    async def get_word_exampels(word: str, top_exmaple: bool)-> dict:
        '''Get word examples'''
        if top_exmaple:
            url = f"{BASE_URL}/word.json/{word}/topExample"
        else:
            url = f"{BASE_URL}/word.json/{word}/examples"
        
        params = {'limit': 5,'api_key': API_KEY}
        
        return await GetWord.fetch_data(url=url,params=params)

    