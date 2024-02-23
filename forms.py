from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField,RadioField
from wtforms import EmailField
from wtforms import validators

class DistanciaForm(Form):
    x1=StringField("x1")
    x2=StringField("x2")
    y1=StringField("y1")
    y2=StringField("y2")

class DiccionarioForm(Form):
    espaniol=StringField("Español",[validators.DataRequired(message='el campo es requerido')])
    ingles=StringField("Ingles",[validators.DataRequired(message='el campo es requerido')])

class TraductorForm(Form):
    idioma = RadioField("Idioma", choices=[('español', 'español'), ('ingles', 'ingles')], validators=[validators.DataRequired(message='El campo es requerido')])
    palabra=StringField("Palabra",[validators.DataRequired(message='el campo es requerido')])
   
   