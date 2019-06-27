import os
from dotenv import load_dotenv
from linkedin_v2 import linkedin
import webbrowser

load_dotenv()

def user_get_token():
    #
    # GET AN AUTH CODE
    #
    CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "OOPS")
    CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "OOPS")
    REDIRECT_URL = os.environ.get("LINKEDIN_REDIRECT_URL", "http://localhost:8000")
    PERMISSIONS = linkedin.PERMISSIONS.enums.values()
    #print(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)
    #print(PERMISSIONS) #> dict_values(['rw_company_admin', 'r_basicprofile', 'r_fullprofile', 'r_emailaddress', 'r_network', 'r_contactinfo', 'rw_nus', 'rw_groups', 'w_messages'])

    auth = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, ["r_basicprofile"])
    #print(type(auth)) #> <class 'linkedin_v2.linkedin.LinkedInAuthentication'>
    #print(auth.authorization_url) # opening this url in the browser. seeing unauthorized_scope_error...

    webbrowser.open_new(auth.authorization_url)
    # login, grant permissions, then you'll be redirected to a localhost url.
    # ... observe the "code" parameter, and store in a variable called AUTH_CODE
    # ... making sure to remove the "state" parameter part of the url, which might come at the end

    ## or maybe just ask the user for it...
    auth_code = input("The auth code was:")

    auth.authorization_code = auth_code

    #
    # GET AN ACCESS TOKEN
    #

    access_token = auth.get_access_token()

    return access_token

if __name__ == "__main__":

    token = user_get_token()
    print(token) # store in environment variable!
    app = linkedin.LinkedInApplication(token=token)

    print(type(app))
