from flask import redirect, url_for, request, Flask, send_from_directory, render_template
import requests
import json

app = Flask(__name__, static_url_path='')

        
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hasil', methods=['POST'])
def post():
    name=request.form['nama']
    url='https://pokeapi.co/api/v2/pokemon/'+name
    poke=requests.get(url)
    if str(poke)=='<Response [404]>':
        return redirect('/NotFound')
    filenama=poke.json()['name']
    besar=filenama[0].upper()
    nama=besar+filenama[1:]
    filegambar=poke.json()['sprites']
    gambar=filegambar['front_default']
    idPoke=poke.json()['id']
    berat=poke.json()['weight']
    tinggi=poke.json()['height']
    files=[nama,gambar,idPoke,berat,tinggi]
    return render_template('hasil.html',x=files)   
    
@app.route('/NotFound')
def notFound():
    return render_template('error.html')

#404 route
@app.errorhandler(404)
def error404(error):
    return render_template('error.html')

if __name__ == "__main__":
    app.run(debug = True)

