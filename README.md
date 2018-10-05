## Python OAuth2 and OpenID sample using Client

This sample app is meant to provide working example of how to Connect with QuickBooks using Python Client. 

Please note that while these examples work, features called out above are not intended to be taken and used in production business applications. In other words, this is not a seed project to be taken cart blanche and deployed to your production environment.

For example, certain concerns are not addressed at all in our samples (e.g. security, privacy, scalability). In our sample apps, we strive to strike a balance between clarity, maintainability, and performance where we can. However, clarity is ultimately the most important quality in a sample app.

Therefore there are certain instances where we might forgo a more complicated implementation (e.g. caching a frequently used value, robust error handling, more generic domain model structure) in favor of code that is easier to read. In that light, we welcome any feedback that makes our samples apps easier to learn from.

### Getting Started

#### Clone the repository:
    
    git clone https://github.com/IntuitDeveloper/SampleOAuth2_UsingPythonClient.git

Note: This sample has been developed with Python 3.6

#### Install dependencies:

    cd SampleOAuth2_UsingPythonClient/
    pip install -r requirements.txt 

#### Configure app

1. Enter your app's `Client ID`, `Client Secret`, `Redirect URL` and app `environment` (`production` or `sandbox`) in [settings.py](SampleOAuth2_UsingPythonClient/settings.py).
2. Make sure the same `Redirect URL` is entered in your Intuit developer app `Keys` tab under the right environment.
3. To test Migration API, also enter `OAuth1 credentials` in the same file.

#### Launch your app:

    python manage.py runserver

Launch URL `http://localhost:8000/app`

### App Workflows
1. OAuth flow followed by QBO API call
2. OpenID flow followed by User Info API call
3. Migration API to migrate tokens from OAuth1 to OAuth2
4. Refresh and Revoke API for OAuth2/OpenID `bearer_token`
