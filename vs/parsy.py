from parse import parse, search

githubs = [
    "https://github.com/koaning/justcharts/",
    "https://github.com/koaning/human-learn/",
    "https://github.com/r1chardj0n3s/parse/",
]

lista = [parse("https://github.com/{owner}/{repo}/", url).named for url in githubs]
print(lista)

s = search("https://github.com/{owner}/{repo}/", "https://github.com/koaning/human-learn/")
print(s)
