from django.shortcuts import render

# Create your views here.
from user_info.models import UserInfo
from user_info.serializers import UserInfoSerializer, UserInfoPutSerializer

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework import generics
from rest_framework.views import APIView


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):

    queryset = UserInfo.objects.all()
    Permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'get':
            return UserInfoSerializer
        if self.action == 'put':
            return UserInfoPutSerializer
        return UserInfoSerializer

    def get(self, request, pk,  *args, **kwargs):
        try:
            user = UserInfo.objects.get(userid=pk)
            serializer = UserInfoSerializer(user)
            return Response(serializer.data)
        except UserInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, *args, **kwargs):
        user = UserInfo.objects.get(userid=pk)
        serializer = UserInfoPutSerializer(user, data=request.data)

        if serializer.is_valid():
            print(serializer)
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreate(generics.CreateAPIView):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoPutSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserList(APIView):

    def get(self, request, *args, **kwargs):

            try:
                queryset = UserInfo.objects.values_list('userid',flat=True)

                return Response(queryset)

            except Exception as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)




