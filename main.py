from flask import Flask, render_template, request
import requests
import json
import time
import random

app = Flask(__name__)

total = 898

color = {
    'Fire': '#FDDFDF',
    'Grass': '#DEFDE0',
    'Electric': '#FCF7DE',
    'water': '#DEF3FD',
    'Ground': '#f4e7da',
    'Rock': '#d5d5d4',
    'Fairy': '#fceaff',
    'Poison': '#98d7a5',
    'Bug': '#f8d5a3',
    'Dragon': '#97b3e6',
    'Psychic': '#eaeda1',
    'Flying': '#F5F5F5',
    'Fighting': '#E6E0D4',
    'Normal': '#F5F5F5',
    'Ice': "#DEF3FD",
    'Ghost': "#98d7a5",
    'Steel': "#F5F5F5",
    'Dark': "#FFFFFF",
}

f = open('sample.json')
pokemons = json.load(f)


@app.route("/", methods=['GET'])
def home():
    pokemon = {}
    for i in range(10):
        id = random.randint(0, 898)
        pokemon[id] = pokemons[str(id)]

    return render_template("index.html", pokemons=pokemon, color=color, types=color.keys(), time=time,
                           pic_height="max-width:auto;display:flex;")


@app.route("/pokedex", methods=['GET'])
def pokedex():
    return render_template("pokedex.html", pokemons=pokemons, color=color, time=time)


@app.route("/detail/<id>", methods=['GET', 'POST'])
def detail(id):
    if id == "search":
        search_input = request.form['search']

        if not search_input:
            return render_template('notfound.html')

        if not search_input.isdigit():
            search_input.lower()
            found = False
            similar = {}
            input = search_input.lower()
            for pokemon in pokemons.values():
                if input == pokemon["name"]:
                    found = True
                    break

                if input in pokemon["name"]:

                    similar[str(pokemon["id"])] = pokemon

            if not found:

                if similar:
                    return render_template('pokedex.html', pokemons=similar, color=color, time=time)

                return render_template('notfound.html')

        else:
            id = search_input

    if int(id) > 898:
        return render_template('notfound.html')

    return render_template('detail.html', pokemon=pokemons[id], color=color)


if __name__ == "__main__":
    app.run(debug=True)

#

# pokemons = {}
# for i in range(1, 899):
#
#     pokemon = {}
#     url = "https://pokeapi.co/api/v2/pokemon/{}".format(i)
#     f = requests.get(url)
#     data = json.loads(f.content)
#
#     pokemon["id"] = i
#     pokemon["name"] = data["name"]
#
#     pokemon["type"] = [slot["type"]["name"].capitalize() for slot in data['types'] ]
#
#     pokemon["ability"] = [ab["ability"]["name"] for ab in data["abilities"]]
#
#     pokemons[str(i)] = pokemon
#
# with open("sample.json", "w") as outfile:
#     json.dump(pokemons, outfile)
# f = open('sample.json')
# pokemons = json.load(f)
