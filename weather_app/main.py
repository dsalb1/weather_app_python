import json
from flask import  Flask

from weather_app.views.weather import weather_bp
from weather_app.services.asset import Asset

app = Flask(__name__)
app.register_blueprint(weather_bp, url_prefix='/weather')

app.config.from_file("../config.json", load=json.load)

Asset(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
