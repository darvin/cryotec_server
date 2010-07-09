import pyjd

from pyjamas.JSONService import JSONProxy
from pyjamas.JSONParser import JSONParser



class RemoteService(JSONProxy):
    def __init__(self):
        JSONProxy.__init__(self, "/json/", 
                             [  "clients_getAll",
                                "checklists_getA",
                                "machines_getAll",
                                "clients_get",
                                "machines_get",
                                "machines_getMark",
                                "checklists_getAllQ",
                                "checklists_getQ",
                                "checklists_getAllA",
                                "machines_getByClient",
                                "machines_getType",
                                "actions_getAll",
                                "clients_getAll",
                                "actions_get",
                                "actions_getByMachine",
                              ])
        
        try:
            from jsonrpc.json import dumps, loads, JSONDecodeException
            self.decode=loads
            self.encode=dumps
        except ImportError:
            from pyjamas.JSONParser import JSONParser
            parser = JSONParser()
            self.encode = getattr(parser, 'encode')
            self.decode = getattr(parser, 'decodeAsObject')
            JSONDecodeException = None 
        
#        self.parser = JSONParser()
#
#        
#    def decode(self, st):
#        return self.parser.decode(st)

        

jsonrpc_proxy = RemoteService()


        
if __name__=="__main__":
    pass
      
