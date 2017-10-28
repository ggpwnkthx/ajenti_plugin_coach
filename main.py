from jadi import component

from aj.plugins.core.api.sidebar import SidebarItemProvider


@component(SidebarItemProvider)
class ItemProvider(SidebarItemProvider):
    '''
    To add a sidebar item, we create a component implementing SidebarItemProvider
    '''
    def __init__(self, context):
        pass

    def provide(self):
        return [
            {
                'attach': None,
                'id': 'category:cluster',
                'name': _('Cluster'),
                'children': []
            },
		]
