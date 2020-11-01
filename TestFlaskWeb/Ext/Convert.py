import json
from datetime import date, datetime
from collections import namedtuple
from Models.Text import Text
class AdvancedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return obj.__dict__

class ConvertObjExt:
    def __init__(self, obj):
        self.Obj = obj

    def ToString(self):
        #將 Class 物件轉成 JsonStr
        str = json.dumps(self.Obj, cls=AdvancedJSONEncoder)
        return str
    def ToJson(self):
        str = self.ToString()
        #將 JsonStr 轉成 數據格式
        return json.loads(str)

    def ToClass(self,type):
        str = self.ToString()
        obj = json.loads(str, object_hook=self.__customDecoder__)
        
        return type(*obj)

    def __customDecoder__(self,obj):
        return namedtuple(type(obj).__name__, obj.keys())(*obj.values())

class ConvertArrayExt():
    def __init__(self, list):
        self.list = list

    def ToArrayString(self):
        #將 List 物件轉成 JsonStr
        result = []
        
        for item in self.list:
            str = ConvertObjExt(item).ToString()
            result.append(str)
        return result
    def ToArrayJson(self):
        str = self.ToArrayString()
        #將 JsonStr 轉成 數據格式
        return json.loads(str)

    def ToList(self):
        result = []
        for item in self.list:
            obj = ConvertObjExt(item).ToClass()
            result.append(obj)
        return result

    

    