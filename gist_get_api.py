import requests
import json

user = input('Enter user name: ')

response = requests.get(url=f'https://api.github.com/search/users?q={user}')

users = json.loads(response.text)

if len(users) > 1:
    print('You have returned more than one user. Select one: ')
    for x, account in enumerate (users['items']):
        print(x + 1, account['login'])
    num = input()
    selection = int(num) - 1

    gists_api = users['items'][selection]['gists_url'].split('{')[0]

    gists_query = requests.get(url=gists_api)
    gists = json.loads(gists_query.text)

    if len(gists) > 1:
        print('You have returned more than one gist. Select one: ')
        for x, gist in enumerate(gists):
            for key, value in gist:
                print(key)
        # print('You have returned more than one gists. Select one: ')
        # for x, gist in enumerate (gists['id']):
        #     print(x+1, gist)