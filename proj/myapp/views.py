from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Person
import neomodel
import json

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.



@method_decorator(csrf_exempt, name='dispatch')
class AddPersonView(View):


	def post(self,request):

		json_data = json.loads(request.body.decode('utf-8'))
		try:
			person = Person(name=json_data['name'])
			person.save()
			return HttpResponse(person)
		except neomodel.exceptions.UniqueProperty :
			html = "<html><body> person named " + json_data['name'] +  " already exists</body></html>" 
			return HttpResponse(html)

@method_decorator(csrf_exempt, name='dispatch')
class AddRelationView(View):
	def post(self,request):
		json_data = json.loads(request.body.decode('utf-8'))

		try:
			Mentor = Person.nodes.get(name = json_data['Mentor'])
		except :
			html = "<html><body> person named " + json_data['Mentor'] +  " does not exist</body></html>" 
			return HttpResponse(html)

		try:
			Mentee = Person.nodes.get(name = json_data['Mentee'])
		except :
			html = "<html><body> person named " + json_data['Mentee'] +  " does not exist</body></html>" 
			return HttpResponse(html)
			

		Mentor.mentee.connect(Mentee)
		html = "<html><body>" + json_data['Mentor'] +  " has been added as a mentor to" + json_data['Mentee'] + " </body></html>" 

		return HttpResponse(html)

@method_decorator(csrf_exempt, name='dispatch')
class DisplayMenteesView(View):
	def post(self,request):
		json_data = json.loads(request.body.decode('utf-8'))
		
		try:
			Mentor = Person.nodes.get(name = json_data['Mentor'])
		except :
			html = "<html><body> person named " + json_data['Mentor'] +  " does not exist</body></html>" 
			return HttpResponse(html)

		node_list = Mentor.get_mentees()
		name_list = []
		for a in Mentor.get_mentees():
			name_list.append(a.__str__())
		list_as_json = json.dumps(name_list)
		return HttpResponse(list_as_json)

