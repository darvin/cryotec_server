from qtdjango.piston_handlers import get_url_pattens

urlpatterns =\
 get_url_pattens(("machines","actions","actiontemplates","clients","checklists"))
