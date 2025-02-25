from flask import Flask
from services.geo_service import geo_service_app
from services.places_service import places_service_app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(geo_service_app, url_prefix='/api')
app.register_blueprint(places_service_app, url_prefix='/api')

if __name__ == "__main__":
    app.run(debug=True)
