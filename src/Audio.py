# Class for obtaining audio from spotify

import spotify

class MusicGetter:
    
    def __init__(self):
        self.session = spotify.Session()
        # logging in 
        self.session.login("skandakk@gmail.com", "s3cr37pa$$w0rD")
        