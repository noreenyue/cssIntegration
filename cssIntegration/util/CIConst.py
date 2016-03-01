# -*- coding: UTF-8 -*- 
class _const: 
    class ConstError(TypeError):pass 
    def __setattr__(self, name, value): 
        if self.__dict__.has_key(name): 
            raise self.ConstError, "Can't define constant (%s)" %name 
        self.__dict__[name]=value 
        
Constants = _const() 
Constants.CSS_SUFFIX = ".css"
Constants.IMPORT_PREFFIX = "@import"
