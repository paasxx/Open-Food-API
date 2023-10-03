import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
import json
from json import loads, dumps
import time
from datetime import datetime


## considerations

# status, imported_t, creator, created_t, last_modified_t are fields created for the API 
# imported_t id the time the request is made in the API
# created_t is the time data is inserted in the database
# last_modified_t is the time the data is updated
# product_name depende on "lc"
# purchase_places did not find reference in csv so i used manufactured_places
# ingredients_text depends on "lc""
# serving_quantity can be derived of "serving_size" or  use "packaging_1_quantity_per_unit" which is empty
# main_category i used "sources_fields:org-database-usda:fdc_category"
# image_url i used "link"
# url i used "link"


def read():
    data = pd.read_csv("export.csv", delimiter='\t', skip_blank_lines=True,  encoding='utf8') 
    return data


def clean_dataframe(data):

    data = data[[
    'code',
    'lc',
    'product_name_ar',
    'product_name_de',
    'product_name_dz',
    'product_name_en',
    'product_name_es',
    'product_name_fr',
    'product_name_it',
    'product_name_ko',
    'product_name_ms',
    'product_name_nb',
    'product_name_nl',
    'product_name_pl',
    'product_name_pt',
    'product_name_ro',
    'quantity',
    'brands',
    'categories',
    'labels',
    'manufacturing_places',
    'stores',
    'ingredients_text_da',
    'ingredients_text_de',
    'ingredients_text_en',
    'ingredients_text_es',
    'ingredients_text_fi',
    'ingredients_text_fr',
    'ingredients_text_it',
    'ingredients_text_ko',
    'ingredients_text_nb',
    'ingredients_text_nl',
    'ingredients_text_pl',
    'ingredients_text_pt',
    'ingredients_text_ro',
    'ingredients_text_sv',
    'traces',
    'serving_size',
    'packaging_1_quantity_per_unit',
    'off:nutriscore_score',
    'off:nutriscore_grade',
    'sources_fields:org-database-usda:fdc_category',
    'link'
    ]]

    data = data.replace(np.nan, None)

    def product_name(row): 
        
        try:
            return row['product_name_' + row['lc']]
        except:
            return None
        

    def ingredients_text(row): 
        
        try:
            return row['ingredients_text_' + row['lc']]
        except:
            return None
        
        
    data['product_name'] = data.apply(lambda row: product_name(row), axis=1)
    data['ingredients_text'] = data.apply(lambda row: ingredients_text(row), axis=1)

    data['nutriscore_score'] = data['off:nutriscore_score']
    data['nutriscore_grade'] = data['off:nutriscore_grade']
    data['main_category'] = data['sources_fields:org-database-usda:fdc_category']
    data['serving_quantity'] = data['packaging_1_quantity_per_unit']
    data['url'] = data['link']
    data['purchase_places'] = data['manufacturing_places']
    data['status'] = 'published'
    data['imported_t'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    data['creator'] = 'GeoByte-Pedro'
    data['created_t'] = int(time.time())
    data['last_modified_t'] = int(time.time())
    data['image_url'] = data['link']
    data['cities'] = None

    data = data[
        ['code',
        'status',
        'imported_t',
        'url',
        'creator',
        'created_t',
        'last_modified_t',
        'product_name',
        'quantity',
        'brands',
        'categories',
        'labels',
        'cities',
        'purchase_places',
        'stores',
        'ingredients_text',
        'traces',
        'serving_size',
        'serving_quantity',
        'nutriscore_score',
        'nutriscore_grade',
        'main_category',
        'image_url'
        ]
    ]


    data=data.dropna(subset=['product_name'])
    data=data.dropna(subset=['quantity'])
    data=data.dropna(subset=['brands'])
    data=data.dropna(subset=['labels'])

    data = data.reset_index(drop=True, inplace=False)

  

    return data



## now after cleaning we have 522 products


def create_json(data):

    response = []
    
    df = data
    json_data = df.to_json(orient = 'index', force_ascii=False)
    parsed = loads(json_data)
    # dump = dumps(parsed, indent=4)

    for key,value in parsed.items():
        block = { 
            "model": "djangoapp.Food",
            "pk": int(key)+1,
            "fields":value}
        response.append(block)
    

    return response
    
    
def save_json(response):

    response = json.dumps(response, indent=2, ensure_ascii=False)

    
    with open("data.json", "w",  encoding='utf-8') as outfile:
        outfile.write(response)


data = read()
data = clean_dataframe(data)

save_json(create_json(data))

