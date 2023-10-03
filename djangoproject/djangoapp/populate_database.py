
from datetime import date, timedelta, datetime


## Auxiliary function to populate database from a dataframe

def populateTableByModel(data, model):
    df = data
    for i in df.index:
        vals = [df.at[i, col] for col in list(df.columns)]

        ##Change to use save function
        model.crypto_objects.all_data().create(
           
        # date=datetime.strftime(vals[0], "%Y-%m-%d"),
            code = vals[0],
            status = vals[1],
            imported_t = vals[2],
            url = vals[3],
            creator = vals[4],
            created_t = vals[5],
            last_modified_t = vals[6],
            product_name = vals[7],
            quantity = vals[8],
            brands = vals[9],
            categories = vals[10],
            labels = vals[11],
            cities = vals[12],
            purchase_places = vals[13],
            stores = vals[14],
            ingredients_text = vals[15],
            traces = vals[16],
            serving_size = vals[17],
            serving_quantity = vals[18],
            nutriscore_score = vals[19],
            nutriscore_grade = vals[20],
            main_category = vals[21],
            image_url = vals[22] 
        )


# data = read()
# data = clean_dataframe(data)

# populateTableByModel(data,Food)
# print('ok')
