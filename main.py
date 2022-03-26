import requests
from pprint import pprint


class Superhero():

    API = "https://superheroapi.com/api/"

    def __init__(self, token: str):
        self.token = token
    def get_iq(self, name):
        url = self.API + self.token + "/search/" + name
        resp = requests.get(url)
        return int(resp.json()['results'][0]['powerstats']['intelligence'])

    def get_max_iq(self, heroes):
        max_iq = 0
        max_name = ''
        for hero in heroes:
            iq = self.get_iq(hero)
            if iq > max_iq:
                max_iq = iq
                max_name = hero
        print(f"Самый умный {max_name} интеллект = {max_iq}")


class YaUploader:
    host = 'https://cloud-api.yandex.net'
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, file_path: str):
        url = self.get_upload_url(file_path)
        if url != "":
            resp = requests.put(url, headers=self.get_headers(),  data=open(file_path, 'rb'))
            resp.raise_for_status()
            if result.status_code == 201:
                return f"Файл {path_to_file} загружен"
            else:
                return f"Файл не загружен"
        else:
            return "Не удалось получить URL для загрузки"

    def get_upload_url(self, file_path: str):
        method = '/v1/disk/resources/upload'
        url = self.host + method
        params = {"path": file_path, "overwrite": "true"}

        myhref = ""
        try:
            resp = requests.get(url, headers=self.get_headers(), params=params)
            myhref = resp.json()['href']
        finally:
            return myhref

if __name__ == '__main__':
    # Задача №1 Кто самый умный супергерой?
    heroes = ["Hulk", "Captain America", "Thanos"]
    TOKEN = '2619421814940190'
    Superhero(TOKEN).get_max_iq(heroes)

    # Задача №2  Яндекс.Диск
    path_to_file = "qfile.txt"
    token = 'секрет'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)


