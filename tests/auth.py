import requests
from enums import Auth, WEB_LINK

def all_auth():

    for auth in Auth:
        print(str(requests(WEB_LINK + auth.value)))