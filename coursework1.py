from flask import Flask, render_template, url_for
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

#black sabbath albums
@app.route('/blacksab')
def black():
    return render_template('blacksab.html'), 200

@app.route('/paranoid')
def para():
    return render_template('paranoid.html'), 200

@app.route('/selftitled')
def self():
    return render_template('selftitled.html'), 200

@app.route('/vol4')
def vol():
    return render_template('vol4.html'), 200

#rage albums
@app.route('/rage')
def rage():
    return render_template('rage.html'), 200

@app.route('/ragest')
def st():
    return render_template('ragest.html'), 200

@app.route('/evilempire')
def ee():
    return render_template('evilempire.html'), 200

@app.route('/battleofla')
def la():
    return render_template('battleofla.html'), 200

# all bands in indie
@app.route('/indie')
def ind():
    return render_template('indie.html'), 200

#all arctic monkeys
@app.route('/arctic')
def arc():
    return render_template('arctic.html'), 200

@app.route('/fwn')
def fwn():
    return render_template('fwn.html'), 200

@app.route('/humbug')
def hum():
    return render_template('humbug.html'), 200

@app.route('/am')
def am():
    return render_template('am.html'), 200

#all radiohead
@app.route('/radio')
def rad():
    return render_template('radio.html'), 200

@app.route('/okcomputer')
def ok():
    return render_template('okcomputer.html'), 200

@app.route('/inrainbows')
def inr():
    return render_template('inrainbows.html'), 200

@app.route('/thebends')
def theb():
    return render_template('thebends.html'), 200

#all oasis
@app.route('/oasis')
def oas():
    return render_template('oasis.html'), 200

@app.route('/definitelymaybe')
def dm():
    return render_template('definitelymaybe.html'), 200

@app.route('/whatsthestory')
def wts():
    return render_template('whatsthestory.html'), 200

@app.route('/themasterplan')
def tmp():
    return render_template('themasterplan.html'), 200

# all bands in alt
@app.route('/alt')
def alt():
    return render_template('alt.html'), 200

#all foo fighters
@app.route('/foo')
def foo():
    return render_template('foo.html'), 200

@app.route('/foofighters')
def ff():
    return render_template('foofighters.html'), 200

@app.route('/colourandtheshape')
def cs():
    return render_template('colourandtheshape.html'), 200

@app.route('/inyourhonor')
def iyh():
    return render_template('inyourhonor.html'), 200

#all nirvana albums
@app.route('/nirvana')
def nir():
    return render_template('nirvana.html'), 200

@app.route('/nevermind')
def nev():
    return render_template('nevermind.html'), 200

@app.route('/inutero')
def inu():
    return render_template('inutero.html'), 200

@app.route('/bleach')
def ble():
    return render_template('bleach.html'), 200

#all muse albums
@app.route('/muse')
def mus():
    return render_template('muse.html'), 200

@app.route('/absolution')
def abs():
    return render_template('absolution.html'), 200

@app.route('/origin')
def org():
    return render_template('origin.html'), 200

@app.route('/blackholes')
def bla():
    return render_template('blackholes.html'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)
