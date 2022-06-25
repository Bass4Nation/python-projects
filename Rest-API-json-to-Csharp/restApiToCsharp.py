from types import SimpleNamespace
import requests
# https://realpython.com/api-integration-in-python/
import json
import pprint

# Test api: https://pokeapi.co 
api_url = "https://pokeapi.co/api/v2/pokemon/ditto"

def jsonReader(api):
    response = requests.get(api)
    jsonData = response.json()
    jsonDataStr = str(response.json())

    # Pretty print
    # pprint.pprint(jsonData)

    for key in jsonData.keys():
        # print(key)
        print("--------------------------------------")
        print(jsonData[key])
        if jsonData[key].keys() in jsonData[key]:
            print("YES")
        # for item in jsonData[key]:
        #     print(item)

    # print(jsonData['abilities'])

    # parsed = json.loads(jsonData)

    # print(json.dumps(parsed)





jsonReader(api_url)
