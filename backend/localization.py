# /backend/localization.py

import os
from fastapi import Request
from babel import Locale, dates
from babel.support import Translations
from typing import Dict

# Default language setup
DEFAULT_LANGUAGE = 'en'

# Localization dictionary for simple fallback
localization_data: Dict[str, Dict[str, str]] = {
    'en': {
        'internal_server_error': "An internal server error occurred.",
        'unauthorized': "Unauthorized access.",
        'property_not_found': "Property not found.",
        'invalid_request': "Invalid request data provided.",
        'prediction_failed': "Prediction could not be completed.",
    },
    'es': {
        'internal_server_error': "Ocurrió un error interno del servidor.",
        'unauthorized': "Acceso no autorizado.",
        'property_not_found': "Propiedad no encontrada.",
        'invalid_request': "Datos de solicitud inválidos.",
        'prediction_failed': "No se pudo completar la predicción.",
    },
    # More languages can be added
}

def get_locale(request: Request) -> str:
    """
    Retrieves the locale (language) preference from the request header.
    Falls back to 'en' if no valid locale is found.
    """
    accept_language = request.headers.get("accept-language", DEFAULT_LANGUAGE)
    return accept_language.split(",")[0]

def get_translations(locale: str) -> Translations:
    """
    Retrieves translations for the specified locale from the local 'locales' directory.
    """
    translations_path = os.path.join("locales", locale, "LC_MESSAGES", "messages.mo")
    if os.path.exists(translations_path):
        return Translations.load(dirname=os.path.join("locales", locale, "LC_MESSAGES"), locales=[locale])
    return None

def get_localized_message(language: str, key: str) -> str:
    """
    Fetches the translation for a given key based on the provided language.
    Falls back to English if the language is missing or key is not found.
    """
    lang = language.lower().split("-")[0]  # Handle locale such as 'en-US', 'es-MX'
    
    # Fallback to English if language is unsupported
    if lang not in localization_data:
        lang = 'en'

    return localization_data[lang].get(key, localization_data['en'].get(key, key))
