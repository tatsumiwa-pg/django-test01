"""
URL configuration for app_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URL全体設計
urlpatterns = [
    # 管理画面にアクセスするURLは以下
    path('admin/', admin.site.urls),
    # 本アプリにアクセスするURLは以下
    path('app_folder/', include('app_folder.urls')),
    # 何もURLを指定しない場合（app_config/views.pyで、自動的に「app_folder」にリダイレクトするよう設定済み）
    path('', views.index, name='index'),
]

# メディアファイル公開用のURL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)