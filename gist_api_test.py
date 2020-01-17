import requests
import json

# Get the initalial information from GitHub
response = requests.get(url='https://api.github.com/users/pmfrank/gists')

# Some testing to see what info is needed and how to get it.
# print(dir(response))
# print(response.text)

# Convert the returned information into a list of dictonaries
gists = json.loads(response.text)

# Loop through the list to get each gist
for gist in gists:
    for key, value in gist['files'].items():
        filename = key
        
        # Get the indivual gists for eash set
        gistcontent = requests.get(url=value['raw_url'])
        
        # Again testing to see what info is needed
        # print(dir(gistcontent))
        
        # Print the code for the gist converting from byte to unicode
        print(gistcontent.content.decode())
        break # Breaks are just to keep it to the first gist for now
    break

response = requests.get(url='https://api.github.com/search/users?q=pmfrank')

users = json.loads(response.text)

print(users['items'])

for user in users['items']:
    print(user['id'])