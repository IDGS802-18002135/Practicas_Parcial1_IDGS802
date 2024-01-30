from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField,RadioField
from wtforms import EmailField

class DistanciaForm(Form):
    x1=StringField("x1")
    x2=StringField("x2")
    y1=StringField("y1")
    y2=StringField("y2")
   
   