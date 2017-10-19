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

# all bands in metal
@app.route('/metal')
def met():
    return render_template('metal.html'), 200

#Led Zep Albums
@app.route('/ledzep')
def led():
    return render_template('ledzep.html'), 200

@app.route('/lz4')
def lz4():
    return render_template('lz4.html'), 200

@app.route('/physical')
def phy():
    return render_template('physical.html'), 200

@app.route('/lz2')
def lz2():
    return render_template('lz2.html'), 200

@app.route('/blacksab')
def black():
    return render_template('blacksab.html'),200

@app.route('/rage')
def rage():
    return render_template('rage.html'), 200

# all bands in indie
@app.route('/indie')
def ind():
    return render_template('indie.html'), 200

@app.route('/arctic')
def arc():
    return render_template('arctic.html'), 200

@app.route('/radio')
def rad():
    return render_template('radio.html'), 200

@app.route('/oasis')
def oas():
    return render_template('oasis.html'), 200

# all bands in alt
@app.route('/alt')
def alt():
    return render_template('alt.html'), 200

@app.route('/foo')
def foo():
    return render_template('foo.html'), 200

@app.route('/nirvana')
def nir():
    return render_template('nirvana.html'), 200

@app.route('/muse')
def mus():
    return render_template('muse.html'), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
