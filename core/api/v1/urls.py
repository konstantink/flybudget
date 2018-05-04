# coding=utf-8

from django.conf.urls import url, include
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import CharField, Serializer
from rest_framework.status import HTTP_201_CREATED, HTTP_405_METHOD_NOT_ALLOWED
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from core.api.v1.views import main, user


__author__ = 'kkolesnikov'


class MessageSerializer(Serializer):
    message = CharField()


@api_view(['POST'])
def echo_view(request, *args, **kwargs):
    if request.method == 'POST':
        return Response(MessageSerializer(request.data).data, status=HTTP_201_CREATED)
    return Response(status=HTTP_405_METHOD_NOT_ALLOWED)


urlpatterns = (
    url(r'^categories', main.CategoryView.as_view()),

    url(r'^echo', echo_view),

    url(r'expenses', main.ExpensesView.as_view()),
    url(r'stats', main.StatisticsView.as_view()),

    # url(r'^auth/', include('core.api.v1.urls_auth'))
    url(r'^auth/', include('rest_framework.urls'), name='rest_framework'),
    url(r'^auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view()),
)