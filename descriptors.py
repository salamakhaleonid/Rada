class IntDescriptor:
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        assert value > 0
        setattr(instance, self.name, value)


class StringDescriptor:
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        assert len(value) > 3
        setattr(instance, self.name, value)



class MetaRada(type):
    counter = 0

    def __new__(cls, name, bases,dct):
        new_dict = dict()

        for key, value in dct.items():
            if key.startwith ("_"):
                new_dict[key] = value
            elif key == "int_types":
                for int_type in value:
                    new_dict[int_type] = IntDescriptor()
                    cls.counter += 1
            elif key == "str_types":
                for str_type in value:
                    new_dict[str_type] = IntDescriptor()
                    cls.counter += 1

        return type.__new__(cls,name,bases,new_dict)

def singleton(cls):
    instance = {}     # why not list?

    def get_instance(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return get_instance
