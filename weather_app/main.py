from flask import Flask

from views.weather import weather_bp
from services.asset import Asset

app = Flask(__name__)

app.register_blueprint(weather_bp, url_prefix='/weather')

app.config.from_pyfile('settings.py')

Asset(app)

if __name__ == '__main__':
    app.debug = True
    app.run()
