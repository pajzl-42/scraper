import os
import sys
import requests
from bs4 import BeautifulSoup as BS
import csv

def incorrect_agruments():
    if len(sys.argv) != 3:
        return True
    else:
        return False

def num_name_dict(url):
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
    for i in range(len(num_list)):
        num_name[num_list[i]] = name_list[i]
    return num_name

def data_scrape(url,csv_name):
    num_name_dict(url)
    numnuts = url[-4:]
    county = url[-16:-14].strip("=")
    num_name = num_name_dict(url)
    for number in num_name:
        url_area = "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj={}&xobec={}&xvyber={}".format(county,number,numnuts)
        site_area = requests.get(url_area)
        soup_area = BS(site_area.text, "html.parser")
        voters = soup_area.find("td",{"headers":"sa2"})
        envelopes = soup_area.find("td", {"headers":"sa3"})
        votes = soup_area.find("td", {"headers": "sa6"})
        parties = []
        for party in soup_area.find_all("td",{"class":"overflow_name"}):
            parties.append(party.string)

        result = [number, num_name[number], space_eraser(voters.string), space_eraser(envelopes.string), space_eraser(votes.string), parties]
        print(result)
        csv_write(csv_name,result)

def csv_write(name, data):
    header = ["Kód obce", "Název obce", "Počet voličů v seznamu", "Počet vydaných obálek", "Počet platých hlasů", "Kandidující strany"]
    if name in os.listdir():
        mode = "a"
        with open(name, mode) as f:
            writer = csv.writer(f)
            writer.writerow(data)
    else:
        mode = "w"
        with open(name, mode) as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)

def space_eraser(str):
    str = str.replace(u"\xa0", u"")

    return str



if __name__ == "__main__":
    print(dir())
    None