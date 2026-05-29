from utils.table import Table 
import random


new_collegues = ["Anna", "Dan", "Gaetan", "Guillermo", "Gunay", 
                         "Hiba", "Hussein", "Ibrahim", "Ibtihel", "Imad", "Iness", 
                         "Irene","Jeong", "Mahalakshmi", "Max", "Neha", "Siegried", 
                         "Sitara", "Sooyoung", "Stephane", "Thi", "Uzair", "Victor", "Vanessa"]

class Openspace:
    '''
    This is the Opensace class with 2 attributes:
    First attribute is the number of tables, in this case it will always be 6
    Second attribute is the ID's of the tables we created from the class Table in utils.table.py, 
    it is created with a loop so if we change the number of tables it will adapt
    '''
    
    def __init__(self, number_of_tables = 6):
        self.nbr_tables = number_of_tables
        self.tables = []
        
        for t in range(number_of_tables):
            self.tables.append(Table())
            
    def __str__(self):
        return 'MyClass = Openspace with ' + str(self.nbr_tables) +' tables ' 
    
    '''
    the method organize is used to assign randomly people to a chair and to a table
    we use the random.shuffle method so each time we call the meethod the list is shuffled
    we use a loops to assign the people to a chair, we go down the new random list with a counter 
    the first loop is for each table in the tables' list from the Openspace class attribute,
    the second loop is for each seats at the tables from the Table class attribute, and we use the
    method set_occupant that we created in the Seat class. The method assign a name to a chair
    '''
    
    def organize(self, names):
        random.shuffle(names)
        cpt = 0
        for t in self.tables:
            for s in t.seat:
                s.set_occupant(names[cpt])
                cpt += 1
    
    '''
    the display method show the names of the persons at a table
    we use a loops to display the people
    the first loop is for each table in the tables' list from the Openspace class attribute,
    the second loop is for each seats at the tables from the Table class attribute, and we print
    the occupant name with the occupant attribute from the Seat class
    '''
    
    def display(self):
        cpt1 = 1
        for t in self.tables:
            print(f"\ntable {cpt1} :") 
            cpt1 += 1
            for s in t.seat:
                print(s.occupant)
                
    '''
    the store method store the reppartition in a file
    The parameter filename is used to name the file in which we want to store the reppartition.
    we use the with open function with the parameter w cause we want to create a file if it doesn't exist or we want to overwrite the content.
    we use the same logic than in the siplay method but instead of using the print function we use the .write to write the information in the file
    '''
      
    def store(self, filename):
        with open(filename, "w") as file:
            cpt1 = 1
            for t in self.tables:
                if cpt1 == 1:
                    file.write(f"Table {cpt1}: ")
                    cpt1 += 1
                else:
                    file.write(f"\nTable {cpt1}: ")
                    cpt1 += 1
                for s in t.seat:
                    file.write(f" {s.occupant} ")
                        
                  
                
            
        
      