from abc import ABC , abstractmethod


    
class Musician(ABC) :
    '''
    This class is the parent class of guitarist,Drummer,Bassit classes ,
    it contain some common methods for all child classes
    '''
    def __init__(self,name="Mo'ath"):
        self.name = name
    
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    @abstractmethod
    def __repr__(self):
       pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician) :
    '''
    This class is used to contain all guitarest musicions with the name of each person
    and some propereties(methods) like their instrument and play solo
    '''

    # def __str__(self):
    #     return f'My name is {self.name} and I play guitar'

    def __repr__(self):
       return f'Guitarist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'guitar'
    
    def play_solo(self):
        return "face melting guitar solo"

   

class Drummer(Musician) :
    '''
    This class is used to contain all drummer musicions with the name of each person
    and some propereties(methods) like their instrument and play solo
    '''
   
    # def __str__(self):
    #     return f'My name is {self.name} and I play drums'

    def __repr__(self):
       return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'drums'
    
    def play_solo(self):
        return "rattle boom crash"



class Bassist(Musician) :
    '''
    This class is used to contain all Bassist musicions with the name of each person
    and some propereties(methods) like their instrument and play solo
    '''

    # def __str__(self):
    #     return f'My name is {self.name} and I play bass'

    def __repr__(self):
       return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(self):
        return 'bass'
    
    def play_solo(self):
        return "bom bom buh bom"

class Band :
    '''
    This class is used to contain mucisian bands names with the members for every band

    '''

    instances = []
    def __init__(self,name: str,arr=[]):
       self.name = name
       self.members = arr
       Band.instances.append(self)

    def __str__(self) -> str:
        return f"Hell our band name is {self.name}"
    
    def __repr__(self) -> str:
        return f"We consist of three type pf musicions"

    def play_solos(self):
        members_play_solo = [] 
        for member in self.members :
            members_play_solo.append(member.play_solo())
            
        return members_play_solo

    def to_list():
        return Band.instances 










if __name__ == '__main__':
 
 print('mmmm')
#  moath = Band("Mo'ath")
#  print(Band.members)
#  print(moath.get_instrument())
#  print(str(moath))
#  print(repr(moath))
#  print(moath.name)
# print(moath.instrument)
# print(Guitarist.instrument)
