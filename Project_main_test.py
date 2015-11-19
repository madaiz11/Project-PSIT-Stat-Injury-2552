"""Test Project."""
import csv
def getdata(file):
    """Return table of data from file.txt inform list."""
    data = csv.reader(open(file+'.txt'))
    table = [row for row in data]
    return table

def mainprogram():
    """Show graph in Circle form by use data from maincause.txt.
    If you want to see detail of each data, you can choose by input number.
    choosen number : 1 = """
    data = getdata('maincause')
    print(data)
    choose = input()
    if choose == "2":
        data_new = getdata('anothercause')
        print(data_new)

mainprogram()
