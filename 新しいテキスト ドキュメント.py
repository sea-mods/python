import requests
from pprint import pprint
from os import getenv

API_URL = 'https://osu.ppy.sh/api/v2'
TOKEN_URL = 'https://osu.ppy.sh/oauth/token'

def get_token():
    data = {
        'client_id': getenv('16920'),
        'client_secret': getenv('LCNy3IXPoXRc9ezj3340s0LSCXBzZGxqEPdwozBO'),
        'grant_type': 'client_credentials',
        'scope': 'public'
    }

    response = requests.post(TOKEN_URL, data=data)

    return response.json().get('access_token')

def main():
    token = get_token()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    params = {
        'mode': 'osu',
        'limit': 5
    }

    response = requests.get(f'{API_URL}/users/25313316/scores/best', params=params, headers=headers)
    
    beatmapset_data = response.json()[0].get('beatmapset')

    pprint(beatmapset_data, indent=2)


if __name__ == '__main__':
    main()
