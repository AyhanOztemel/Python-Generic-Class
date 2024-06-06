def generic(cls):
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            self._property_types = {}
            super().__init__(*args, **kwargs)

        def __setattr__(self, name, value):
            if name.startswith('_'):
                # Check to prevent overwriting of properties and methods.
                super().__setattr__(name, value)
            else:
                if name not in self._property_types:
                    self._property_types[name] = type(value)
                elif not isinstance(value, self._property_types[name]):
                    raise TypeError(f"For property {name}, the type must be {self._property_types[name].__name__}, given {type(value).__name__}.")
                super().__setattr__(name, value)

    return Wrapper

# Decorator usage:
@generic
class Library:
    def __init__(self, item, item2,item3,item4,item5):
        self.item = item
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.item5 = item5
        
            # Usage example-1:       
k = Library("ayhan",54.89,21,"öztemel","kartal")

try:
    # initial assignment outputs  
    print(k.item)   # 'ayhan' gives the output.
    print(k.item2)  # 54.89 gives the output.
    print(k.item3)
    print(k.item4)
except TypeError as e:
    print(e)
    
print("----------------------------------------------")
try:
    k.item = "Mahmut" 
    k.item2 = 41.23    
    print(k.item)  # Ok! The first assignment is of type str.
    print(k.item2) # Ok! The first assignment is of type Float.
except TypeError as e:
    print(e)
    
try:
    k.item3=36.12  # Error!!! The first assignment is of type int.
    print(k.item3)
except TypeError as e:
    print(e)
print("----------------------------------------------")

             # Usage example-2:
k3 = Library(21,"hello",67,"ilknur","orhantaepe")

try:    
    k3.item = 42   # Ok! The first assignment is of type int.
    k3.item3 = 76  # Error!!! The first assignment is of type int.   
    print(k3.item)  
    print(k3.item4)
    print(k3.item5)
except TypeError as e:
    print(e)
    
try:
    k3.item2 = 34 #Error!!! The first assignment is of type str.
except TypeError as e:
    print(e)
    
try:
    k3.item3 ="ayhan" # Error!!! The first assignment is of type int.
except TypeError as e:
    print(e)    

print("----------------------------------------------")
             #------with class---------------
@generic
class Library2:
    def __init__(self, item, item2):
        self.item = item
        self.item2 = item2
             
class Merhaba():pass
class Selam(Merhaba):pass
class Hello():pass
class Naber(Selam):pass

#instance created
merhaba=Merhaba()
selam=Selam()
hello=Hello()

#  Usage example-3
k2 = Library2(Merhaba,Selam)  #It can be class or instance
try:  
    print(k2.item)  
    print(k2.item2)
except TypeError as e:
    print(e)
    
print("----------------------------------------------")
try:                #Inheritance
    k2.item =Naber  #Merhaba()-->Selam()--->Naber()
    print(k2.item)
except TypeError as e:
    print(e)
    
print("----------------------------------------------")
try:
    k2.item2=Hello() #Error!!! Hello() or the class that inherits it can be assigned
    print(k2.item2)  #Because the first assignment is Hello()
except TypeError as e:
    e="bad assignment!!! \n Selam() or the class that inherits it can be assigned \n because the first assignment is Selam()"
    print(e)
