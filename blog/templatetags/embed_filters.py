from django import template
import re

register = template.Library()

@register.filter
def embed_url(value):
    """
    Transforms YouTube URLs into embeddable format
    """
    youtube_match = re.match(r'.*youtu\.be/(.*)', value) or re.match(r'.*youtube\.com/watch\?v=([^&]+)', value)
    if youtube_match:
        video_id = youtube_match.group(1)
        return f"https://www.youtube.com/embed/{video_id}"
    return value
