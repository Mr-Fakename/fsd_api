import json
import os

from bson import json_util
from pymongo import MongoClient
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .models import Setup
from .serializers import TokenSerializer, RegisterSerializer, SetupSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ObtainTokenView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenSerializer


class SetupView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Setup.objects.filter(user=self.request.user)

    serializer_class = SetupSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def mongo_call(request):
    try:
        username = os.getenv("MONGO_USERNAME")
        password = os.getenv("MONGO_PASSWORD")
        uri = os.getenv("MONGO_URI")
    except Exception as e:
        return Response({"error": f"Error loading environment variables: {e}"})

    connection_string = f"mongodb+srv://{username}:{password}@{uri}/?retryWrites=true"
    client = MongoClient(connection_string)
    db = client["main"]
    collections = db.list_collection_names()

    data = {}

    for collection in collections:
        data[collection] = []
        for doc in db[collection].find():
            data[collection].append(doc)

    data = json.loads(json_util.dumps(data))

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    # with open("data.json", "r") as f:
    #     data = json.load(f)

    return Response({"data": data})
