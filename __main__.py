import pandas as pd
from urllib.parse import urlparse


def write_html_tables_to_separate_csv_files(url):
    tables = extract_tables_from_webpage(url)
    filename = generate_filename_from_url(url)
    range_of_tables = range(len(tables))
    for x_table in range_of_tables:
        tables[x_table].to_csv(
            "./data/{}-{}.csv".format(
                filename, (x_table + 1)
                ),
            index = False
        )


def extract_tables_from_webpage(url):
    return pd.read_html(url, header=0)

def generate_filename_from_url(url):
    file_title = get_file_title_from_domain(url)
    file_subtitle = get_file_subtitle_from_last_path_component(url)
    return file_title + '-'+ file_subtitle

def get_file_title_from_domain(url):
    domain_labels = make_list_of_domain_labels(url)
    if domain_labels[0] != "www":
        return domain_labels[0]
    else:
        return domain_labels[1]

def get_file_subtitle_from_last_path_component(url):
    path_list = make_list_of_path_components(url)
    if len(path_list) == 0:
        return "main"
    elif path_list[-1] != '':
        return path_list[-1]
    else:
        return path_list[-2]


def make_list_of_domain_labels(url):
    return urlparse(url).netloc.split(".")

def make_list_of_path_components(url):
    return urlparse(url).path.split("/")

url = "https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/antalet-testade-for-covid-19/"
write_html_tables_to_separate_csv_files(url)
