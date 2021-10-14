'''
To view how routes map to functions please view app/swagger/openapi.yaml
'''
from flask import jsonify

def healthcheck():
    """basic service healthcheck"""
    return jsonify({"status": "ok"}), 200
