import requests
import datetime as dt

# request.post --- gives data to external system
# request.put --- update data of external system
# request.delete --- deletes data of external system

USERNAME = "your username"
TOKEN = "your token"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "kaster",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "your id",
    "name": "Reading Graph",
    "unit": "unit",
    "type": "int",
    "color": "sora"
}

headers = {                     # here we're using header API, it isn't shown in the url and is harder to be leaked.
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{graph_endpoint}/{graph_params['id']}"

pixel_params = {
    "date": dt.datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many pages did you read today? ")
}


# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)
