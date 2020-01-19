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

    print(users['items'][selection])