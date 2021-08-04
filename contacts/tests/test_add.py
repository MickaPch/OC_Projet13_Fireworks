

from django.contrib.auth.models import User
from django.urls.base import reverse
from contacts.tests.test_contacts_views import ContactsTest


class UserCanAddContactToCompanyTest(ContactsTest):

    def setUp(self):

        self.user_logged_in = self.client.login(
            username='User1',
            password='pwd$User1'
        )

        return super().setUp()
    
    def test_company_card_show_add_btn(self):

        response = self.client.get(reverse('contacts_home'))

        self.assertIn(
            b"add-contact-to-company",
            response.content
        )