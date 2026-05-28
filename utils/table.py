class Seat:
    def __init__(self, occupant = "" , free = True ):
        self.free = free
        self.occupant = occupant
        
    def __str__(self):
        return 'MyClass = Seat (seat is free=' + str(self.free) + ' ,name of the occupant=' + str(self.occupant) + ')'
        
    def set_occupant(self,name):
        if self.free == True:
            self.occupant = name
            self.free = False
            
        else:
            print("the seat is taken")
    
    def remove_occupant(self):
        if self.free == False:
            self.occupant = ""
            self.free = True
        else: 
            print("Nobody is sitting")
        
    
    
            
class Table:
    def __init__(self,capacity = 4):
        self.capacity = capacity
        self.seat = []
        
        for i in range(capacity):
            self.seat.append(Seat())
    
    def __str__(self):
        return 'MyClass = Table (capacity of seats=' + str(self.capacity) + ' ,seat id=' + str(self.seat) + ')'
        
    def has_free_spot(self):
        for i in self.seat:
            if i.free == True:
                return True
            else:
                return False
    
    def assign_seat(self, name):
        for i in self.seat:
            if i.free == True:
                i.set_occupant(name)
                break
          
    
    def left_capacity(self):
        left_seats = 0
        for i in self.seat:
            if i.free == True:
                left_seats += 1
                
        return left_seats
                
     
