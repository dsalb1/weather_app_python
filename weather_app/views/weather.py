from flask import (
    render_template,
    request,
    flash,
    Blueprint, jsonify
)

from weather_app.services.weather_api import WeatherAPI, WeatherAPIError

weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/python")
def weather_python():
    out = {}
    query = request.args.get('q')

    if query:
        api = WeatherAPI(query)
        try:
            out = api.get_forecast()
        except WeatherAPIError as e:
            flash(str(e), 'warning')

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
        try:
            out = api.get_forecast()
        except WeatherAPIError as e:
            out = {'error': str(e)}
            # just call any error a generic 400 for now, this was already logged anyway
            return jsonify(out), 400

    return jsonify(out)
