'''
@author: darvin
'''
from pyjamas.ui.Composite import Composite
from pyjamas.ui.HTML import HTML
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.SimplePanel import SimplePanel
from Actions import Fix, Maintenance, Report, Checkup, AbstractAction
from pyjamas.ui import HorizontalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.CustomButton import CustomButton
from pyjamas.ui.Label import Label
from pyjamas.ui.Image import Image
from pyjamas import Window
from pyjamas.ui.DialogBox import DialogBox


from JsonRpcProxy import jsonrpc_proxy


ICON_PATTERN = "fatcow/%s.png"
BIG_ICON_PATTERN = "fatcow/32/%s.png"

class AbstractTab(SimplePanel):
    '''
    classdocs
    '''
    icon = "abstracticon"
    title = "Абстрактный конь в вакууме"

    def get_title(self):
        icon = ICON_PATTERN % self.icon
        return '<nobr><img src="%s">%s</nobr>'%(icon,self.title)

    def __init__(self, app):
        '''
        Constructor
        '''
        SimplePanel.__init__(self)
        self.app = app

        
        
    def refresh(self):
        raise NotImplementedError
    
    
    
class MachineTab(AbstractTab):
    
    icon = "information"
    title = "Информация"
    
    def __init__(self, app):
        AbstractTab.__init__(self, app)
        self.panel = VerticalPanel()
        self.panel.add(HTML("Здесь будет информация про машину в более читаемом виде"))
        self.html = HTML()
        self.panel.add(self.html)
        self.add(self.panel)
        self.app.machine_filter.add_handler("client","machines_get",self)
        self.app.machine_filter.add_handler("machine","machines_get",self)
        self.app.machine_filter.add_handler("mark","machines_get",self)
        

            
    def onRemoteResponse(self, response, request_info):
        if (self.app.machine_filter.is_not_blank()):
            response_decoded = jsonrpc_proxy.decode(response)
            self.html.setHTML("%s"%response_decoded)
        
    def onRemoteError(self, code, message, request_info):
        print "error"
        print ("error %s" % str(message))
        
    



class AlarmsTab(AbstractTab):
    
    icon = "alarm_bell"
    title = "Оповещения"
    
    def __init__(self, app):
        AbstractTab.__init__(self, app)
        self.add(HTML("Здесь будут оповещения о предстоящих событиях и способы управления ими"))
        


    
class ActionTab(AbstractTab):
    
    action = AbstractAction
    icon = action.icon
    title = action.title
    button_list = (("Неисправность","bug_add"),
                   ("Ремонт","brick_add"),
                   ("Профосмотр","date_add"),
                   ("Техобслуживание","time_add"),
                   ("Удалить","database_delete"),
                   ("Редактировать","database_edit"),
                   )
    
    def __init__(self, app):
        AbstractTab.__init__(self, app)
        self.panel = VerticalPanel()
        self.add(self.panel)
        toolbar = HorizontalPanel()
        
#        b = CustomButton(HTML('<img src="fatcow/brick.png">hi'))
#    
#        toolbar.add(b)
        for buttontext, buttonimg in self.button_list:
            bimg = Image(BIG_ICON_PATTERN % buttonimg)
            blabel = Button(buttontext, self.showDialog)
            toolbar_btn = HorizontalPanel()
            toolbar_btn.add(bimg)
            toolbar_btn.add(blabel)
            toolbar_btn.setPadding(8)
            toolbar.add(toolbar_btn)
            
        
        self.panel.add(toolbar)
        self.panel.add(HTML("снизу табличка"))
        self.html = HTML()
        self.panel.add(self.html)
        
        self.app.machine_filter.add_handler("client","actions_getByMachine",self)
        self.app.machine_filter.add_handler("machine","actions_getByMachine",self)
        self.app.machine_filter.add_handler("mark","actions_getByMachine",self)
        
        
        
    def showDialog(self, event):
        contents = VerticalPanel(StyleName="Contents",
                                 Spacing=4)
        contents.add(HTML('Тут будут формы ввода, подтверждения и т.д.'))
        contents.add(Button("Close", getattr(self, "onClose")))
        

        self._dialog = DialogBox(glass=True)
        self._dialog.setHTML('<b>Диалоговое окно</b>')
        self._dialog.setWidget(contents)

        left = (Window.getClientWidth() - 200) / 2 + Window.getScrollLeft()
        top = (Window.getClientHeight() - 100) / 2 + Window.getScrollTop()
        self._dialog.setPopupPosition(left, top)
        self._dialog.show()
        

    def onClose(self, event):
        self._dialog.hide()
        
        
            
    def onRemoteResponse(self, response, request_info):
        response_decoded = jsonrpc_proxy.decode(response)
        self.html.setHTML("%s"%response_decoded)
        
    def onRemoteError(self, code, message, request_info):
        print "error"
        print ("error %s" % str(message))


class ReportTab(ActionTab):
    action = Report
    icon = action.icon
    title = action.title
    button_list = (("Новая неисправность","bug_add"),
               ("Удалить","bug_delete"),
               ("Редактировать","bug_edit"),
               )



class FixTab(ActionTab):
    action = Fix
    icon = action.icon
    title = action.title
    button_list = (("Новый ремонт","brick_add"),
           ("Удалить","brick_delete"),
           ("Редактировать","brick_edit"),
           )
    
    
    
class CheckupTab(ActionTab):
    action = Checkup
    icon = action.icon
    title = action.title
    button_list = (("Новый профосмотр","date_add"),
           ("Удалить","date_delete"),
           ("Редактировать","date_edit"),
           )
    
class MaintenanceTab(ActionTab):
    action = Maintenance
    icon = action.icon
    title = action.title
    button_list = (("Новое техобслуживание","time_add"),
               ("Удалить","time_delete"),
               ("Редактировать","time_go"),
               )    

    
TAB_CLASSES = (MachineTab,
               ActionTab,
#               ReportTab,
#               FixTab,
#               CheckupTab,
#               MaintenanceTab,
#               AlarmsTab,
               )
  
