from flask import render_template, url_for, redirect, request
from form import MooForm
from moo import moo
from CowWebsite import app

years_ = 0
beef_ = 0

@app.route('/',  methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def index():
    global years_
    global beef_
    form = MooForm()
    if form.validate_on_submit():
        years_ = request.form.get('years')
        beef_ = request.form.get('beef')
        return redirect(url_for('result'))

    return render_template('index.html', form=form)

@app.route('/result')
def result():
    global years_
    global beef_
    results = moo(beef_, years_)
    return render_template ('result.html', results = results)