from hashlib import md5
from requests import get
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = '604b17cd8972bf03beb4c347d4c5b0f6'
    priv_key = '038cf69a169be005de2cb1c465f4e5ed092834a2'

    def hash_params(self):
        hash_md5=md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    
    def get_heroes(self):
        params = {'ts':self.timestamp, 'apikey':self.pub_key, 'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)

        data = results.json()
        print(data)
        print(data['status'])

    def get_gen1_pokemon_images(self):
        base_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"
        return [f"{base_url}{i}.png" for i in range(1, 152)]



restmarvel = RestMarvel()
restmarvel.get_heroes()
urls = restmarvel.get_gen1_pokemon_images()

for url in urls:
    print(url)
