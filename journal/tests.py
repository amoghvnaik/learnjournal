from django.test import TestCase
from .models import Resources
from django.urls import reverse

class TestDatabase(TestCase):

    def test_resource(self):
        
        #create resource
        resource1 = Resources(title="Gatling Cheat Sheet", url="https://gatling.io/docs/current/cheat-sheet/#simulation-configuration", software="Gatling", notes="Very helpful")
        resource1.save()
        self.assertEqual(Resources.objects.count(), 1)
        
        #update resource
        resource1.notes = "Extremely helpful"
        resource1.save()
        self.assertEqual(Resources.objects.filter(title='Gatling Cheat Sheet').first().notes, "Extremely helpful")
        
        #delete resource
        resource1.delete()
        self.assertEqual(Resources.objects.count(), 0)

class TestViews(TestCase):

    def test_home_view(self):
        response = self.client.get(reverse('journal:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No resources are available.") 

    def test_form_view(self):
        response = self.client.get(reverse('journal:form'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Submit")   
