import requests
import csv
import os

os.makedirs("csv", exist_ok=True)

pokemenoes = []
for i in range(1, 152):
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    respuesta = requests.get(url)
    data = respuesta.json()
    p = {   
        "id": data["id"],
        "nombre": data["name"],
        "peso": data["height"],
        "altura": data["weight"],
        "tipo": [t["type"]["name"] for t in data["types"]],
        }
    pokemenoes.append(p)

with open("pokemons.csv", "w", newline="") as csvfile:
    fieldnames = ["id", "nombre", "peso", "altura", "tipo"] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for p in pokemenoes:
        writer.writerow(p)
