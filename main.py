
class Legs:
    def walk(self):
        print(self.name+" is walking")
        
    def jump(self):
        print(self.name+" is jumping")  
              
    def crawl(self):
        print(self.name+" is crawling")
        
    def stand(self):
        print(self.name+" is standing")


class Eyes:
    def look(self):
        print(self.name+" is looking")
        
    def stare(self):
        print(self.name+" is staring")  
              
    def blink(self):
        print(self.name+" is blinking")
        
    def cry(self):
        print(self.name+" is crying")
        

class Hands:
    def wave(self):
        print(self.name+" is waving")
        
    def punch(self):
        print(self.name+" is punching")  
              
    def hold(self):
        print(self.name+" is holding")
        
    def stand(self):
        print(self.name+" is standing")
        
class Head:
    def nod(self):
        print(self.name+" is nodding")
        
    def eat(self):
        print(self.name+" is eating")  
              
                          
                
def include(*other_objs):
    def inner(obj): 
        for other_obj in other_objs:
            functions = list(filter( lambda x: not "__" in x, dir(other_obj))) # the inspect module should used to include more cases
            for func in functions:
                fn = (getattr(other_obj, func))
                setattr(obj, func, fn)
        return obj
        
    return inner        

@include(Legs, Hands, Eyes, Head)        
class Person:
    
    def __init__(self, name:str) -> None:
        self.name = name        
        
        
@include(Legs, Head)        
class Monster:  
    
    def __init__(self, name:str="monster") -> None:
        self.name = name   


class Unknown:  
    
    def __init__(self, name:str="unknown") -> None:
        self.name = name                     
        

if __name__ == "__main__":
        
    unknown = include(Legs, Head)(Unknown)() # inlined version
    monster = Monster()
    person = Person("mario")
    
    person.jump()
    monster.eat()
    unknown.nod()


