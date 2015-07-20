__author__ = 'lucas.arana'

from Clients import Clients
from DANaix import DANaix

class Petitions:
    """Class for every service and petition requested by the Client"""

    @staticmethod
    def petition(handler):
        """Redirecting petition to SoundClouds Service"""
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
        DANaix.initiliaze_client(soundCloudClient.client_id, access_token.access_token)
        current_user = soundCloudClient.get('/me').username
        return current_user #Si lo hago acá anda!


    @staticmethod
    def getSoundCloudClient(handler):
        #Si lo hago aca no anda
        # client_id = handler.get_argument('client_id')
        access_token = DANaix.get_client_token('efb4da00b3d22f63a53c8f0b9b96c553')
        client_object = Clients()
        soundCloudClient = client_object.SoundCloudClient(access_token=access_token)
        current_user = soundCloudClient.get('/me').username
        return current_user
