from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
import os
# Chapter 4
from django.contrib.staticfiles import finders
from rango.models import Page, Category
import populate_rango
import rango.test_utils as test_utils

from rango.decorators import chapter6

from rango.decorators import chapter7
from rango.forms import CategoryForm, PageForm

from django.template import loader
from django.conf import settings
from rango.decorators import chapter8
import os.path


def test_base_template_exists(self):
    # Check base.html exists inside template folder
    path_to_base = settings.TEMPLATE_DIR + '/rango/base.html'
    print(path_to_base)
    self.assertTrue(os.path.isfile(path_to_base))


def test_titles_displayed(self):
    # Create user and log in
    test_utils.create_user()
    self.client.login(username='testuser', password='test1234')

    # Create categories
    categories = test_utils.create_categories()

    # Access index and check the title displayed
    response = self.client.get(reverse('index'))
    self.assertIn('Rango -'.lower(), response.content.decode('ascii').lower())

    # Access category page and check the title displayed
    response = self.client.get(reverse('show_category', args=[categories[0].slug]))
    self.assertIn(categories[0].name.lower(), response.content.decode('ascii').lower())

    # Access about page and check the title displayed
    response = self.client.get(reverse('about'))
    self.assertIn('About'.lower(), response.content.decode('ascii').lower())

    # Access login page and check the title displayed
    response = self.client.get(reverse('login'))
    self.assertIn('Login'.lower(), response.content.decode('ascii').lower())

    # Access register page and check the title displayed
    response = self.client.get(reverse('register'))
    self.assertIn('Register'.lower(), response.content.decode('ascii').lower())

    # Access restricted page and check the title displayed
    response = self.client.get(reverse('restricted'))
    self.assertIn("Since you're logged in".lower(), response.content.decode('ascii').lower())

    # Access add page and check the title displayed
    response = self.client.get(reverse('add_page', args=[categories[0].slug]))
    self.assertIn('Add Page'.lower(), response.content.decode('ascii').lower())

    # Access add new category page and check the title displayed
    response = self.client.get(reverse('add_category'))
    self.assertIn('Add Category'.lower(), response.content.decode('ascii').lower())


