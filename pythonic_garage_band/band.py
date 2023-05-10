
class Musician :
    pass


class Guitarist :

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
   pass

class Band :
   pass



if __name__ == '__main__':

 moath = Guitarist("Mo'ath")
#  print(repr(moath))
#  print(moath.name)
#  print(str(moath))
