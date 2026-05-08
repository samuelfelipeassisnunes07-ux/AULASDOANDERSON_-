from pprint import pprint

filmes = {
    "filme1": {
        "titulo": "O Poderoso Chefão",
        "ano": 1972,
        "diretor": "Francis Ford Coppola",
        "atores": ["Marlon Brando", "Al Pacino", "James Caan"]
    },
    "filme2": {
        "titulo": "Pulp Fiction",
        "ano": 1994,
        "diretor": "Quentin Tarantino",
        "atores": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]
    },
    "filme3": {
        "titulo": "A Origem",
        "ano": 2010,
        "diretor": "Christopher Nolan",
        "atores": ["Leonardo DiCaprio", "Marion Cotillard", "Ellen Page"]
    }
}

print("=== Todos os filmes ===")
pprint(filmes)

print("\n=== Primeiro filme ===")
pprint(filmes["filme1"])

print("\n=== Título do segundo filme ===")
print(filmes["filme2"]["titulo"])
