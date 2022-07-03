from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class User:
    def __init__(self, id, age, gender, email):
        self.id = id
        self.age = age
        self.gender = gender
        self.email = email


users = [
    User(1, 12, "male", "mail1@gmail.com"),
    User(2, 22, "male", "mail2@gmail.com"),
    User(3, 42, "female", "mail3@gmail.com"),
    User(4, 12, "male", "mail4@gmail.com"),
    User(5, 52, "female", "mail5@gmail.com"),
    User(6, 42, "male", "mail6@gmail.com"),
    User(7, 62, "female", "mail7@gmail.com"),
    User(8, 82, "male", "mail8@gmail.com"),
]


def users_to_json(users):
    res = []
    for i in users:
        res.append(i.__dict__)
    return res


class GetUsersList(APIView):
    def get(self, request):
        id_param = request.GET.get("id", None)
        age_param = request.GET.get("age", None)
        gender_param = request.GET.get("gender", None)
        mail_param = request.GET.get("mail", None)

        res = []

        for i in users:
            if (not id_param or str(i.id) == id_param) \
                    and (not age_param or str(i.age) == age_param)\
                    and (not gender_param or str(i.gender) == gender_param)\
                    and (not mail_param or str(i.email) == mail_param):
                res.append(i)
        return Response(users_to_json(res))

