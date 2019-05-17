from django.db import models
from django_neomodel import DjangoNode
from neomodel import StructuredNode, StringProperty, DateProperty,RelationshipTo,UniqueIdProperty

# Create your models here.
class Person(DjangoNode):
	uid  = UniqueIdProperty()
	name = StringProperty(unique_index = True)
	mentee = RelationshipTo('Person','is_mentor_of')
	
	def __str__(self):
		return 'Name : ' + self.name
	
	def get_mentees(self):
		results,columns = self.cypher('MATCH (a) WHERE id(a)={self} MATCH (a)-[]->(b) RETURN b')
		return [self.inflate(row[0]) for row in results]
