import json
import requests
from bs4 import BeautifulSoup

def fetch_disease_info(url):
    full_url = "https://www.atlasdasaude.pt" + url
    response = requests.get(full_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    disease_div = soup.find('div', class_="node-doencas")

    disease_data = {}

    # date
    date_div = disease_div.find('div', class_="field-name-post-date")
    if date_div:
        disease_data["Date"] = date_div.div.div.text

    # content
    content_div = disease_div.find('div', class_="field-name-body")
    if content_div:
        content_info = {"Description": []}
        current_title = "Description"

        content_elem = content_div.find("div", class_="field-item even")

        for item in content_elem:
            if item.name == 'p' or item.name == 'div':
                content_info[current_title].append(item.text.replace(" ", " "))
            elif item.name == 'h2':
                current_title = item.text.replace(" ", "").title()
                content_info[current_title] = []
            elif item.name == 'ul':
                content_info[current_title].append([li.text for li in item.find_all('li')])
            elif item.name == 'h3':
                if len(content_info[current_title]) == 0:
                    content_info[current_title].append({item.text.replace(" ", ""): item.a["href"]})
                else:
                    content_info[current_title][0] = content_info[current_title][0] | {item.text.replace(" ", ""): item.a["href"]}

        disease_data["Information"] = content_info

    # source
    source_div = disease_div.find('div', class_="field-name-field-fonte")
    if source_div:
        disease_data["Source"] = source_div.find('div', class_="field-item even").text
    # website
    website_div = disease_div.find('div', class_="field-name-field-site")
    if website_div:
        disease_data["Website"] = website_div.find('div', class_="field-item even").text

    # note
    note_div = disease_div.find('div', class_="field-name-field-nota")
    if note_div:
        note = note_div.find("div", class_= "field-item even").text
        disease_data["Note"] = note

    return {'Url': full_url, "Content": disease_data}

def diseases_by_letter(letter):
    response = requests.get("https://www.atlasdasaude.pt/doencasAaZ/" + letter)
    print(f'URL: {response.url}')

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    diseases = {}

    for elem in soup.find_all('div', class_="views-row"):
        name = elem.div.h3.a.text.strip()
        disease_url = elem.div.h3.a['href']
        disease_info = fetch_disease_info(disease_url)

        desc_div = elem.find("div", class_="views-field-body")
        description = desc_div.div.text
        disease_info["Summary"] = description.strip().replace(" ", " ")
        diseases[name] = disease_info

    return diseases

all_diseases = {}

for a in range(ord("a"), ord("z") + 1):
    letter = chr(a)
    all_diseases = all_diseases | diseases_by_letter(letter)

with open("diseases.json", "w", encoding="utf-8") as file:
    json.dump(all_diseases, file, indent=4, ensure_ascii=False)
