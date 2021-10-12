from balance import app
from flask import render_template, request, redirect, url_for, flash
from balance.models import DBManager
from balance.forms import MovimientoFormulario
from date.time import 

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

    if request.method == 'GET':
        return render_template("nuevo_movimiento.html", el_formulario = formulario)     
    else:
        if formulario.validate():
            consulta = """
                INSERT INTO movimiento (fecha, concepto, ingreso_gasto, cantidad)
                 VALUES (:fecha, :concepto, :ingreso_gasto, :cantidad))
            """

            try:
                dbManager.modificaSQL(consulta, formulario.data)
            except Exception as e:
                print("Se ha producido un error de acceso a base de datos:", e)
                flash("Se ha producido un error en la base de datos. Consulte con su administrador")
                return render_template("nuevo_movimiento.html", el_formulario=formulario)

            return redirect(url_for("inicio"))
        else: 
            return render_template("nuevo_movimiento.html", el_formulario = formulario)
        """
        Validar formulario
        si la validación es OK -> insertar registro en tabla y redireccionar a /
        si la validacion es erronea -> devolver el formulario y render_template
            y preparar nuestra plantilla para gestionar los errores
        """

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    if request.method == 'GET':
        consulta = """
        SELECT id, fecha, concepto, ingreso_gasto, cantidad
        WHERE id = ?
        """
        movimiento = dbManager.consultaSQL(consulta, [id])
        if len(movimientos)  == 0:
            flash(f"Movimiento {id} no encontrado")
            return redirect(url_form("inicio"))
        el_movimiento= movimientos[0]
        el_movimiento['fecha']=date.formisoformat(el_movimiento["fecha"])
        formulario = MovimientoFormulario(data=el_movimiento)

        return render_template("borrar.html", el_formulario=formulario, id=el_movimiento['id'])

    return "holasoyunpost"