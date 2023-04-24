from .db import conn, cur

class JsonFilter:
    def __init__(self, json_array):
        self.json_array = json_array

    def filter(self, args):
        return list(filter(lambda x: all(x.get(key) == value for key, value in args.items()), self.json_array))
    
def headlineFilter():
    print('starting headling filter options fcuntion')
    conn
    #list of filter parameters
    filterParams={}
    if 
    
