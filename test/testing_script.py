import os
from pathlib import Path

def fileTest():
    with open("dada.txt", "r") as file:
        data = file.read()



def pathTest():
    entries = Path.cwd().parent
    print(os.listdir(entries))
if __name__ == "__main__":
	fileTest()
