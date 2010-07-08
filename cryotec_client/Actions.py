'''
@author: darvin
'''

class AbstractAction(object):
    '''
    classdocs
    '''
    icon = "blackboard_drawing"
    title = "Весь журнал"

    def __init__(self):
        '''
        Constructor
        '''
        raise NotImplementedError
    
    
class Report(AbstractAction):
    icon = "bug"
    title = "Неисправности"

class Fix(AbstractAction):
    icon = "brick"
    title = "Ремонт"

    
class Checkup(AbstractAction):
    icon = "date"
    title = "Профосмотр"

    
class Maintenance(AbstractAction):
    icon = "time"
    title = "Техобслуживание"
