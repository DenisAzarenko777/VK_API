from pprint import pprint
from urllib.parse import urlencode
import requests

TOKEN = "10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c"

class User:
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
    def __str__(self):
        return self.s

    def __add__(self, other):
        if not isinstance(other,User):
            raise ArithmeticError("Провал")
        mutal_user_list = set()
        mutal_user_list = (self.s).union(other.s)
        return mutal_user_list

user1 = User(token = TOKEN)
u1 = user1.response()
user2 = User(token = TOKEN)
u2 = user2.response()
u3 = u1 & u2
print(u3)


