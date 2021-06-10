from abc import abstractmethod

class Band():

    all_bands = []
    instances = []
    solo_list = []


    def __init__(self,name,members):
        self.name = name 
        self.members=members
        Band.all_bands.append(self)
        Band.instances.append(self)


    def play_solos(self):
        for i, member in enumerate(self.members):
            if member.get_instrument() == 'guitar':
                Band.solo_list.append("face melting guitar solo")
            elif member.get_instrument() == 'bass':
                Band.solo_list.append("bom bom buh bom")
            elif member.get_instrument() == 'drums':
                Band.solo_list.append("rattle boom crash")
           
        return Band.solo_list


    def __str__(self):
        return f"{self.name}"


    def __repr__(self):
        return f"{self.name}"


    @classmethod
    def to_list(cls) :
        return cls.all_bands


class Musician():

    def __init__(self, name):
        self.name = name
       

    @abstractmethod
    def __str__(self):
        pass


    @abstractmethod
    def __repr__(self):
        pass 
    
    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass 



class Guitarist(Musician):


    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}" 

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician): 

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return "rattle boom crash"


class  Bassist(Musician):
   def __str__(self):
        return f"My name is {self.name} and I play bass"

   def __repr__(self):
        return f"Bassist instance. Name = {self.name}" 

   def get_instrument(self):
        return 'bass'

   def play_solo(self):
        return "bom bom buh bom"



