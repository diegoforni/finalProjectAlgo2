import json

with open('C:\\Users\\juana\\OneDrive\\Documents\\GitHub\\ProjectFinalAlgo2\\semantic\\sinonimos.json', 'r') as archivo:
    data = json.load(archivo)

def leerSinonimos(palabra):
    for apartado in data:
        for sinonimo in data[apartado]:
            if palabra == sinonimo:
                return apartado


print(leerSinonimos("realidad virtual"))

