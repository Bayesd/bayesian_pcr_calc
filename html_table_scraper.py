import pandas as pd
from urllib.parse import urlparse

url = "https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/antalet-testade-for-covid-19/"

netloc_list = urlparse(url).netloc.split(".")
path_list = urlparse(url).path.split("/") 

name = ""
path = "index"

if netloc_list[0] == "www":
    name = netloc_list[1]
else:
    name = netloc_list[0]

if path_list[-1] == '':
    path = path_list[-2]

dfs= pd.read_html(url, header=0)

for i in range(len(dfs)):
    dfs[i].to_csv("{}-{}-{}.csv".format(name, path, i), index = False)
