from django.test import TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    page_title = "Home" 
    content = "In this site we ..."
    menu = {"Developers":"developers","Tech Field":"tech_field","Home":""}

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
           
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        
    def test_view_menu(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        print("response.context",response.context)
        self.assertTrue(response.context['menu'],self.menu)

    def test_view_content(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        print("response.context",response.context)
        self.assertTrue(response.context['content'],self.content)


    def test_view_page_title(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        print("response.context",response.context)
        self.assertTrue(response.context['page_title'],self.page_title)