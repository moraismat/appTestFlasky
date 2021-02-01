from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from wtforms import( DateField, TextField, FloatField, RadioField, SelectField,
        Form, IntegerField, validators, StringField, FormField
    )

class usuario(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    tipo_entidade = Column(String(1), nullable=True)
    valor = Column(Float)
    novo_valor = Column(Float)

    def __init__(self):
        self.novo_valor = self.valor

    def __repr__(self):
        return self.name
