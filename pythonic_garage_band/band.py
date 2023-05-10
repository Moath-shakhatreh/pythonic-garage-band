
class Musician :
    
    @classmethod
    def get_instrument(cls):
        return Guitarist.instrument


class Guitarist(Musician) :
    
    instrument = 'guitar'
    def __init__(self,name="Mo'ath"):
        self.name = name
        
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
       return f'Guitarist instance. Name = {self.name}'

   
    



class Drummer :
   
    def __init__(self,name="Mo'ath"):
        self.name = name
        
    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
       return f'Drummer instance. Name = {self.name}'


class Bassist :
    def __init__(self,x="Mo'ath"):
        self.name = x

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
       return f'Bassist instance. Name = {self.name}'

class Band :
   def __init__(self,name,arr):
       self.name = name



if __name__ == '__main__':

 moath = Guitarist("Mo'ath")
#  print(str(moath))
#  print(repr(moath))
#  print(moath.name)
# print(moath.instrument)
print(Guitarist.instrument)
