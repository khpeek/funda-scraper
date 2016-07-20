''' In lieu of geolocation, coordinates are looked up from the four numbers of the Dutch postal code only.'''
import pandas as pd

df = pd.read_json('amsterdam_sold_geo.json')
df.reset_index(drop = True)

# Coordinates of 4-number Dutch postal codes, obtained from https://github.com/bobdenotter/4pp
df_4pp = pd.read_csv('4pp.csv')

def get_4pp(postal_code):
    return postal_code.split()[0]

def get_latitude(postal_code_4pp):
    try:
        return df_4pp[df_4pp['postcode']==int(postal_code_4pp)].iloc[0]['latitude']
    except:
        return np.nan

def get_longitude(postal_code_4pp):
    try:
        return df_4pp[df_4pp['postcode']==int(postal_code_4pp)].iloc[0]['longitude']
    except:
        return np.nan

df['postal_code_4pp'] = df['postal_code'].apply(get_4pp)
df['latitude_4pp'] = df['postal_code_4pp'].apply(get_latitude)
df['longitude_4pp'] = df['postal_code_4pp'].apply(get_longitude)

df.to_json('amsterdam_sold_geo4pp.json')
