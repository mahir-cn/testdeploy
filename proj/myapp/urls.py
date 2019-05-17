from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^api/add_person',views.AddPersonView.as_view(),name = 'add_person_view'),
	url(r'^api/add_relation',views.AddRelationView.as_view(),name = 'add_relation_view'),
	url(r'^api/display_mentees',views.DisplayMenteesView.as_view(),name = 'show_view'),

]