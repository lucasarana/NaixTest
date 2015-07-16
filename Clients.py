__author__ = 'lucas.arana'

import soundcloud

class Clients:

    def SoundCloudClient(self):

        soundCloudClient = soundcloud.Client(
        client_id = 'efb4da00b3d22f63a53c8f0b9b96c553',
        client_secret = '6b8bbb0743b912695afd94fe0187c7b7',
        redirect_uri='http://localhost:2020/petitionresolved'
        )
        return soundCloudClient