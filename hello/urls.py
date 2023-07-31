from django.urls import path, include
from .views import HelloAPI, JbnusApiMixins, JbnuApiMixins


'''
urlpatterns = [
    path("hello/", HelloAPI),
]
'''

urlpatterns = [
    path("hello/", HelloAPI, name="hello-api"),   
    path("mixin/jbnus", JbnusApiMixins.as_view()),
    path("mixin/jbnu/<int:id>/", JbnuApiMixins.as_view()),
]



