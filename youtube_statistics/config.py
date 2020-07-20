import os

RESOURCE_DIR = os.path.join(os.path.join(os.getcwd(), 'youtube_statistics'), 'resource')

if not os.path.exists(RESOURCE_DIR):
    os.mkdir(RESOURCE_DIR)

DATA_FILE = os.path.join(RESOURCE_DIR, 'udacity_view_data.csv')
GOOGLE_OAUTH_CLIENT_ID = 'client_secret.json'