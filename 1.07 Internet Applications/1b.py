from flask import Flask

app = Flask(__name__)

suma = ""

@app.route("/add/<liczba1>/<liczba2>")
def add(liczba1, liczba2):

    try:
        suma = int(liczba1) + int(liczba2)
    except ValueError:
        return "Podaj liczbę!"

    return "Suma wynosi {}".format(str(suma)) #return musi byc stringiem

app.run(debug=True)