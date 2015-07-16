__author__ = 'lucas.arana'

from Clients import Clients

class Petitions:
    """Class for every service and petition requested by the Client"""

    @staticmethod
    def petition(handler):
        """Just trying out soundCloud redirection system"""
        client_object = Clients()
        soundCloudClient = client_object.SoundCloudClient()
        handler.redirect(soundCloudClient.authorize_url())

    @staticmethod
    def petitionresolved(handler):
        """Getting back from redirection of SoundCloud and getting Acces_Token"""
        client_object = Clients()
        soundCloudClient = client_object.SoundCloudClient()
        code = handler.get_argument('code')
        access_token = soundCloudClient.exchange_token(code)

        # render_text("Hi There, %s" % client.get('/me').username)

        return access_token.refresh_token
