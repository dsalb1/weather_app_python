import requests

from flask import current_app


class WeatherAPIError(Exception):
    pass


class WeatherAPI:
    def __init__(self, query):
        self.base_url = current_app.config["WEATHER_BASE_URL"]
        self.key = current_app.config["WEATHER_API"]
        self.query = query

    def _make_request(self, path, **kwargs):
        params = {'key': self.key, 'q': self.query}
        params.update(kwargs)
        try:
            res = requests.get(self.base_url + path, params=params)
            res.raise_for_status()
            return res.json()
        except (requests.HTTPError, requests.ConnectionError) as e:
            message = f'There was an error requesting the Weather API data: {str(e)}'
            print(message)
            raise WeatherAPIError(message)
        except (requests.JSONDecodeError, KeyError) as e:
            message = f'There was an error parsing the JSON response from the Weather API: {str(e)}'
            print(message)
            raise WeatherAPIError(message)

    def get_forecast(self):
        req = self._make_request('forecast.json', days=1)
        return self._build_forecast(req)

    def _build_forecast(self, weather_data):
        location = weather_data['location'] or {}
        current = weather_data['current'] or {}
        forecast = weather_data['forecast']['forecastday']
        weather_res = {
            'city': location.get('name'),
            'region': location.get('region'),
            'country': location.get('country'),
            'temp': current.get('temp_f'),
            'text': current.get('condition', {}).get('text'),
            'icon': 'https:' + current.get('condition', {}).get('icon'),
        }
        if forecast:
            weather_res.update({
                'maxtemp': forecast[0]['day']['maxtemp_f'],
                'mintemp': forecast[0]['day']['mintemp_f'],
            })
        return weather_res

