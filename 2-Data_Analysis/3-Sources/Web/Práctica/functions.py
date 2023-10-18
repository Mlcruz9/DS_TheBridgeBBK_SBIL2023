import hashlib
import datetime
import requests
import pandas as pd

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params

def peticion(pub_key, priv_key, name_start, offset = 0):
    offset = offset
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

    pub_key = '45eb7b336c41f4380b0cf4ac7139458e'
    priv_key = '82f732ba05300c8659948f06cf34d2feafcb1d1d'

    params = {'ts': timestamp,
            'apikey': pub_key, 
            'nameStartsWith': name_start,
            'hash': hash_params(timestamp,priv_key,pub_key),
            'limit': 100, 
            'offset': offset};

    url = 'http://gateway.marvel.com/v1/public/characters'

    res = requests.get(url,params=params)
    return res.json()

def character_df(res):
    dicc_characters = {'id': [], 'name': [], 'picture_url': []}
    for i in range(len(res['data']['results'])):
        id = res['data']['results'][i].get('id')
        name = res['data']['results'][i].get('name')
        path = res['data']['results'][i].get('thumbnail').get('path')
        extension = res['data']['results'][i].get('thumbnail').get('extension')
        url = path + "." + extension

        dicc_characters['id'].append(id)
        dicc_characters['name'].append(name)
        dicc_characters['picture_url'].append(url)
    
    df = pd.DataFrame(dicc_characters)
    return df