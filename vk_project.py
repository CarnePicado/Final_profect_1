import requests


VK_USER_ID = 151227453
with open('/home/carnepicado/Desktop/NetologyHomeWork/Work_with_json/FinalProject/token.txt', 'r') as file_object:
    token_vk = file_object.read().strip()

class VK_photo_save:
    
    def __init__(self, token_vk, version):
        self.params = {
            'access_token': token_vk,
            'v': version
        }

    def get_photo_data(self, owner_id=VK_USER_ID):
        params={'access_token': token_vk,
            'owner_id': owner_id,
            'album_id': 'profile',
            'rev': 0,
            'extended': 1,
            'v': '5.131'
            }
        req = requests.get('https://api.vk.com/method/photos.get', params).json()
        res = req['response']['items']
        return res
    def get_photo():
        data = vk.get_photo_data()
        photo_params = {'like_count': 0, 'filename': '', 'comments_count': 0}
        for d in data['response']['items']:
            photo_params['like_count'] == d['likes']['count']
            file_url = d['sizes']['url']
            photo_params['filename'] = file_url.split('/')[-1]
            photo_params['comments_count'] == d['comments']['count']
            if photo_params['like_count'] < d['likes']['count']:
                if photo_params['like_count'] == d['likes']['count']:
                    if d['comments']['count'] > photo_params['comments_count']:
                        photo_params['comments_count'] == d['comments']['count']

        url = requests.get(file_url)
        with open(photo_params['filename'], 'wb') as file:
            file.write(url.content)

            

vk = VK_photo_save(token_vk, '5.131')
vk.get_photo_data()

with open('/home/carnepicado/Desktop/NetologyHomeWork/Work_with_json/FinalProject/token.txt', 'r') as file_object:
    token_ya = file_object.read().strip()

class YaDisk:
    
    def __init__(self, token_ya):
        self.token = token_ya

    def get_headers(self):
        return {
            'Content-Type': 'application/json'
            'Authorization': 'OAuth {self.token}'
            }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()
    
    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


ya = YaDisk(token_ya)
ya.upload_file_to_disk('Lisk/photo.jpg', 'photo.jpg')

