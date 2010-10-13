# -*- coding: UTF-8 -*-


'''
@author: darvin
'''


from qtdjango.modelsmanager import ModelsManager

ADDRESS = "http://127.0.0.1:8000"
API_PATH= "/api/"
mm = ModelsManager(ADDRESS, API_PATH, "/home/darvin/workspace/cryotec_service/cryotec_service", \
                              ["machines","actions","actiontemplates","clients","checklists"],
                              ("Action", "PAction",))

current_module =__import__(__name__)



mm.do_models_magic_with_module(current_module)

if __name__ == '__main__':
    print Machine.all()
    m1 = Machine.new()
    m1.save()
    m2 = Machine.new()
    m2.save()

    from pprint import pprint
    for m in Machine.all():
        pprint (m.__dict__)
