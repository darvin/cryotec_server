from qtdjango.piston_handlers import get_url_pattens



BASE_PACKAGE_NAME = "cryotec_service"
APPS = ["clients",
        "actions",
        "machines",
        
        "actiontemplates",
        "checklists",
        "files",
        ] 
urlpatterns = get_url_pattens(BASE_PACKAGE_NAME, APPS)

