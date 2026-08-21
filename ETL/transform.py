import pandas as pd

def transform_product(product_df):
    df = product_df.copy()

    df = df.rename(columns = {
        'id' : 'prod_id',
        'title' : 'prod_title',
        'price' : 'prod_price',
        'category' : 'prod_category',
        'description' : 'description',
        'image' : 'prod_img'
    })

    df = df[[
        'prod_id', 'prod_title', 'prod_price', 'prod_category', 'description', 'prod_img'
    ]]

    df['prod_price'] = df['prod_price'].astype(float)

    return df

def transform_users(user_df):
    df = user_df.copy()

    df['first_name'] = df['name'].apply(lambda x: x['firstname'])
    df['last_name'] = df['name'].apply(lambda x: x['lastname'])

    df['street'] = df['address'].apply(lambda x: x['street'])
    df['city'] = df['address'].apply(lambda x: x['city'])
    df['zipcode'] = df['address'].apply(lambda x: x['zipcode'])

    df = df.rename(columns = {
        'id' : 'user_id',
        'email' : 'user_email',
        'username' : 'username'
    })

    df = df[[
        'user_id', 'user_email', 'username', 'first_name', 'last_name',
        'street', 'city', 'zipcode'
    ]]

    return df