from django.conf import settings
from django.templatetags.static import static

# django-fullcalendar static file location defaults to FullCalendar default 
# folder structure, expected to be under the STATIC_URL

FULLCALENDAR_DEFAULTS: dict[str] = {
    'fullcalendar_css_url': static('fullcalendar/main.min.css'),
    'fullcalendar_url': static('fullcalendar/main.min.js'),
    'jquery_url': static('jquery/dist/jquery.js'),
    'jquery_ui_url': static('jquery-ui-dist/jquery-ui.js'),
    'bootstrap_css_url': static('bootstrap/dist/css/bootstrap.min.css'),
    'fontawesome_css_url': 'https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.13.1/css/all.css',
}

# Updates location based on configuration defined by 
# settings.py of the project

FULLCALENDAR = FULLCALENDAR_DEFAULTS.copy()
FULLCALENDAR |= getattr(settings, 'FULLCALENDAR', {})


def get_url(key: str) -> str:
    return FULLCALENDAR[key]


def css_url():
    return FULLCALENDAR['css_url']


def javascript_url():
    return FULLCALENDAR['javascript_url']


def jquery_url():
    return FULLCALENDAR['jquery_url']


def jquery_ui_url():
    return FULLCALENDAR['jquery_ui_url']


def bootstrap_css_url():
    return FULLCALENDAR['bootstrap_css_url']


def fontawesome_css_url():
    return FULLCALENDAR['bootstrap_css_url']

