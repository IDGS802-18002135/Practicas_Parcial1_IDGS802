from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField,RadioField,DecimalField
from wtforms import EmailField

class HoroscopoForm(Form):
    nombre=StringField('nombre')
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    dia = SelectField(choices=[    ('1', '1'),    ('2', '2'),    ('3', '3'),    ('4', '4'),    ('5', '5'),    ('6', '6'),    ('7', '7'),    ('8', '8'),    ('9', '9'),    ('10', '10'),    ('11', '11'),    ('12', '12'),    ('13', '13'),    ('14', '14'),    ('15', '15'),    ('16', '16'),    ('17', '17'),    ('18', '18'),    ('19', '19'),    ('20', '20'),    ('21', '21'),    ('22', '22'),    ('23', '23'),    ('24', '24'),    ('25', '25'),    ('26', '26'),    ('27', '27'),    ('28', '28'),    ('29', '29'),    ('30', '30'),    ('31', '31')])
    mes = SelectField(choices=[    ('1', '1'),    ('2', '2'),    ('3', '3'),    ('4', '4'),    ('5', '5'),    ('6', '6'),    ('7', '7'),    ('8', '8'),    ('9', '9'),    ('10', '10'),    ('11', '11'),    ('12', '12')])

    anio=DecimalField('año')
    sexo=RadioField('Sexo',choices=[('masculino','masculino'),('femenino','femenino')])

       

