from os import path
from unittest import mock

from django.test import TestCase
from django.core.management import call_command

import command_overrides


class StartAppTestCase(TestCase):

    @mock.patch('django.core.management.commands.startapp.Command.handle')
    def test_overridden_start_app(self, *mocks):
        """
        Test we successfully inject our custom template.
        """
        args = ['test_app']
        opts = dict([('template', None)])
        call_command('startapp', *args, **opts)

        template_path = path.join(command_overrides.__path__[0], 'conf', 'app_template')
        self.assertEqual(template_path, mocks[0].call_args[1].get('template'))

