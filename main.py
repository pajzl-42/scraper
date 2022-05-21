"""
python projekt 3 - Engeto Python Akademie 2022

author: Jan Tásler
e-mail: jan.tasler@gmail.com
"""
from functions import *

def main():
    if incorrect_agruments():
        print("Incorrect initial arguments, the program won't initialize")
        quit()
    url = sys.argv[1]
    csv_name = sys.argv[2] + '.csv'

    data_scrape(url, csv_name)


if __name__ == "__main__":
    main()



