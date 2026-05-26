import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    # Completando a URL base com o nome do pokémon escolhido
    url = f"{base_url}/pokemon/{name}"
    # requests.get() vai retornar um objeto de resposta, que está sendo armazenado na variável response
    response = requests.get(url)

    # Se o response retornar 200, isso significa que a requisição deu certo
    # A função json() converte o objeto response em um dicionário Python, que terá a estrutura chave: valor
    # Portanto, pokemon_data é um dicionário
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data 
    else:
        print(f"Failed. Error code: {response.status_code}")    

while True:
    pokemon_name = input("Digite o nome do Pokémon: ")
    # pokemon_name é o parâmetro nane da função get_pokemon_info
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        break
    print("Esse pokémon não existe na PokéAPI. Tente novamente.")

# Convertendo altura de decímetros para METROS e peso de hectogramas para KG
height_m = pokemon_info['height']/10
weight_kg = pokemon_info['weight']/10

if pokemon_info:
    print(f"ID do Pokémon: {pokemon_info['id']}")
    print(f"Nome do Pokémon: {pokemon_info['name'].capitalize()}")
    print(f"Altura do {pokemon_name.capitalize()}: {height_m} metros")
    print(f"Peso do {pokemon_name.capitalize()}: {weight_kg} KG")


