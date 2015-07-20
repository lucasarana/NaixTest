__author__ = 'lucas.arana'

import soundcloud

class Clients:
    """Class containing all necessary information from the Clients"""

    def SoundCloudClient(self, access_token=[]):
        """Sound Clouds detailed Client"""
        if access_token:
            sound_cloud_client = soundcloud.Client(
                access_token=access_token
                )
        else:
            sound_cloud_client = soundcloud.Client(
                client_id = 'efb4da00b3d22f63a53c8f0b9b96c553',
                client_secret = '6b8bbb0743b912695afd94fe0187c7b7',
                redirect_uri='http://localhost:2020/petitionresolved'
                )

        return sound_cloud_client
