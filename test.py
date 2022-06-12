import requests
BASE = "http://127.0.0.1:5000/"
USER_NAME = "duc"
data = [{"call_duration": 300000},
        {"call_duration": 150000},
        {"call_duration": 142003}]

for i in range(len(data)):
    response = requests.put(BASE+"mobie/"+USER_NAME+"/call", data[i])
    print(response.json())

response = requests.get(BASE+"mobie/"+USER_NAME +
                        "/billing")
print(response.json())
