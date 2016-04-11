from tethys_sdk.base import TethysAppBase, url_map_maker


class Secondapp(TethysAppBase):
    """
    Tethys app class for secondapp.
    """

    name = 'Utah Trail Profiler'
    index = 'life:home'
    icon = 'life/images/loneArch.jpg'
    package = 'life'
    root_url = 'life'
    color = '#34495e'
    description = 'Place a brief description of your app here.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='home',
                           controller='life.controllers.home'),
                    UrlMap(name='help',
                           url='help',
                           controller='life.controllers.help'),
                    UrlMap(name='documentation',
                           url='documentation',
                           controller='life.controllers.documentation'),
        )

        return url_maps