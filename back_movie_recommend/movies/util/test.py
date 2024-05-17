import requests
url = f"https://api.themoviedb.org/3/movie/popular?language=ko-KR&page={1}"
headers = {
    "accept": "application/json",
    "Authorization": ""
}
response = requests.get(url, headers=headers).json()
for n in range(20):
    print(response['results'][n]['id'])