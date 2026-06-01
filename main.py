from utils.openspace import Openspace
from utils.file_utils import convert_file


def main():
    
    file_path = "./new_colleagues.txt" #path of the file that contain the names
    names = convert_file(file_path)   #converting the names name to a list
    output_filename = input('The name of the file you want to save the reppartition in: ')
    
    # create an OpenSpace()
    open_space = Openspace()

    # assign a colleague randomly to a table
    open_space.organize(names)
    
    # add someone to the openspace
    open_space.add_someone()

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

    
        
if __name__ == "__main__":
    main()

            