import jsonpickle
import jsonpickle.tags as tags
import jsonpickle.unpickler as unpickler
import jsonpickle.util as util

class Thing(object):
    pass

dct = {}
dct[tags.OBJECT] = util.importable_name(Thing)
dct['name'] = 'awesome'

obj = unpickler.Unpickler().restore(dct, classes=Thing)
assert isinstance(obj, Thing)
assert obj.name == 'awesome'


def from_json2(class_type, json_str):
    #Get the class type from py/type
    type_dict_str = to_json(class_type)
    json_type_dict = json.loads(type_dict_str)
    
    # Set the py/object with py/type from passed class
    json_dict = json.loads(json_str)
    json_dict.update({"py/object": json_type_dict["py/type"]})
    return decode(json.dumps(json_dict))