import requests

test = requests.get('https://www.donneesquebec.ca/recherche/api/3/action/package_show?id=f170fecc-18db-44bc-b4fe-5b0b6d2c7297').json()
test = test['result']['resources']
for i in range(len(test)):
    print(test[i]['url'])
