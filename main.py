from utils.table import Table
from utils.table import Seat 
from utils.openspace import Openspace, new_collegues


def main():
    
    names = new_collegues
    output_filename = input('The name of the file you want to save the reppartition in: ')
    
    
    # create an OpenSpace()
    open_space = Openspace()

    # assign a colleague randomly to a table
    open_space.organize(names)
    
    open_space.add_someone("CLAUDEEEEE")

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

    
        
if __name__ == "__main__":
    main()

            