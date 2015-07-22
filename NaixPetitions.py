__author__ = 'lucas.arana'

from Clients import Clients
from DANaix import DANaix

class Petitions:
    """
    Class for every service and petition requested by the Client (Just SoundCloud for now)
    """

    def __init__(self):
        pass

    @staticmethod
    def petition(handler):
        """
        Redirecting petition to SoundClouds Service
        """
        # client_object = Clients()
        sound_cloud_client = Clients().sound_cloud_client()
        handler.redirect(sound_cloud_client.authorize_url())

    @staticmethod
    def sound_cloud_petition_resolved(handler):
        """
        Getting back from redirection of SoundCloud and getting Access_Token
        :param code: Code extracted from the URL that SoundCloud Redirect (Default)
        """
        code = handler.get_argument('code')
        sound_cloud_client = Clients().sound_cloud_client()
        access_token = sound_cloud_client.exchange_token(code)
        current_user = sound_cloud_client.get('/me').username
        DANaix.initialize_client(current_user, access_token.access_token)
        return "ok"  # Improve messages. Change to Json

    @staticmethod
    def get_sound_cloud_user(handler):
        """
        Retrieves the user name (Just for testing purposes). The user_id = current_user
        :param user_id: The user who is performing the action
        """
        user_id = handler.get_argument('user_id')
        sound_cloud_client = Petitions.instantiate_user(user_id)
        current_user = sound_cloud_client.get('/me').username
        return current_user  # Improve messages. Change to Json

    @staticmethod
    def upload_music(handler):
        """
        Uploads a music track into SoundCloud
        :param user_id: The user who is performing the action
        :param path: The path/route the music is stored (locally or url)
        """
        user_id = handler.get_argument('user_id')
        music_path = handler.get_argument('path') #Having problems parsing this out
        sound_cloud_client = Petitions.instantiate_user(user_id)
        track = sound_cloud_client.post('/tracks', track={
            'title': 'Testing Uploads',
            'asset_data': open(music_path, 'rb')
        })

        return track.permalink_url  # Improve messages. Change to Json

    @staticmethod
    def instantiate_user(user_id):
        """
        Creates a SoundCloud Client with his access token (searching in the DB)
        :param user_id: The user who is performing the action
        Note: Not a petition. Just internal functions to avoid DRY
        """
        access_token = DANaix.get_client_token(user_id)
        sound_cloud_client = Clients().sound_cloud_client(access_token=access_token)
        return sound_cloud_client
