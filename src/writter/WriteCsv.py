import csv

import requests
from bs4 import BeautifulSoup


class WriteCsv:

    # Write company name and url in csv file
    def write_company(self):
        with open('output.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            response = requests.get(self.driver.current_url, timeout=50)
            soup = BeautifulSoup(response.content, 'html.parser')
            for each_div in soup.find_all('div', {"class": "data-row-top"}):
                try:
                    company = each_div.find('a')
                    writer.writerow([company.text.strip(), company['href']])
                except AttributeError:
                    print('All the companies are scraped')


    # Write drug name, generic_name, drug_strength, drug_type in csv file
    def write_drugs(self):
        with open('drugs.csv', 'a') as drug_file:
            writer = csv.writer(drug_file)
            response = requests.get(self.driver.current_url, timeout=300)
            soup = BeautifulSoup(response.content, 'html.parser')
            process = 0
            for each_div in soup.find_all('div', {"class": "data-row"}):
                process += 1
                drug = each_div.find('div', {'class': 'data-row-top'}).find(text=True).strip()
                drug_type = each_div.find('span', {'class': 'inline-dosage-form'}).text.strip()
                drug_strength = each_div.find('span', {'class': 'grey-ligten'}).text.strip()
                generic_name = each_div.find_all('div', {'class': 'col-xs-12'})[2].text.strip()
                
                try:
                    unit_price = each_div.find('div', {'class': 'package-container'})
                    unit_price2 = unit_price.find('span', {'class': 'package-pricing'}).text.replace('Unit Price :', '').split()[1]

                except AttributeError:
                    unit_price2 = 'N/A'
                writer.writerow([drug, drug_type, drug_strength, generic_name, unit_price2])

            print(f'processed {process} drugs, getting next page')
