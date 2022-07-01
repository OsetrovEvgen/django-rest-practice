from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

users = [
    {
        "id": 1,
        "email": "anton.osetrov@gmail.com",
        "age": 22,
        "gender": "men",
        "profession": "IT developer",
    },
    {
        "id": 2,
        "email": "qwe.132@gmail.com",
        "age": 25,
        "gender": "woman",
        "profession": "nurse",
    },
    {
        "id": 3,
        "email": "sdfsdf@gmail.com",
        "age": 40,
        "gender": "men",
        "profession": "driver",
    },
    {
        "id": 4,
        "email": "123.qeasd23@gmail.com",
        "age": 32,
        "gender": "woman",
        "profession": "accountant",
    },
    {
        "id": 5,
        "email": "13qweer.qwe@gmail.com",
        "age": 17,
        "gender": "woman",
        "profession": "business woman",
    },
    {
        "id": 6,
        "email": "1456123@gmail.com",
        "age": 36,
        "gender": "men",
        "profession": "salesman",
    },
    {
        "id": 7,
        "email": "qweqweqwe.576@gmail.com",
        "age": 29,
        "gender": "woman",
        "profession": "unemployed",
    },
]

class ReqGet(APIView):
    def get(self, request, format=None):
        return Response({'req type': 'Get'})

    def post(self, request):
        return Response({'req type': 'Post'})


class UsersList(APIView):
    def get(self, request):
        def analyze_object(users):
            count = 0
            if isinstance(object, dict):
                for items in object:
                    count += analyze_object(object[items])

        return Response(request)

for i in users:
    if i['age'] == query:
