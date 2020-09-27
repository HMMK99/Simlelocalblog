from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

from .models import Posty

class BlogTests(TestCase):
	def setUp(self):
		self.user = get_user_model().objects.create_user(
			username = 'test',
			email = 'test@email.com',
			password = 'secret'
		)
		
		self.post = Posty.objects.create(
			title='good',
			body='goody',
			auther=self.user,
		)
		
	def test_string_representation(self):
		post = Posty(title='sample')
		self.assertEqual(str(post), post.title)
		
	def test_get_absolute_url(self):
		self.assertEqual(self.post.get_absolute_url(), '/posty/1/')
		
	def test_post_content(self):
		self.assertEqual(f'{self.post.title}', 'good')
		self.assertEqual(f'{self.post.auther}', 'test')
		self.assertEqual(f'{self.post.body}', 'goody')
		
	def test_post_list_view(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'goody')
		self.assertTemplateUsed(response, 'home.html')
		
	def test_post_detail_view(self):
		response = self.client.get('/posty/1/')
		no_response = self.client.get('/posty/10000/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(no_response.status_code, 404)
		self.assertContains(response, 'good')
		self.assertTemplateUsed(response, 'post_detail.html')

	def test_post_create_view(self):
		response = self.client.post(reverse('post_new'),{
			'title': 'New title',
			'body' : 'New body',
			'auther': self.user,
		})
		self.assertEqual(response.status_code,200)
		self.assertContains(response,'New title')
		self.assertContains(response, 'New body')
		
	def test_post_update_view(self):
		response = self.client.post(reverse('post_edit', args = '1'),{
			'title': 'Updated title',
			'body' : 'Updated body',
			'auther': self.user,
		})
		self.assertEqual(response.status_code,302)
		
	def test_post_delete_view(self):
		response = self.client.get(reverse('post_delete', args = '1'))
		self.assertEqual(response.status_code,200)
		
		
	

























