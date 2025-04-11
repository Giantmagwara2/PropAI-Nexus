# /backend/localization.py

import os
from typing import Dict

# A simple localization dictionary for demonstration.
localization_data: Dict[str, Dict[str, str]] = {
    'en': {
        'internal_server_error': "An internal server error occurred.",
        'unauthorized': "Unauthorized access.",
    },
    'es': {
        'internal_server_error': "Ocurrió un error interno del servidor.",
        'unauthorized': "Acceso no autorizado.",
    },
    # Add more languages as needed...
}

def get_localized_message(language: str, key: str) -> str:
    # Default to English if language not supported
    lang = language if language in localization_data else 'en'
    return localization_data[lang].get(key, key)
