#! /usr/local/bin/python3

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd



def parse_html_table(table):
    cnum = 0
    rnum = 0
    column_names = []

    for row in table.find_all('tr'):
        column_marker = 0
        tds = row.find_all('td')
        if len(tds) > 0:
            rnum += 1
            if cnum == 0:
                cnum = len(tds)

        ths = row.find_all('th')       
        if len(ths) > 0 and len(column_names) == 0:
            for th in ths:
                column_names.append(th.get_text())

    # check  Column Titles
    if len(column_names) > 0 and len(column_names) != cnum:
        raise Exception("Column titles do not match the number of columns")
        
    columns = column_names if len(column_names) > 0 else range(0, cnum)
    df = pd.DataFrame(columns = columns, index=range(0,rnum))
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0   
        columns = row.find_all('td')
        for column in columns:
            df.iat[row_marker,column_marker] = column.get_text()
            #print(row_marker, column_marker, df.iat[row_marker,column_marker])
            column_marker += 1
            #print(column)
        if len(columns) > 0:
            row_marker += 1
    return df

def get_html_page(url):
    page = urlopen(url)
    # parse the html code by beautiful soup and store in variable 
    #soup = BeautifulSoup(page, 'html.parser')

    #Parse as a string
    page = BeautifulSoup(page, 'lxml')
    return page

def get_table(order, soup):
    #table = soup.find_all('table')
    table = soup('table')[order]
    return table

def parse_time_table(tb):
    links = []
    for link in tb.find_all('a'):
        links.append(link.get('href'))
    return links    

def get_time(link):
    #gameArchives.jsp?user=ayabot003&year=2014&month=2    
    parts = link.split('&')
    yr = parts[-2].split('=')[-1]
    month = parts[-1].split('=')[-1]
    return(yr, month)

if __name__ == '__main__':
    #id = 'ayabot003'
    id = 'qwesz'
    url = "https://www.gokgs.com/gameArchives.jsp?user=%s" %(id)
    print(url)
    page = get_html_page(url)
    time_table = get_table(1, page)
    links = parse_time_table(time_table)
    print(len(links))
    df = pd.DataFrame()
    for link in links:
        yr, mon = get_time(link)
        dlk = "https://www.gokgs.com/%s" %(link)
        
        month_pg = get_html_page(dlk)       
        print('month page: ', type(month_pg)) 
        #month_tb = get_table(0, month_pg)
        #df_month = parse_html_table(month_tb)
        #print(yr, mon, dlk)
        #print(df_month)
        #df.append(df_month)
    #print("new: ",df)
