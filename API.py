from pprint import pprint
from urllib.parse import urlencode
import requests

TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

class User:
    respon = set()
    def __init__(self, token: str) -> None:
        self.token = token
        self.s = {}

    def response(self):
        response1 = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                "access_token": self.token,
                'order': 'name',
                "count": '5000',
                "v": 5.122,
            }
        )
        new_dict = response1.json()
        new_list = []
        for item in new_dict['response']['items']:
            new_list.append("vk.com/id"+ str(item))
        new = set(new_list)
        s = new
        return s

    def __repr__(self):
        return "{a}".format(a = (self.respon))


    def __add__(self, other):
        return list((self.response()).intersection(other.response()))



user1 = User(token = TOKEN)
user2 = User(token = TOKEN)
user3 = user1 + user2
print(user3)




