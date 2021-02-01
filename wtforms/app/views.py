from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app import appbuilder

from .models import usuario


class CrudUsuario(ModelView):
    datamodel = SQLAInterface(usuario)    
    after_model_change ={
        
    }


appbuilder.add_view(CrudUsuario, "Usuario")