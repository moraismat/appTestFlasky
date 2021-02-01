from flask_wtf import FlaskForm
from flask_appbuilder.forms import DynamicForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class Form(DynamicForm):
    nome = StringField('Qual o seu nome?', validators=[DataRequired()])
    tipo_entidade = RadioField('Que tipo de usuario voce é?', choices=[('Cliente', 'C'), ('F', 'Fornecedor')])  
    valor = StringField('Quanto você quer investir?')
    submit = SubmitField('Cadastrar!')
