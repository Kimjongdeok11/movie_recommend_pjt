import requests
import pprint

movie_id = []

for n in range(1, 501):
    url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={n}"
    headers = {
        "accept": "application/json",
        "Authorization": ""
    }
    response = requests.get(url, headers=headers).json()
    for n in range(20):
        movie_id.append(response['results'][n]['id'])

print(movie_id)

    # pprint.pprint(response['results'][0]['id'])



