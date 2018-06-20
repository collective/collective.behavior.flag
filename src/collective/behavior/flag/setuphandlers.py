# -*- coding: utf-8 -*-
import logging
from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFPlone.utils import getToolByName
from zope.interface import implementer

logger = logging.getLogger('collective.behavior.flag')

@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            'collective.behavior.flag:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.
    add_indexes(context)


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def add_indexes(context):
    """Add indexes.
    """
    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()

    wanted_indexes = [
        ('flaggedobject', 'FieldIndex'),
    ]

    indexables = []
    for index_name, index_type in wanted_indexes:
        if index_name not in indexes:
            catalog.addIndex(index_name, index_type)
            indexables.append(index_name)
            logger.info('Added %s for %s.' % (index_type, index_name))
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        # I was pretty sure this also updated the catalog brains, but
        # it does not...
        catalog.manage_reindexIndex(ids=indexables)
