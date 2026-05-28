from utils.table import Table 
import random


new_collegues = ["Anna", "Dan", "Gaetan", "Guillermo", "Gunay", 
                         "Hiba", "Hussein", "Ibrahim", "Ibtihel", "Imad", "Iness", 
                         "Irene","Jeong", "Mahalakshmi", "Max", "Neha", "Siegried", 
                         "Sitara", "Sooyoung", "Stephane", "Thi", "Uzair", "Victor", "Vanessa"]

class Openspace:
    def __init__(self, number_of_tables = 6):
        self.nbr_tables = number_of_tables
        self.tables = []
        
        for t in range(number_of_tables):
            self.tables.append(Table())
            
    def __str__(self):
        return 'MyClass = Openspace (nombre de table =' + str(self.nbr_tables) + ' ,tables id =' + str(self.tables) + ')'
    
    def organize(self, names):
        random.shuffle(names)
        cpt = 0
        for t in self.tables:
            for s in t.seat:
                s.set_occupant(names[cpt])
                cpt += 1
                
    def display(self):
        cpt1 = 1
        for t in self.tables:
            print(f"table {cpt1} :")
            cpt1 += 1
            for s in t.seat:
                print(s.occupant)
      
    def store(self, filename):
        reaprtition_list = []
        cpt1 = 1
        for t in self.tables:
            reaprtition_list.append(f"Table {cpt1}:")
            cpt1 += 1
            for s in t.seat:
                reaprtition_list.append(f"{s.occupant}")
        
        with open(filename, "w") as file:
            file.write(str(reaprtition_list))
            
        
      
        
            
            
becode = Openspace()
becode.organize(new_collegues)
becode.display()
print(becode.__str__())
becode.store("test.txt")

                
            