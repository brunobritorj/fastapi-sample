import os
from fastapi_msal import MSALClientConfig, MSALAuthorization, UserInfo

tenant = os.getenv("MSENTRA_TENANT", "common")
client_id = os.getenv("MSENTRA_CLIENT_ID")
client_secret = os.getenv("MSENTRA_CLIENT_SECRET")
secret_key = os.getenv("SECRET_KEY")

if (not client_id) or (not client_secret) or (not tenant):
    raise ValueError("Missing required environment variable")

client_config = MSALClientConfig(
    tenant=tenant,
    client_id=client_id,
    client_credential=client_secret
)

msal_auth = MSALAuthorization(client_config=client_config)
