import requests, json

search_name = input('Please input a search name: ')

# Make sure input returns the name I want
# print(search_name)


response = requests.get(url=f'https://api.github.com/search/users?q={search_name}')

# Make sure response returned a valid response
# print(response)

# First try at looking at response
# print(dir(response))

# Second try at looking at response. Returned a binary object
# print(response.content)

# Third try to look at resonse, this time using json. Object cam as one dictonary
# answers = json.loads(response.content)

# This returned a list of users and their info that we can work with
# answers = json.loads(response.content)
# print(answers['items'])

answers = json.loads(response.content)

if(len(answers['items'])  > 1):
    for user in answers['items']:
        print(user['login'])
else:
    raise 