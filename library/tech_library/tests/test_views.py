from django.test import TestCase
from django.urls import reverse
from tech_library.models import Developer, Theme, Topic

class HomeViewTest(TestCase):
    page_title = "Home" 
    content = "In this site we ..."

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
           
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        
    def test_view_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['content'],self.content)


    def test_view_page_title(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_title'],self.page_title)


class DeveloperViewTest(TestCase):
    page_title = "Developers" 
    content = "List of developers:"
    
    @classmethod
    def setUpTestData(cls):

        dev1 = Developer.objects.create(name='test_dev1', description='test_dev1 description')
        dev2 = Developer.objects.create(name='test_dev2', description='test_dev2 description')
        dev3 = Developer.objects.create(name='test_dev3', description='test_dev3 description')
        dev4 = Developer.objects.create(name='test_dev4', description='test_dev4 description')


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/home/developers/')
        self.assertEqual(response.status_code, 200)
           
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('display_dev'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        

    def test_view_content(self):
        response = self.client.get(reverse('display_dev'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['content'],self.content)

    def test_view_developers(self):
        response = self.client.get(reverse('display_dev'))
        self.assertEqual(response.status_code, 200)

        self.assertTrue(len(response.context['developers']) == 4)


    def test_view_page_title(self):
        response = self.client.get(reverse('display_dev'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['page_title'],self.page_title)