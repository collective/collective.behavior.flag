from plone.indexer.decorator import indexer
from .behaviors.flaggedobject import IFlaggableObject
from Products.CMFPlone.utils import safe_hasattr

@indexer(IFlaggableObject)
def flaggedobject(object, **kw):
    if safe_hasattr(object, 'flaggedobject'):
        return bool(object.flaggedobject)
    else:
        return False


