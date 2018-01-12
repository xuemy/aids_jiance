from django import template


register = template.Library()


def iter_pages(paginator, page_obj, left_edge=2, left_current=2,
               right_current=4, right_edge=2):
    last = 0
    pages = paginator.num_pages
    page = page_obj.number
    for num in range(1, pages + 1):
        if num <= left_edge or \
            (num > page - left_current - 1 and num < page + right_current) or num > pages - right_edge:
            if last + 1 != num:
                yield None
            yield num
            last = num


@register.inclusion_tag('core/pagination.html')
def a_pagination(paginator, page_obj):
    return {
        'page_range': iter_pages(paginator, page_obj),
        'page_obj': page_obj
    }
