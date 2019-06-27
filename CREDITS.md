# Credits, Notes, and Reference

## LinkedIn API

### Obtaining Credentials

  + https://www.linkedin.com/developers/

Login, visit the developer page, click "create app" button. Then provide the following info:

  + App name: "Student Support - Jobfinder"
  + Company name (WHY IS THIS REQUIRED?): "N/A" (DOESN'T ALLOW YOU TO PUT N/A). I chose  "NYU Stern School of Business"
  + Business Email: your email
  + Upload a logo (WHY IS THIS REQUIRED?) I uploaded a Python logo.
  + Products (WHAT DO EACH OF THESE MEAN?): leave the two default products checked ("Share on Linkedin, "Sign in on Linkedin"). The marketing product is maybe not necessary.
  + Check the box to say you agree with the terms

Redirected to the new app's settings. Navigate to the "__" tab to locate credentials "Client Id" and "Client Secret". Storing them in environment variables:
   + `LINKEDIN_CLIENT_ID`
   + `LINKEDIN_CLIENT_SECRET`

### Documentation

  + https://developer.linkedin.com/docs/guide/v2/jobs
  + https://developer.linkedin.com/docs/guide/v2/jobs/recommended-jobs

"The Recommended Jobs API returns jobs posted on LinkedIn that match the user’s profile. It exposes the same data as the section Jobs you may be interested in on Linkedin, and brings the benefits of LinkedIn’s job recommendation into your service."
