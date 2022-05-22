"""
python projekt 3 - Engeto Python Akademie 2022

author: Jan Tásler
e-mail: jan.tasler@gmail.com
"""
from functions import *

def main():
    url = arguments_load()[0]
    csv_name = arguments_load()[1]
    data_scrape(url, csv_name)
    print("All done!")

if __name__ == "__main__":
    main()



