class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        self.owner=self.own(owner)
        self.pet_type=self.validator(pet_type)
    
    def validator(self,pet):
        if pet not in Pet.PET_TYPES:
            raise ValueError("pet type incorrect")
        else:
            Pet.all.append(self)
            return pet
    def own(self,owner):
        if isinstance(owner,Owner):
            owner.add_pet(self)
            return owner
        else:
            Owner(owner).add_pet(self)
            return Owner(owner)
class Owner:
    def __init__(self,name):
        self.name=name
        self.all=[]
        
    def pets(self):
        return self.all
        
    def add_pet(self,pet):
        if isinstance(pet,Pet):
            pet.owner=self
            self.all.append(pet)
        else:
            raise TypeError("pet is not of instance Pet")
        
    def get_sorted_pets(self):
        return sorted(self.all, key=lambda k:k.name)
                        


owner = Owner("John")
pet1 = Pet("Fido", "dog", owner)
pet2 = Pet("Clifford", "dog", owner)
pet3 = Pet("Whiskers", "cat", owner)
pet4 = Pet("Jerry", "reptile", owner)

print(owner.get_sorted_pets())