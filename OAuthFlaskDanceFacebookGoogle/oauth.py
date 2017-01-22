from flask import url_for, flash
from flask_dance.contrib.facebook import facebook
from flask_dance.contrib.google import google


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('callback', provider=self.provider_name,
                       _external=True)

    @classmethod
    def get_provider(cls, provider_name):
        if cls.providers is None:
            cls.providers = {}
            for provider_class in cls.__subclasses__():
                provider = provider_class()
                cls.providers[provider.provider_name] = provider
        return cls.providers[provider_name]


class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')

    def callback(self):
        resp = facebook.get('me?fields=id,first_name,email').json()
        try:
            return resp['id'], resp['first_name'], resp['email']
        except KeyError:
            flash(resp)
            return None, None, None


class GoogleSignIn(OAuthSignIn):
    def __init__(self):
        super(GoogleSignIn, self).__init__('google')

    def callback(self):
        resp = google.get("/plus/v1/people/me").json()
        try:
            return resp['id'], resp['name']['givenName'], resp['emails'][0]['value']
        except KeyError:
            flash(resp)
            return None, None, None
