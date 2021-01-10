import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):

        file_path = input('Введите путь до файла: ')

        if ':' in file_path:
            url_path = file_path[3:]
        else:
            url_path = file_path

        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', headers={'Authorization': self.token}, params={'path': url_path})
        upload_url = response.json()['href']


        with open (file_path, 'rb') as f:
            resp = requests.put(upload_url, files={'file': f})

        print('загружено')
        return 'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    uploader = YaUploader('-')
    result = uploader.upload('file_path')