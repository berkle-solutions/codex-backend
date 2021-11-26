import environ
from infobip_api_client.api_client import ApiClient, Configuration


env = environ.Env()
environ.Env.read_env()

client_config = Configuration(
    host=env('INFOBIP_BASE_URL'),
    api_key={"APIKeyHeader": env('INFOBIP_API_KEY')},
    api_key_prefix={"APIKeyHeader": env('INFOBIP_API_PREFIX')},
)

def initialize_infobip_service():
    api_client = ApiClient(client_config)
    return api_client