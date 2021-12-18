"""SimpleDRFExample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.db import router
from blog.views import method_article_list, \
                    method_article_detail, \
                    method_api_view_article_list, \
                    method_api_view_article_detail, \
                    ClassAPIView_Article, \
                    ClassAPIView_ArticleDetails, \
                    GenericAPIView_Article, \
                    ViewSet_Article, \
                    GenericViewSet_Article, \
                    ModelViewSet_Article
                                        
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ViewSet_Article, basename='article')

# Generic ViewSet
# url : class/viewset/generic/
# url : class/viewset/generic/<int:pk>/
router.register('generic/article', GenericViewSet_Article, basename='generic_viewset_article')

# Model ViewSet
# url : class/viewset/model/
# url : class/viewset/model/<int:pk>/
router.register('model/article', ModelViewSet_Article, basename='model_viewset_article')

urlpatterns = [
    # Method
    path('method/article', method_article_list),
    path('method/detail/<int:pk>', method_article_detail),

    # Method API View
    path('method/apiview/article/', method_api_view_article_list),
    path('method/apiview/detail/<int:pk>', method_api_view_article_detail),

    # Class API View
    path('class/apiview/article/', ClassAPIView_Article.as_view()),
    path('class/apiview/detail/<int:id>/', ClassAPIView_ArticleDetails.as_view()),

    # Generic API View
    path('class/apiview/generic/article/', GenericAPIView_Article.as_view()),
    path('class/apiview/generic/detail/<int:id>', GenericAPIView_Article.as_view()),

    # ViewSet
    path('class/viewset/', include(router.urls)),
    path('class/viewset/<int:pk>/', include(router.urls)),

    # admin
    path('admin/', admin.site.urls),
]
