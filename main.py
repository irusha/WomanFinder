import traceback

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Average_human_height_by_country"

countries: list = []
heights: list = []

try:
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find("tbody")
    tableRows = job_elements.find_all("tr")
    for tableRow in tableRows:
        tableDatas = tableRow.find_all("td")
        # print(tableDatas)
        c = 0
        country = ""
        for tableData in tableDatas:
            if c == 0:
                country = tableData.get_text().strip()
            elif c == 2:
                heightDataArray = tableData.get_text().split("cm")
                height = heightDataArray[0]
                try:
                    float_height = float(height)
                    countries.append(country)
                    heights.append(float_height/30.48)

                except:
                    pass
            elif c == 3:
                break

            c += 1

except Exception as err:
    print(Exception, err)
    print("Connection problem. Try again")

print("Got all the data")
height = 0.00
while True:
    try:
        height = float(input("Please enter the height in foot and decimals or else to exit the program:\n"))

    except:
        break

    incval = 0
    entry_counter = 0
    for currentHeight in heights:
        if currentHeight < height:
            print(countries[incval], currentHeight)
            entry_counter += 1
        incval += 1

    print("You have", entry_counter, "countries/ places to choose from")
