DEBUG = True
PORT = 8000
HOST = "0.0.0.0"
BASE_URL = "/tide"

SECRET_KEY = "adsfjkasn"

# MONGODB_DB = 'tide'
# MONGODB_HOST = '192.168.169.16'
# MONGODB_PORT = 27017
# MONGODB_USERNAME = 'ylin'
# MONGODB_PASSWORD = '^&*yt345'

# mongo debug
DEBUG_TB_PANELS = [
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    # 'flask_mongoengine.panels.MongoDebugPanel'
]
