from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base/')
def get_base():
    return render_template('base.html')


@app.route('/processors/')
def get_processors():
    return render_template('processors.html')


@app.route('/memory/')
def get_memory():
    return render_template('memory.html')


@app.route('/motherboards/')
def get_motherboards():
    return render_template('motherboards.html')