from flask import (
    render_template,
    request,
    flash,
    Blueprint, jsonify
)

from requests import (
    HTTPError,
    ConnectionError,
    JSONDecodeError
)

from weather_app.services.weather_api import WeatherAPI

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/python")
def weather_python():
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

    return render_template("main_python.html", weather=out)


@weather_bp.route("/js")
def weather_js():
    return render_template("main_js.html")


@weather_bp.route("/js/api", methods=['POST'])
def weather_js_api():
    out = {}
    query = request.form.get('q')
    if query:
        api = WeatherAPI(query)
        out = api.get_forecast()

    return jsonify(out)
