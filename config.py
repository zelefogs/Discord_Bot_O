import os


settings = {
    'token': os.environ.get("token", "Insert your API key OWM here"),
    'bot': 'test_bot',
    'id': 771490653795909674,
    'prefix': '<'
}

OWM_API_KEY = os.environ.get("OWM_API_KEY", "Insert your API key OWM here")