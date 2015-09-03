from instagram.client import InstagramAPI
from geopy.distance import vincenty

class Instoosh:

    def __init__(self):
        self.client = api = InstagramAPI(client_id="b4c040b6991745dba56b25ed82977d4d",
            client_secret="cf93546e4da84780b68e3017411f21be")

    def get_posts(self, search, point=None):
        '''
            get search field, and location cords 
            and return filters posts
        '''
        media_list, _ = self.client.tag_recent_media(tag_name=search, count=50)
        posts = []
        images = []
        def too_far(media):
            if hasattr(media, 'location') and hasattr(media.location, 'point'):
                return vincenty(point, media.location.point).meters <= 1000
            return False
        media_list = filter(too_far, media_list)
        for m in media_list:
            tags_text = ' '.join(map(lambda t: t.name, m.tags))
            posts.append(tags_text + ' ' + m.caption.text)
            if hasattr(m, 'images'):
                images.append(m.images['standard_resolution'].url)
        return posts, images
