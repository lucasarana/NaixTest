__author__ = 'lucas.arana'

# import urllib3.contrib.pyopenssl
# urllib3.contrib.pyopenssl.inject_into_urllib3()

from Clients import Clients

class Petitions:

    @staticmethod
    def petition(handler):
        client_object = Clients()
        soundCloudClient = client_object.SoundCloudClient()
        handler.redirect(soundCloudClient.authorize_url())

    @staticmethod
    def petitionresolved(handler):
        client_object = Clients()
        soundCloudClient = client_object.SoundCloudClient()
        code = handler.get_argument('code')
        access_token = soundCloudClient.exchange_token(
            code=code)

        # render_text("Hi There, %s" % client.get('/me').username)

        return access_token