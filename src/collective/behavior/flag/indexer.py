from plone.indexer.decorator import indexer
from .behaviors.flaggedobject import IFlaggableObject


@indexer(IFlaggableObject)
def flaggedobject(object, **kw):
    return object.flaggedobject

