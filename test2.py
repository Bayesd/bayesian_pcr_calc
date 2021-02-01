import requests
import bs4

page=requests.get("https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/antalet-testade-for-covid-19/")

soup = bs4.BeautifulSoup(page.text, "lxml")

table  = soup.find("table")
print(table)
"""
headers = [heading.text for heading in table.find_all("th")]
headers = headers[1:5]
print(headers)
table_rows = [row for row in table.find_all("tr")]

results = [ {headers[index]:cell.text for index,cell in enumerate(row.find_all("td"))} for row in table_rows]
print(results[1])

"""
