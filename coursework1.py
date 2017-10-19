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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
