from flask import Flask


app = Flask(__name__)

from CowWebsite import routes
