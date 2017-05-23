import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation


class VagPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    plugins.implements(plugins.ITranslation)
    # IConfigurer


    # IRoutes

    def before_map(self, map):
    	#Define vag routes
    	rtw_controller = 'ckanext.vag.controllers.widget:RealTimeWidgetController'

    	map.connect('real_time_widget',
    		'/real_time_widget',
    		 controller=rtw_controller, 
    		 action='real_time_widget')
        return map

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'vag')