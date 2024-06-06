from typing import Generic, TypeVar, Any, Callable
T = TypeVar("T")

class TypeSafe(Generic[T]):
    def __init__(self, value: T, value2: T, value3: T) -> None:
        self._value: T = value
        self._value2: T = value2
        self._value3: T = value3

    @property
    def value(self) -> T:
        return self._value
    
    @value.setter 
    def value(self, new_value: T) -> None:
        if not isinstance(new_value, type(self._value )):
            raise TypeError(f"Hatalı tip  Giriş --->{type(self._value )} tipinde olmalıdır ")
        else:self._value = new_value
 
    @property
    def value2(self) -> T:
        return self._value2
    
    @value2.setter
    def value2(self, new_value: T) -> None:
        if not isinstance(new_value, type(self._value2 )):
            raise TypeError(f"Hatalı tip  Giriş --->{type(self._value2 )} tipinde olmalıdır ")
        else:self._value2= new_value
        
    @property
    def value3(self) -> T:
        return self._value3
    
    @value3.setter  
    def value3(self, new_value: T) -> None:
        if not isinstance(new_value, type(self._value3 )):
            raise TypeError(f"Hatalı tip  Giriş --->{type(self._value3 )} tipinde olmalıdır ")
        else:self._value3= new_value
            
# Kullanım örneği
x = TypeSafe(10,"Ayhan",22.34)
print(x.value)
print(x.value2)
print(x.value3)
try:
    x.value = "11"  # Hata oluşur, çünkü "11" bir int değer değildir
    print(x.value)
except TypeError as e:
    print(e)

try:
    x.value2 ="21a"    # ok
    print(x.value2)    
except TypeError as e:
    print(e)
    
try:
    x.value2 =21    # ok
    print(x.value2)    
except TypeError as e:
    print(e)
    
try:
    x.value3 ="merhaba" # Hata oluşur, çünkü "Merhaba Dünya" bir int değer değildir
    print(x.value3)
except TypeError as e:
    print(e)
