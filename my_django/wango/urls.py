from venv import create
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('blog', views.index),
    path('blog/new', views.new),
    path('blog/json', views.jsonify),
    path('blog/create', views.create),
    path('blog/<int:my_val>', views.show),
    path('blog/<int:my_val>/edit', views.edit),
    path('blog/<int:my_val>/delete', views.desteoy),
    # path('admin/', admin.site.urls),
]
