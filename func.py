FILE_PATH="../test/sf.txt"


def get_todos(path=FILE_PATH):
    """ read the file and return list of item
    in todos"""
    
    with open(path, "r") as file_loc :
        todos_loc = file_loc.readlines()
    return todos_loc


def write_todos(arg_todos , path=FILE_PATH):
    """writhe the to_items in the file"""
    with open(path, "w") as file_local:
        file_local.writelines(arg_todos)

