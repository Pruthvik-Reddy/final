from django.conf.urls import url
from first_app import views

urlpatterns=[
        url(r'^book_appointments/',views.book,name='book'),
        url(r'^show_appointments/',views.showapp,name='showapp'),
        url(r'^slot_book/',views.slotapp,name='slotapp'),
        url(r'^booked/',views.bookapp,name='bookapp'),
        url(r'^yourappointments/',views.showappmnts,name='showappmnts'),

        url(r'^$',views.index,name='index'),


]