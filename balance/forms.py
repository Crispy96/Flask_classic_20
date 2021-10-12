#FORMULARIO
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, FloatField, RadioField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

import datetime

def validar_fecha(formulario, campo):
    hoy = datetime.date.today()  #date de hoy
    if campo.data > hoy:
        raise ValidationError("La fecha no puede ser posterior a hoy ")

class MovimientoFormulario(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired(message="Debe informar la fecha")])
    concepto = StringField("Concepto", validators=[DataRequired(message="Debe informar el concepto"), Length(min=10)])
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debe  informar el monto del movimiento"), 
                                                  NumberRange(message="Debe informar un importe positivo", min=0.01)])
    ingreso_gasto = RadioField(validators=[DataRequired(message="Debe informar el tipo de movimiento")], 
                                            choices=[('G', 'Gasto'), ('I', 'Ingreso')])

    submit = SubmitField('Aceptar') 

    #lo defino dentro o lo defino fuera y luego lo adjunto
    def validate_fecha(self, campo):
        hoy = datetime.date.today()  #date de hoy
        if campo.data > hoy:
            raise ValidationError("La fecha no puede ser posterior a hoy ")