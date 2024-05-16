import requests
import pprint
# for n in range(1, 501):
url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={1}"
headers = {
    "accept": "application/json",
    "Authorization": 
}
response = requests.get(url, headers=headers).json()

pprint.pprint(response['results'])

def get_movies_from_api():
    pass
