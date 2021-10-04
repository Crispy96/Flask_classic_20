#creamos las rutas de inicio y de otros movimientos
from balance import app

@app.route("/")
def inicio():
    return "Paguina de inicio"

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return "Paguina de alta de movimiento"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])   #sirve para borrar la posición que queramos
def borrar(id):
    return f"Paguina de borrado de {id}" 