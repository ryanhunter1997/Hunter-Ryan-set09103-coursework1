from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('home.html'), 200

@app.route('/sub-genre')
def subgenre():
    return render_template('sub-genre.html'), 200

@app.route('/artists')
def art():
    return render_template('artists.html'), 200

@app.route('/metal')
def met():
    return render_template('metal.html'), 200

@app.route('/ledzep')
def led():
    return render_template('ledzep.html'), 200

@app.route('/blacksab')
def black():
    return render_template('blacksab.html'),200

@app.route('/rage')
def rage():
    return render_template('rage.html'), 200

@app.route('/indie')
def ind():
    return render_template('indie.html'), 200

@app.route('/alt')
def alt():
    return render_template('alt.html'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
