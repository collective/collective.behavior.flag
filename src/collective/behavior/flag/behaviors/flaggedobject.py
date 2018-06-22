# -*- coding: utf-8 -*-

from collective.behavior.flag import _
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


@provider(IFormFieldProvider)
class IFlaggableObject(model.Schema):
    """
    """

    model.fieldset(
        'settings',
        label=u'Settings',
        fields=[
            'flaggedobject',
        ]
    )

    flaggedobject = schema.Bool(
        title=_(u'Special object'),
        description=_(u'Mark this object as special'),
        default=False,
        required=False,
    )


@implementer(IFlaggableObject)
@adapter(IDexterityContent)
class FlaggableObject(object):
    def __init__(self, context):
        self.context = context

    @property
    def flaggedobject(self):
        if hasattr(self.context, 'flaggedobject'):
            return self.context.flaggedobject
        return None

    @flaggedobject.setter
    def project(self, value):
        self.context.flaggedobject = value
