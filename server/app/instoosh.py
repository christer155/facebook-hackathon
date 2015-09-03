from instagram.client import InstagramAPI
import json, requests

class Instoosh:

    def __init__(self):
        self.instagram_client_id = "b4c040b6991745dba56b25ed82977d4d"
        self.instagram_client_secret = "cf93546e4da84780b68e3017411f21be"

    def getPostsByTag(self, tag_name, count=20):
        api = InstagramAPI(client_id=self.instagram_client_id, client_secret=self.instagram_client_secret)

        # dunnoWhatThisIs, httpResponse = api.tag_recent_media(tag_name=tag_name, count=count, max_tag_id='12345')
        dunnoWhatThisIs, httpResponse = api.media_search(q=tag_name, lat='32.067939', lng='34.770462')
        responseText = requests.get(httpResponse)
        jsonResponse = json.loads(responseText.text)
        posts = jsonResponse['data']
        texts = []
        for post in posts:
            texts.append(post['caption']['text'])

        return texts
