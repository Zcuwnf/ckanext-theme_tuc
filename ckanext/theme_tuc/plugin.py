from ckan import plugins
from ckan.plugins import toolkit
from ckan.lib.plugins import DefaultTranslation


class ThemeTucPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITranslation)

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource('fanstatic', 'theme_tuc')

class StatsPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.IConfigurer, inherit=True)

    def before_map(self, m):
        m.connect('stats',
            '/stats',
            controllers='ckanext.theme_tuc.controllers:StatsController',
            action='stats') 
        return m