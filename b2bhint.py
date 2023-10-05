from bs4 import BeautifulSoup
import requests
import threading
import tkinter as tk
from tkinter import ttk
import sv_ttk
import csv
import datetime
import json
import threading
from multiprocessing import freeze_support
from urllib.parse import urlparse
import pandas as pd 
import numpy as np
import re

def scrape_link():
    contents = []
    for i in range(1, 1001):
        response=requests.get(f'https://b2bhint.com/en/search?country=16&q=&type=companies&activities=&page={i}')
        soup = BeautifulSoup(response.text, "lxml")
        company_list = soup.find('div', class_='Search_list__U_8b1').find_all('div', class_='SearchItem_item__ab1gL')
        for row in company_list:
            content = {}
            content['company'] = row.find('a').text
            content['enterprise_number'] = row.find('p').text
            # sub_url = 'https://b2bhint.com' + row.find('a').get('href')
            # response1=requests.get(sub_url)
            # soup1 = BeautifulSoup(response1.text, "lxml")
            contents.append(content)
    print(contents)
    current_datetime = datetime.datetime.now()
    csv_file = f"B2BHint Scrape - {current_datetime.strftime('%d-%m-%Y %H_%M_%S')}.csv"

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["company", "enterprise_number"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for csv_row in contents:
            writer.writerow(csv_row)

def main():
    startbot.config(state='enabled', text='Processing...')
    scrape_link()
    startbot.config(state='disabled', text='Completed!')
    

if __name__ == "__main__":
    global startbot
    global contents
    freeze_support()
    app = tk.Tk()
    app.title(f'B2Bhint Scraper')
    app.minsize(400, 300)
    app.maxsize(400, 300)
    ttk.Frame(app, height=30).pack()
    title = tk.Label(app, text='B2Bhint Scraper', font=("Calibri", 24, "bold"))
    title.pack(padx=10, pady=30, fill=tk.X)
    startbot = ttk.Button(app, text='Start Bot', style='Accent.TButton', width=15,
                          command=lambda:threading.Thread(target=main).start())
    startbot.pack(pady=40)
    sv_ttk.set_theme('dark')
    app.mainloop()

