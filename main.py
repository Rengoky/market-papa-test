from typing import Dict, Any, Optional
import aiohttp
import os

from exceptions import NoApiKeysAvailable


class WeatherApiClient:
    """A class for interacting with the M3O Weather API."""

    def __init__(self):
        self.api_key = os.getenv('WEATHER_KEY')
        self.base_url = 'https://api.m3o.com/v1/weather'
        self.location = 'Moscow'

    async def get_current_weather(self, location: str) -> Optional[Dict[str, Any]]:
        """Get current weather forecast."""
        if not self.api_key:
            raise NoApiKeysAvailable
        url = f'{self.base_url}/current'
        params = {'location': location}
        headers = {'Authorization': f'Bearer {self.api_key}'}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('weather')
        return None

    async def get_weather_forecast(self, location: str, days: int) -> Optional[Dict[str, Any]]:
        """Get weather forecast for the next `days` days."""
        if not self.api_key:
            raise NoApiKeysAvailable
        url = f'{self.base_url}/forecast'
        params = {'location': location, 'days': days}
        headers = {'Authorization': f'Bearer {self.api_key}'}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('forecast')
        return None
