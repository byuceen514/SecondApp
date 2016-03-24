from tethys_sdk.base import TethysAppBase, url_map_maker


class Secondapp(TethysAppBase):
    """
    Tethys app class for secondapp.
    """

    name = 'Trail Profiler'
    index = 'life:home'
    icon = 'life/images/icon.gif'
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
                           url='life',
                           controller='life.controllers.home'),
        )

        return url_maps