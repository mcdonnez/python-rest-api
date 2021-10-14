'''
Main server file to run the application
'''
from prometheus_flask_exporter import ConnexionPrometheusMetrics
import connexion
from config.constants import BASE_PATH, PORT, SERVER
from app.utils import json_encoder

METRICS_PATH = BASE_PATH + '/metrics'
app = connexion.App(__name__, specification_dir="../config", port=PORT)
metrics = ConnexionPrometheusMetrics(app, path=METRICS_PATH)
app.add_api('openapi.yaml', base_path=BASE_PATH, arguments={'host':SERVER})

app.app.json_encoder = json_encoder.CamelCaseEncoder

if __name__ == "__main__":
    app.run()
