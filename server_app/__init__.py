from flask import Flask

app = Flask(__name__, template_folder='..')

import server_app.api
import server_app.frontend