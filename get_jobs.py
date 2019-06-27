import os
from pprint import pprint
from dotenv import load_dotenv
from linkedin_v2 import linkedin
import webbrowser

load_dotenv()

LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")
JOB_PERMISSION = "r_JYMBII"
PERMISSIONS = ["r_emailaddress", "r_liteprofile", JOB_PERMISSION]

def user_get_token(permissions):
    CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "OOPS")
    CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "OOPS")
    REDIRECT_URL = os.environ.get("LINKEDIN_REDIRECT_URL", "http://localhost:8000")
    auth = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, permissions)
    webbrowser.open_new(auth.authorization_url)
    # login, grant permissions, then you'll be redirected to a localhost url.
    # ... observe the "code" parameter, and enter it below
    # ... making sure to remove the "state" parameter part of the url, which might come at the end
    auth_code = input("The auth code was:")
    auth.authorization_code = auth_code
    access_token = auth.get_access_token() # this is an AccessToken object with a access_token property, which should be stored in the env var
    return access_token

if __name__ == "__main__":

    print("----------------")
    print("GETTING TOKEN...")
    if LINKEDIN_ACCESS_TOKEN:
        token = LINKEDIN_ACCESS_TOKEN
    else:
        token = user_get_token(PERMISSIONS)
    print(token) # store in environment variable!

    breakpoint()


    print("----------------")
    print("INITIALIZING APP...")
    client = linkedin.LinkedInApplication(token=token)
    #print(type(client))

    print("----------------")
    print("GETTING RECOMMENDED JOBS...")
    jobs = client._______()
    pprint(jobs)
