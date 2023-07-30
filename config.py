from google.cloud import secretmanager

def get_secret_version(project_id, secret_id, version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode('UTF-8')

GCP_PROJECT_ID = "97418787038"
SITE_HOMEPAGE = "https://gcp-strava.wl.r.appspot.com/"

# OpenAI API Configurations
OPENAI_API_KEY_ID = "OPENAI_API_KEY"
OPENAI_SECRET_KEY = get_secret_version(GCP_PROJECT_ID, OPENAI_API_KEY_ID)

# Google Maps API Configurations
GOOGLE_MAPS_SECRET_API_ID = "google_maps_api_key"
GOOGLE_MAPS_API_KEY = get_secret_version(GCP_PROJECT_ID, GOOGLE_MAPS_SECRET_API_ID)