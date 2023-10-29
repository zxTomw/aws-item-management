import requests
import json

apiKey = 'lWdRhYFnVN6eqpMQjpSnx9flpFbFfG0M5suxRwTb'

URL = 'https://s4c5y7evfl.execute-api.us-east-2.amazonaws.com/deploy/itemmanagement/'

prompt = "commands: g for get, gid for get with id, p for post (add new item), q for quit."
i = None
print(prompt)
while(i != "q"):
    i = input("command: ")
    response = None
    if i == "gid":
        id = input("id: ")
        response = json.loads(requests.get(URL+id, headers={"x-api-key": apiKey}).text)
        if response == None:
            print("item does not exist")
            continue
        print("-------------")
        print("ID: " + response['ID'])
        print("name: " + response['name'])
        print("description: " + response['description'])
        print("-------------")
        
    elif i == "g":
        response = json.loads(requests.get(URL).text)
        print("All items:\n-------------")
        for i in response:
            print("ID: " + i['ID'])
            print("name: " + i['name'])
            print("description: " + i['description'])
            print("-------------")
    elif i == 'p':
        item_id = input("ID: ")
        item_name = input("name: ")
        item_description = input("description: ")
        response = json.loads(requests.post(URL, headers={"x-api-key": apiKey}, 
        json={'ID':item_id, 'name': item_name, 'description': item_description}).text)
    else:
        print(prompt)
        continue
    print("Response: "+str(response))