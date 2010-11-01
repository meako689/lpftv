from django.conf import settings
from django import template
from apps.serials.models import Episode

register = template.Library()

class LastEpisodeNode(template.Node):
    """Return 5 last episodes in context 'last_episode' """
    def __init__(self):
        self.last_episodes = Episode.objects.order_by('-pub_date')[0:4]
    
    def render(self, context):
        context['last_episodes'] = self.last_episodes
        return ''

def last_episode(parser, token):
    """Tags for template for get last 5 episodes"""
    return LastEpisodeNode()

last_episode = register.tag(last_episode)

