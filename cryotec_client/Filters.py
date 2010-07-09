
import new
import types



from JsonRpcProxy import jsonrpc_proxy





class Filter(dict):
    def setter(self):
        l = []
        for key in self.keys_names:
            l.append(self[key])
#        print l
        for method in self.handlers[self.lastkey]:
            jsonrpc_proxy.callMethod(method, l, self)
   
    def __init__(self, *values_list):
        dict.__init__(self, zip(self.keys_names, values_list))
        self.handlers = {}
        for k in self.keys_names:
            self.handlers[k] = {}
    
    def add_handler(self, key_name, method_name, handler):
        try:
            self.handlers[key_name][method_name].append(handler)
        except KeyError:
            self.handlers[key_name][method_name] = []
            self.handlers[key_name][method_name].append(handler)
            
   
    def __getattr__(self, key):
        return self[key]
    
    def set(self, key, value):
        self[key] = value
        self.lastkey = key
#        if value != -1:
        l = self.keys_names[:self.keys_names.index(key)]
        l.reverse()
        for k in l:
            self[k] = -1
        self.setter()
        
    
    def __setattr__(self, key, value):
        if key in ["refreshers", "handlers", "lastkey"]:
            dict.__setattr__(self, key, value)
        else:
            raise AssertionError
    
    def is_not_blank(self):
        for key in self:
            if self[key]!=-1:
                return True
        return False
    
    def onRemoteResponse(self, response, request_info):
        for handler in self.handlers[self.lastkey][request_info.method]:
            handler.onRemoteResponse(response, request_info)
        
    def onRemoteError(self, code, message, request_info):
        for handler in self.handlers[self.lastkey][request_info.method]:
            handler.onRemoteError(code, message, request_info)
        

class MachineFilter(Filter):
    keys_names = [ "machine","mark", "client",]
    handlers = {"client":{},
                "mark":{},
                "machine":{},
                }
    


class ActionFilter(Filter):
    keys_names = ["client", "mark", "machine"]
    jsonrpc_method = "actions_get"