import os

import requests
from flask import (
    Flask,
    render_template,
    request, flash
)

from requests import (
    HTTPError,
    ConnectionError,
    JSONDecodeError
)

from services.weather_api import WeatherAPI
from asset import Asset

app = Flask(__name__)
app.secret_key = os.urandom(24)
Asset(app)


@app.route("/")
def index():
    out = {}
    error = False
    message = ''
    query = request.args.get('q')

    if query:
        api = WeatherAPI(query)
        try:
            out = api.get_forecast()
        except (HTTPError, ConnectionError) as e:
            error = True
            message = 'There was an error requesting the Weather API data:'
            print(message + ' ' + str(e))
        except (JSONDecodeError, KeyError) as e:
            error = True
            message = 'There was an error parsing the JSON response from the Weather API:'
            print(message + ' ' + str(e))

        if error:
            flash(message, 'warning')

    return render_template("main.html", weather=out)


if __name__ == '__main__':
    app.debug = True
    app.run()
