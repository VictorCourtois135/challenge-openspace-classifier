class Seat:
    '''
    The Seat class has 2 attributes when it is created
    the first one is occupant and it is set empty because the seat is available
    the second one is free and it is a boolaen that returns true if the seat is available, it is set to true because the seat is always empty when it is created
    '''
    
    def __init__(self, occupant = "" , free = True ):
        self.occupant = occupant
        self.free = free
        
        
    def __str__(self):
        return 'MyClass = Seat (seat is free=' + str(self.free) + ' ,name of the occupant=' + str(self.occupant) + ')'
    
    '''
    the set_occupant method is used to assign a name to a seat, it takes a name in parameter and it assigns this name to the seat
    First, it checks if the seat is free with the self.free attribute and if the seat is available it assigns the name to the seat and it change the self.free attribute to False
    If the seat is not free it prints the seat is taken
    '''
    
        
    def set_occupant(self,name):
        if self.free == True:
            self.occupant = name
            self.free = False
            
        else:
            print("the seat is taken")
            
    '''
    The remove_occupant method is used to remove the name of the seat's occupant and replace it with ""
    First it checks if the seat is occupied with the self.free attribute, then it changes the name to "" and after it changes the self.free to true 
    If the seat is free it prints Nobody is sitting
    '''
    
    
    def remove_occupant(self):
        if self.free == False:
            self.occupant = ""
            self.free = True
        else: 
            print("Nobody is sitting")
        
    
    
            
class Table:
    
    '''
    the Table class has 2 attributes, the first one is the seat's capacity for 1 table and the second one is the IDs of each seat created with the Seat class
    with a loop so if we change the number of seats it will adapt
    '''
    
    def __init__(self,capacity = 4):
        self.capacity = capacity
        self.seat = []
        
        for i in range(capacity):
            self.seat.append(Seat())
    
    def __str__(self):
        return 'MyClass = Table with a capacity of '+ str(self.capacity) +' seats' 
    
    '''
    the has_free_spot method is used to check if a sea is free at the table and it returns a boolaen
    With a loop we check each seat in the table with the self.seat attribute and if 
    a seat is free it returns true, we check the availability of the seat with the free attribute of Seat class
    '''
    
        
    def has_free_spot(self):
        for i in self.seat:
            if i.free == True:
                return True
            else:
                return False
     
            
    '''
    the assign_seat method is used to assign the seat to someone, we put the name of the person we want to assign the seat to in the parameter
    with a loop we check if the seat is free with the free attribute from the seat class, and if the seat is free we use the 
    set_occupant method from the seat class 
    '''
    
    
    def assign_seat(self, name):
        for i in self.seat:
            if i.free == True:
                i.set_occupant(name)
                break
          
    '''
    this method returns the number of seats available at the table.
    we create a variable left_seats and we set it up at 0, and with a loop we check if a seat is available with the free attribute from the seat class
    if the seat is free we do a +1 in the left_seats variable. We return the variable at the end
    '''
    
    def left_capacity(self):
        left_seats = 0
        for i in self.seat:
            if i.free == True:
                left_seats += 1
                
        return left_seats
                
     
