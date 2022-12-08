from django.urls import path

from ORS import views

urlpatterns = [
    path('',views.index),

    path('auth/<page>/',views.auth),
    path('<page>/',views.actionID),
    path('<page>/<operation>/<int:id>',views.actionID),
]
