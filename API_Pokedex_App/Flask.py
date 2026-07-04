# Imports
from flask import Flask, render_template, request
import requests

app = Flask (__name__)

# URL
url_base = 'https://pokeapi.co/api/v2/pokemon'

# def get_pokemon_info
def get_pokemon_info(name):
    url = f"{url_base}/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  


# rota
@app.route('/', methods=['GET', 'POST'])
def index():
    pokemon = None
    error = None

    if request.method == 'POST':
        name = request.form.get('pokemon_name', '').strip()
        data = get_pokemon_info(name)

        if data:
            pokemon = {
                'id': data['id'],
                'name': data['name'].capitalize(),
                'height': data['height']/10,
                'weight': data['weight']/10, 
                'abilities': [
                    {'name': a['ability']['name'].capitalize(), 'hidden': a['is_hidden']} for a in data['abilities']
                ],
                'types': [t['type']['name'].capitalize() for t in data['types']],
                # Testando a visualização de Sprite
                'sprite': data['sprites']['front_default']
            }
        else:
            error = f"{name} não foi encontrado"    

    return render_template('index.html', pokemon=pokemon, error=error)


if __name__ == '__main__':
    app.run()