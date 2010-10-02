# -*- coding: UTF-8 -*-


'''
@author: darvin
'''


from cryotec_service.cryotec_qtdjango_objects import models
from qtdjango.helpers import get_registered_models

models = get_registered_models(models)

current_module =__import__(__name__)

for model in models:
    model.load()
    setattr(current_module, model.__name__, model)
for model in models:
    model.refresh_foreing_keys()
    model.printall_foreing_keys()


if __name__=="__main__":
    print models
    for model in models:
        print model.__name__, model.resource_name
        model.load()