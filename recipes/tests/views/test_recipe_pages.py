# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from django.test import TestCase
from django.urls import reverse

from recipes.models.recipe import Recipe


class TestRecipeDetailView(TestCase):
    def setUp(self):
        r = Recipe()
        r.save()

    def test_url_path(self):
        """
        Test the path directly
        """
        response = self.client.get('/planner/recipes/1/')
        self.assertEqual(response.status_code, 200)

    def test_reversed_path(self):
        """
        Rely on the url reversing
        """
        url_path = reverse('planner:recipes-detail', args='1')
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)

    def test_html_response(self):
        response = self.client.get('/planner/recipes/1/')
        html_response_content = response.content
        soup = BeautifulSoup(html_response_content, 'html.parser')
        recipe_containers = soup.find_all(id='selected_recipe_container')
        self.assertEqual(1, len(recipe_containers))


class TestRecipeListView(TestCase):
    def test_url_path(self):
        """
        Test the path directly
        """
        response = self.client.get('/planner/recipes/')
        self.assertEqual(response.status_code, 200)

    def test_reversed_path(self):
        """
        Rely on the url reversing
        """
        url_path = reverse('planner:recipes-list')
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
