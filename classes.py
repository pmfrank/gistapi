import requests
import json

API_URL = 'https://api.github.com/'

class User():

    def __init__(self, user):
        __account = self.__user_search(user)
        if __account == False:
            return None
        self.login = __account['login']
        self.id = __account['id']
        self.gists_url = __account['gists_url'][:-10]
        self.gists_list = self.__load_gists(self.gists_url)


    def __user_search(self,user):
        response = requests.get(url=f'{API_URL}search/users?q={user}')

        users = json.loads(response.text)

        for account in users['items']:
            if account['login'] == user:
                return account
        return False

    def __load_gists(self, gists_url):
        response = requests.get(url=gists_url)
        gists = json.loads(response.text)

        gists_list = list()

        for gist in gists:
            gist_dict = dict()
            gist_dict['url'] = gist['url']
            gist_dict['id'] = gist['id']
            gist_dict['files'] = list()
            for key, value in gist['files'].items():
                file_dict = dict()
                file_dict['filename'] = value['filename']
                file_dict['language'] = value['language']
                file_dict['raw_url'] = value['raw_url']
                gist_dict['files'].append(file_dict)
            gists_list.append(gist_dict)

        return gists_list

user = User('pmfrank')
print(user.gists_list)