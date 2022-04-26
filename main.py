import os
import argparse

print('Started')

def CreateGraph(data):
    pass


if __name__ == "__main__":
    IN_FOLDER = 'in';
    INPUT_FILE = 'simulations.txt'
    _source_file = os.path.join( os.getcwd(), IN_FOLDER, INPUT_FILE);      

    try:
        # Create data array for all nodes in landscape
        with open(_source_file, 'r') as _incidents:
            for entry in _incidents:
                print(entry)

    except Exception as err:
            print(err)

print('Completed')