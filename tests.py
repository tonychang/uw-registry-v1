import unittest
from uwregistry.models import Service
from django.contrib.auth.models import User

class ServiceTestCase(unittest.TestCase):
	def setUp(self):
		user = User.objects.create_user(username='t', password='t',email='t@t.com');
		self.camper = Service.objects.create(name="Camper Service", nickname="camper-service", description="Description", owner=user, support_contact="cheiland@u.washington.edu", doc_url="http://www.washington.edu", root_url="http://www.washington.edu", status='1', date_submitted='2009-04-28', date_modified='2009-04-28');
		self.dancing = Service.objects.create(name="Dancing Service", nickname="dancing-service", description="Description", owner=user, support_contact="cheiland@u.washington.edu", doc_url="http://www.washington.edu", root_url="http://www.washington.edu", status='1', date_submitted='2009-04-28', date_modified='2009-04-28');

	def testEquals(self):
		self.assertEquals(self.camper.status, '1');
		self.assertEquals(self.dancing.status, '1');
