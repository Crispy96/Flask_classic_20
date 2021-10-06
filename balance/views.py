from balance import app
from flask import render_template, request
from balance.models import DBManager
from balance.forms import MovimientoFormulario

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS")
dbManager = DBManager(ruta_basedatos)


@app.route("/")
def inicio():

    consulta = """
        SELECT * 
          FROM movimiento 
         ORDER BY fecha;
    """
    movimiento = dbManager.consultaSQL(consulta)

    return render_template("inicio.html", items=movimiento)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()
    return render_template("nuevo_movimiento.html", el_formulario = formulario)



    return "Pagina de alta de movimiento"

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    return f"Pagina de borrado de {id}"