import os
import sys
import requests
from bs4 import BeautifulSoup as BS
import csv
import time

def incorrect_agruments():
    if len(sys.argv) != 3:
        return True
    else:
        return False

def arguments_load():
    if incorrect_agruments():
        print("Incorrect initial arguments, the program won't initialize")
        quit()
    url = sys.argv[1]
    csv_name = sys.argv[2] + '.csv'
    arguments = [url, csv_name]
    return arguments

def dir_name_check(name):
    if name in os.listdir():
        print("ATTENTION")
        print("File with this name is in current directory and has data inside,"
              "the result data for this calucaltion will be appended.")
        for i in range(3,0,-1):
            print("Starting in {}".format(i))
            time.sleep(1)

def num_name_dict(url,csv_name):
    dir_name_check(csv_name)
    site = requests.get(url)
    soup = BS(site.text, "html.parser")
    num_list = []
    name_list = []
    for i in soup.find_all("td"):
        if i.string == 'X' or i.string == "-":
            continue
        elif i.string.isnumeric():
            num_list.append(i.string)
        else:
            name_list.append(i.string)
    num_name = {}
    if (len(num_list)) < 1:
        print("Error with input arguments - incorrect form")
        csv_write(csv_name, "Error with input arguments - incorrect form")
        return TypeError
    else:
        for i in range(len(num_list)):
            num_name[num_list[i]] = name_list[i]
        return num_name


def data_scrape(url,csv_name):
    try:
        numnuts = url[-4:]
        county = url[-16:-14].strip("=")
        num_name = num_name_dict(url,csv_name)
        for number in num_name:
            url_area = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj={}&xobec={}&xvyber={}".format(county,number,numnuts)
            site_area = requests.get(url_area)
            soup_area = BS(site_area.text, "html.parser")
            voters = soup_area.find("td", {"headers":"sa2"})
            envelopes = soup_area.find("td", {"headers":"sa3"})
            votes = soup_area.find("td", {"headers": "sa6"})

            parties = []
            for party in soup_area.find_all("td",{"class":"overflow_name"}):
                parties.append(party.string)

            parties_votes = []
            for vote in soup_area.find_all("td",{"headers":"t1sa2 t1sb3"}):
                parties_votes.append(vote.string)
            for vote in soup_area.find_all("td", {"headers":"t2sa2 t2sb3"}):
                parties_votes.append(vote.string)

            header = ["Kód obce", "Název obce", "Počet voličů v seznamu", "Počet vydaných obálek","Počet platých hlasů"] + parties
            result = [number, num_name[number], space_eraser(voters.string), space_eraser(envelopes.string), space_eraser(votes.string)] + parties_votes

            print("Scraped for area: {}".format(num_name[number]))
            csv_write(csv_name,result,header)
    except TypeError:
        None
    except:
        print("Error with data extraction")
        csv_write(csv_name, "Error with data extraction","")

def csv_write(name, data, header):
    if name in os.listdir():
        mode = "a"
        with open(name, mode, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    else:
        mode = "w"
        with open(name, mode, newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)

def space_eraser(str):
    str = str.replace(u"\xa0", u"")
    return str

if __name__ == "__main__":
    print(dir())
    None