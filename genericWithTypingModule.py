from typing import TypeVar, Generic
from typeguard import typechecked

class Merhaba():pass
class Selam(Merhaba):pass
class Hello(Selam):pass
class Naber():pass
print(type(23.6))
T1 = TypeVar('T1',bound=Merhaba)#tek kullanımda bound zorunlu
T2 = TypeVar('T2',int,str)      #çoklu type tanımlama
print("Naber()---->",Naber())

@typechecked  #@typechecked --->T1 ve T2 tipini garanti altına alır
class Kutuphane(Generic[T1,T2]):
    def __init__(self, item: T1=None,item2:T2=None):
        self.item = item
        self.item2 = item2
        
    def get_item(self) -> T1:
        return self.item
    
merhaba=Merhaba()
selam=Selam()
hello=Hello()
naber=Naber()
#Kutuphane sınıfı yalnızca item1 Merhaba ve türevi ,item2 string,int tiplerle kullanılabilir.

print("------merhaba  instance ile----------------")
try: 
    kutuphane= Kutuphane(merhaba,15) #ok
    print(kutuphane.item)
    print(kutuphane.item2)
except TypeError as e:
    print("Error !!!------->",e)

print("------naber instance ile----------------")
try:
    kutuphane2= Kutuphane(naber,34)  # Error !!!
    print(kutuphane2.item)
    print(kutuphane2.item2)
except TypeError as e:
    print("Error !!!------->",e)
    
print("------selam instance ile----------------")
try:
    kutuphane3= Kutuphane(selam,"selam") #ok
    print(kutuphane3.item)
    print(kutuphane3.item2)
except TypeError as e:
    print("Error !!!------->",e)
print("------Hello() class ile----------------")
try:
    kutuphane4= Kutuphane(Hello(),"hellooooo") #ok
    print(kutuphane4.item)
except TypeError as e:
    print("Error !!!------->",e)
print("*******************************")
try:
    kutuphane5= Kutuphane(hello,21) #0k 
    print(kutuphane5.item)
    print(kutuphane5.item2)
except TypeError as e:
    print("Error !!!------->",e)
