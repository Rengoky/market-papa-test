# market-papa-test
Тестовое задание для компании market-papa

Тестовое - это приложение для получения погоды в указанном городе.

Он использует API https://m3o.com/weather/api погоды для получения информации о погоде.

## Установка

Для установки проекта Тестовое необходимо:

Склонировать репозиторий на локальную машину:
```
git clone https://github.com/Rengoky/market-papa-test.git
```
Создать виртуальное окружение:
```
python -m venv venv
```
Установить зависимости:
```
pip install -r requirements.txt
```
## Использование

Тестовое предоставляет два метода для получения информации о погоде:

```
get_current_weather(location: str) -> Optional[Dict[str, Any]]:

получает текущую погоду в указанном городе.
```
```
get_weather_forecast(location: str, days: int) -> Optional[Dict[str, Any]]: 

получает прогноз погоды на указанное количество дней для указанного города.
```
## Атрибуты:
- api_key: строка, содержащая API ключ для доступа к API погоды M3O, извлекается из переменных окружения. Для получения
необходимо зарегестрироваться 

- base_url: строка, содержащая базовый URL для API погоды M3O.
- location: строка, содержащая местоположение по умолчанию для запросов к API.

## Пример использования:
```
from weather_api import WeatherApiClient

Создаем экземпляр клиента API погоды

client = WeatherApiClient()

Получаем текущую погоду в Москве
current_weather = await client.get_current_weather('Moscow')

Получаем прогноз погоды на 5 дней в Москве
weather_forecast = await client.get_weather_forecast('Moscow', 5)
```