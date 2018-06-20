# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.behavior.flag


class CollectiveBehaviorFlagLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=collective.behavior.flag)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.behavior.flag:default')


COLLECTIVE_BEHAVIOR_FLAG_FIXTURE = CollectiveBehaviorFlagLayer()


COLLECTIVE_BEHAVIOR_FLAG_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_BEHAVIOR_FLAG_FIXTURE,),
    name='CollectiveBehaviorFlagLayer:IntegrationTesting',
)


COLLECTIVE_BEHAVIOR_FLAG_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_BEHAVIOR_FLAG_FIXTURE,),
    name='CollectiveBehaviorFlagLayer:FunctionalTesting',
)


COLLECTIVE_BEHAVIOR_FLAG_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_BEHAVIOR_FLAG_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveBehaviorFlagLayer:AcceptanceTesting',
)
