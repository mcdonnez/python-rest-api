# This is where we can change settings
# https://docs.gunicorn.org/en/latest/settings.html#
import config.constants as constants
bind = "0.0.0.0:" + str(constants.PORT)
timeout = 60
workers = 3

logconfig = "config/logging.conf"
access_log_format = '''{"referer":"%(f)s","method":"%(m)s","ip":"%(h)s","query":"%(q)s","servertime":"%(t)s","url":"%(U)s","transactionId":"%({transactionId}i)s","status-code":"%(s)s","parentRequestId":"%({parentRequestId}i)s","user-agent":"%(a)s","executeTime":"%(M)s"}'''
