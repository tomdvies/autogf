import requests
id=69881
with open("creds.txt") as f:
    email,passwd = f.read().split("\n")
token = requests.post("https://console.gitfront.io/api/signin", json ={"email":email, "password":passwd}).cookies
print(requests.get("https://console.gitfront.io/api/build",cookies=token,json={"id":id}).content)