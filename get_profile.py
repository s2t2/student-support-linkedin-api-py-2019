import os
from dotenv import load_dotenv
from linkedin_v2 import linkedin

load_dotenv()

CLIENT_ID = os.environ.get("LINKEDIN_CLIENT_ID", "OOPS")
CLIENT_SECRET = os.environ.get("LINKEDIN_CLIENT_SECRET", "OOPS")
REDIRECT_URL = os.environ.get("LINKEDIN_REDIRECT_URL", "http://localhost:8000")
PERMISSIONS = linkedin.PERMISSIONS.enums.values()
#print(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)
#print(PERMISSIONS) #> dict_values(['rw_company_admin', 'r_basicprofile', 'r_fullprofile', 'r_emailaddress', 'r_network', 'r_contactinfo', 'rw_nus', 'rw_groups', 'w_messages'])

auth = linkedin.LinkedInAuthentication(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL, PERMISSIONS)
print(type(auth))
print(auth.authorization_url) # opening this url in the browser. seeing unauthorized_scope_error...





breakpoint()





app = linkedin.LinkedInApplication(auth)
print(type(app))











auth.authorization_code = '______________'
auth.get_access_token()


#AUTH_TOKEN =
#app = linkedin.LinkedInApplication(token=AUTH_TOKEN)
