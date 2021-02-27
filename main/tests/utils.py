import json
import re

from django.contrib.auth.models import User
from django.test import Client


def _get_logged_client(username, password=None):
    """
    Returns a logged in Client instance, if password is provided the login process will be executed as usual, otherwise
    the login will be forced assigning the user instance to the Client instance directly.
    """
    client = Client()

    if not password:
        user = User.objects.get(username=username)
        client.force_login(user)
    else:
        client.login(username=username, password=password)

    return client


def get_standard_client():
    """
    Returns a Client instance referencing a user with staff=False, ensure to load test/common fixture
    before calling this.
    """
    return _get_logged_client('test_standard')


def get_staff_client():
    """
    Returns a Client instance referencing a user with staff=True, ensure to load test/common fixture
    before calling this.
    """
    return _get_logged_client('test_admin')


def eval_pagination_regex(response, entries_count, no_results_name='entries'):
    """
    Common regex used to test list views for some models
    """
    regex = r'(Showing 1 to [0-9]+ of {})|(No {} were found.)'.format(entries_count, no_results_name)
    return bool(re.search(regex, response.content.decode('utf-8')))


def check_redirection_to(testcase, response, to, final_status=302):
    """
    Provides the common checks for response with follow=True
    """
    redirects_number = len(response.redirect_chain)
    last_url, status_code = response.redirect_chain[-1] if redirects_number > 0 else (None, None)

    testcase.assertGreater(redirects_number, 0)
    testcase.assertEqual(status_code, final_status)
    testcase.assertRegexpMatches(last_url, to)


def load_json(response):
    return json.loads(response.content)
