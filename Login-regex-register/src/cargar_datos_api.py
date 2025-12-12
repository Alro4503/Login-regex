import requests
import pandas as pd
import os


def get_pokemon_data(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    respuesta = requests.get(url)

    if respuesta.status_code != 200:
        print("Pokémon no encontrado.")
        return None
    
    return respuesta.json()


def analyze_stats(pokemon):
    stats = {s["stat"]["name"]: s["base_stat"] for s in pokemon["stats"]}

    max_stat = max(stats, key=stats.get)
    min_stat = min(stats, key=stats.get)

    neutral_stats = {k: v for k, v in stats.items() if k not in (max_stat, min_stat)}

    print("\n=== STATS ===")
    print(f"  Más fuerte:   {max_stat} ({stats[max_stat]})")
    print(f"  Más débil:    {min_stat} ({stats[min_stat]})")
    print("  Neutrales:")
    for k, v in neutral_stats.items():
        print(f"    - {k}: {v}")


def analyze_types(pokemon):
    types = [t["type"]["name"] for t in pokemon["types"]]

    print("\n=== TIPOS ===")
    print("  Tipos del Pokémon:", ", ".join(types))

    strengths = set()
    weaknesses = set()
    resistances = set()
    immunities = set()

    for t in types:
        type_data = requests.get(f"https://pokeapi.co/api/v2/type/{t}").json()
        relations = type_data["damage_relations"]

        weaknesses.update([x["name"] for x in relations["double_damage_from"]])
        strengths.update([x["name"] for x in relations["double_damage_to"]])
        resistances.update([x["name"] for x in relations["half_damage_from"]])
        immunities.update([x["name"] for x in relations["no_damage_from"]])

    print("\n  Fortalezas (hace doble daño):")
    print("    " + ", ".join(strengths) if strengths else "    Ninguna")

    print("\n  Debilidades (recibe doble daño):")
    print("    " + ", ".join(weaknesses) if weaknesses else "    Ninguna")

    print("\n  Resistencias (recibe mitad de daño):")
    print("    " + ", ".join(resistances) if resistances else "    Ninguna")

    print("\n  Inmunidades (no recibe daño):")
    print("    " + ", ".join(immunities) if immunities else "    Ninguna")


def guardar_imagen(pokemon):
    nombre = pokemon["name"]
    url_imagen = pokemon["sprites"]["front_default"]

    if url_imagen is None:
        print("Este Pokémon no tiene sprite disponible.")
        return

    # Crear carpeta si no existe
    os.makedirs("images", exist_ok=True)

    # Descargar
    imagen = requests.get(url_imagen)

    # Guardar imagen
    with open(f"images/{nombre}.png", "wb") as f:
        f.write(imagen.content)

    print(f"\nImagen guardada en images/{nombre}.png")


# PROGRAMA PRINCIPAL

pokemon_name = input("Nombre del Pokémon: ")
pokemon = get_pokemon_data(pokemon_name)

if pokemon:

    nombre = pokemon["name"]
    id_num = pokemon["id"]
    tipos = [t["type"]["name"] for t in pokemon["types"]]
    peso = pokemon["weight"]
    altura = pokemon["height"]

    analyze_stats(pokemon)
    analyze_types(pokemon)
    guardar_imagen(pokemon)

    df = pd.DataFrame([{
        "Nombre": nombre,
        "ID": id_num,
        "Tipos": ", ".join(tipos),
        "Peso": peso,
        "Altura": altura
    }])

    print("\n--- Datos del Pokémon ---")
    print(df)
