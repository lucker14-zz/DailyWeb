from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from vids.models import Post

from . import views

urlpatterns = [
	url(r'^$', ListView.as_view(
											queryset=Post.objects.all().order_by("-date")[:25],
											template_name="vids/home.html")),
]