"""Config file that controls values from environment used in the service"""
import os

SERVICE_NAME='python-rest-api-template'
PORT = 8080
BASE_PATH = '/' + SERVICE_NAME
SERVER = 'http://localhost:' + str(PORT)
