from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from ..fullcalendar import get_url

register = template.Library()


@register.simple_tag
def calendar(calendar_id: str = 'calendar'):
    return format_html("<div id='{}'></div>", calendar_id)


@register.inclusion_tag('fullcalendar/calendar_init.html')
def calendar_init(calendar_id: str = 'calendar', calendar_config_options: str = None):
    return {'calendar_id': mark_safe(calendar_id), 'calendar_config_options': mark_safe(calendar_config_options)}


@register.simple_tag
def fullcalendar_css(url: str) -> str:
    return format_html("<link href='{}' rel='stylesheet' />", get_url(url))


@register.simple_tag
def fullcalendar_js(url: str) -> str:
    return format_html("<script src='{}'></script>", get_url(url))
