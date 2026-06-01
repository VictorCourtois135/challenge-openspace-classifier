def convert_file(file):
    '''
    A function that convert all the names in a document to a list
    '''
    
    with open(file, "r") as file_open:
        string_file = file_open.read()
        name_list = string_file.split()
      
    return name_list

