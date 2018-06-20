# -*- coding: utf-8 -*-
from collective.behavior.flag.behaviors.flaggedobject import IFlaggedObject
from collective.behavior.flag.testing import COLLECTIVE_BEHAVIOR_FLAG_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class FlaggedObjectIntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_BEHAVIOR_FLAG_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_flaggedobject(self):
        behavior = getUtility(IBehavior, 'collective.behavior.flag.flaggedobject')
        self.assertEqual(
            behavior.marker,
            IFlaggedObject,
        )
        behavior_name = 'collective.behavior.flag.behaviors.flaggedobject.IFlaggedObject'
        behavior = getUtility(IBehavior, behavior_name)
        self.assertEqual(
            behavior.marker,
            IFlaggedObject,
        )
