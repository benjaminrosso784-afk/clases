import requests
import csv
import os
import sqlite3

os.makedirs("csv", exist_ok=True)

pokemenoes = []
for i in range(1, 20):
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

con = sqlite3.connect('pokemons.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS pokemones"
            "(nombre TEXT, peso INTEGER)")
for s in pokemenoes:
    cur.execute("INSERT INTO pokemones VALUES (? , ?)", (s["nombre"], s["peso"]))
con.commit()
for fila in cur.execute("SELECT * FROM pokemones"):
    print(fila)