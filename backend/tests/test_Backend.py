
from flask_testing import TestCase

import backend.server

class TodolistAPITestCase(TestCase):


    def create_app(self):
        return backend.server.app

    def test_alwaysTrue(self):
        #Yeah we should really have some Test there, but hey its a demo :)
        self.assertTrue(True)