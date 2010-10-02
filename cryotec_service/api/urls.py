from qtdjango.piston_handlers import get_url_pattens


from cryotec_service.cryotec_qtdjango_objects import models
urlpatterns = get_url_pattens(models)
