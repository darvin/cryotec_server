# -*- coding: UTF-8 -*-


'''
@author: darvin
'''


from qtdjango.helpers import get_registered_models

models = get_registered_models("/home/darvin/workspace/cryotec_service/cryotec_service", \
                              ["machines","actions","actiontemplates","clients",],
                              ("Action", "PAction",))

current_module =__import__(__name__)

for model in models:
    setattr(current_module, model.__name__, model)


print dir(current_module)

if __name__=="__main__":
    print models
    for model in models:
        print model.__name__, model.resource_name
        model.load()
