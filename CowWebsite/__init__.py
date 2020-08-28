from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ad15a7e74cae2a04a436d996579c50f9'

from CowWebsite import routes
