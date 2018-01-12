from django import template

from aids_jiance.shizhi.models import Shizhi

register = template.Library()

@register.inclusion_tag('shizhi/fangan.html')
def fangan(k):
    return {
        'objects':Shizhi.get_fangan(k)
    }

@register.inclusion_tag('shizhi/fangan_list.html')
def fangan_list(k, v):
    return {
        'objects':Shizhi.get_fangan(k),
        'v':v
    }