from fastapi import Request
from fastapi.templating import Jinja2Templates
from babel import Locale, dates
from babel.support import Translations
import os

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Load translations
def get_locale(request: Request):
    accept_language = request.headers.get("accept-language", "en")
    return accept_language.split(",")[0]

def get_translations(locale):
    translations_path = os.path.join("locales", locale, "LC_MESSAGES", "messages.mo")
    if os.path.exists(translations_path):
        return Translations.load(dirname=os.path.join("locales", locale, "LC_MESSAGES"), locales=[locale])
    return None

# Endpoint with internationalization
@app.get("/greet/")
async def greet(request: Request):
    locale = get_locale(request)
    translations = get_translations(locale)
    if translations:
        greeting = translations.gettext("Hello, welcome to the Property Value Predictor!")
    else:
        greeting = "Hello, welcome to the Property Value Predictor!"
    return templates.TemplateResponse("greet.html", {"request": request, "greeting": greeting})
