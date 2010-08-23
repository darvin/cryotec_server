from restclient.restful_lib import Connection
import json


ADDRESS = "http://127.0.0.1:8000"
API_PATH= "/api/"
CONNECTION =  Connection(ADDRESS)




def get_collection_from_server(resname):
    res = CONNECTION.request_get("%s%s" % (API_PATH,resname))["body"]
    #print res
    return json.loads(res)


class Service(object):
    def __init__(self):
        self.connection = Connection(ADDRESS)
        
        self.machine_list = self.get_from_server("machines")
        self.client_list =  self.get_from_server("clients")
    
    
    def get_reports(self):
        return self.get_from_server("reports")
    
    def get_from_server(self, resname):
        res = CONNECTION.request_get("%s%s" % (API_PATH,resname))["body"]
        return json.loads(res)


    def get_machine_name_by_id(self, id):
        for machine in self.machine_list:
            if machine["id"] == id:
                if machine["alias"]:
                    name = machine["alias"]
                elif machine["serial"]:
                    name = machine["serial"]
                else:
                    name = "%s_%s" % (machine["client"]["name"],machine["machinemark"]["name"])
                return name

    
if __name__ == "__main__":
    print get_collection_from_server("reports")