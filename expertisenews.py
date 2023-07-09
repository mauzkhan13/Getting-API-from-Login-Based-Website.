""" Import the Necessary module"""

import requests
import pandas as pd


login_url = 'https://expertisenews.be/fr/login/'
api_url = 'https://expertisenews.be/fr/wp-admin/admin-ajax.php'

payload = {
    'username': 'abc@gmail.com',
    'password': '123456789'
}

# Perform the login request

with requests.session() as session:
    session.post(login_url, data=payload)

    cookies = {
    'wordpress_sec_3d0fd394de1f4ea36def9f6e9d5d683a': 'alexis%40alternativ.be%7C1690005766%7CbQ2o6uxej7KKCKyvAu4wcCOrE4xjLTk8q8wQ98Sdzmt%7C30da4b76a8bf24a1bda2f6ba2a95ce8b73b7c549868531199dc622ecbfe2865e',
    'pmpro_visit': '1',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wordpress_logged_in_3d0fd394de1f4ea36def9f6e9d5d683a': 'alexis%40alternativ.be%7C1690005766%7CbQ2o6uxej7KKCKyvAu4wcCOrE4xjLTk8q8wQ98Sdzmt%7C09a76e25ebe1e65a92e6e659b65879483202d13817928c1f2828f27017b1318d',
    }

    headers = {
        'authority': 'expertisenews.be',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9,de;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wordpress_sec_3d0fd394de1f4ea36def9f6e9d5d683a=alexis%40alternativ.be%7C1690005766%7CbQ2o6uxej7KKCKyvAu4wcCOrE4xjLTk8q8wQ98Sdzmt%7C30da4b76a8bf24a1bda2f6ba2a95ce8b73b7c549868531199dc622ecbfe2865e; pmpro_visit=1; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_3d0fd394de1f4ea36def9f6e9d5d683a=alexis%40alternativ.be%7C1690005766%7CbQ2o6uxej7KKCKyvAu4wcCOrE4xjLTk8q8wQ98Sdzmt%7C09a76e25ebe1e65a92e6e659b65879483202d13817928c1f2828f27017b1318d',
        'origin': 'https://expertisenews.be',
        'referer': 'https://expertisenews.be/fr/dbase/lettings/tu-offices/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'action': 'get_wdtable',
        'table_id': '5',
    }

    data = {
        'draw': '13',
        'columns[0][data]': '0',
        'columns[0][name]': 'address',
        'columns[0][searchable]': 'true',
        'columns[0][orderable]': 'true',
        'columns[0][search][value]': '',
        'columns[0][search][regex]': 'false',
        'columns[1][data]': '1',
        'columns[1][name]': 'region',
        'columns[1][searchable]': 'true',
        'columns[1][orderable]': 'true',
        'columns[1][search][value]': '',
        'columns[1][search][regex]': 'false',
        'columns[2][data]': '2',
        'columns[2][name]': 'published',
        'columns[2][searchable]': 'true',
        'columns[2][orderable]': 'true',
        'columns[2][search][value]': '|',
        'columns[2][search][regex]': 'false',
        'columns[3][data]': '3',
        'columns[3][name]': 'deal',
        'columns[3][searchable]': 'true',
        'columns[3][orderable]': 'true',
        'columns[3][search][value]': '',
        'columns[3][search][regex]': 'false',
        'columns[4][data]': '4',
        'columns[4][name]': 'area1',
        'columns[4][searchable]': 'true',
        'columns[4][orderable]': 'true',
        'columns[4][search][value]': '|',
        'columns[4][search][regex]': 'false',
        'columns[5][data]': '5',
        'columns[5][name]': 'rent1',
        'columns[5][searchable]': 'true',
        'columns[5][orderable]': 'true',
        'columns[5][search][value]': '',
        'columns[5][search][regex]': 'false',
        'columns[6][data]': '6',
        'columns[6][name]': 'companyto',
        'columns[6][searchable]': 'true',
        'columns[6][orderable]': 'true',
        'columns[6][search][value]': '',
        'columns[6][search][regex]': 'false',
        'columns[7][data]': '7',
        'columns[7][name]': 'agents',
        'columns[7][searchable]': 'true',
        'columns[7][orderable]': 'true',
        'columns[7][search][value]': '',
        'columns[7][search][regex]': 'false',
        'order[0][column]': '2',
        'order[0][dir]': 'desc',
        'start': '0',
        'length': '18449',
        'search[value]': '',
        'search[regex]': 'false',
        'wdtNonce': '06ebb4708c',
        'sRangeSeparator': '|',
    }
    response = session.post(
                api_url,
                params=params,
                cookies=cookies,
                headers=headers,
                data=data
            )
address = []
region = []
date = []
deal = []
area = []
rent = []
occupier = []
agents = []
info = []

if response.ok:
    api_data = response.json()
    results = api_data['data']
    
    address = []
    region = []
    date = []
    deal = []
    area = []
    rent = []
    occupier = []
    agents = []

    for result in results:
        address.append(result[0])
        region.append(result[1])
        date.append(result[2])
        deal.append(result[3])
        area.append(result[4] + ' m2')
        rent.append(result[5] + ' EUR') 
        occupier.append(result[6])
        agents.append(result[7])
else:
    print('API request failed with status code:', response.status_code)



df = pd.DataFrame(zip(address, region, date, deal, area, rent, occupier, agents), columns =["Address", "Region", "Date", 'Deal',"Area", "Rent","Occupier", "Agents"])

# If there are signs or words in the data frame, which are not supported in the Excel. This df_encoded will be ignored and save the data in Excel.
df_encoded = df.applymap(lambda x: x.encode('unicode_escape').decode('utf-8') if isinstance(x, str) else x)
df_encoded.to_excel("express.xlsx", index=False)
print(df_encoded)