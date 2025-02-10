import os

BASE_DIR=os.path.dirname(__file__)
MYAPP_CONFIG = {
    "static_directory" : os.path.join( BASE_DIR, "static"),
    "template_directory": os.path.join(BASE_DIR, "templates")
}