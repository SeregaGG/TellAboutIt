from django import template

register = template.Library()


@register.simple_tag(name='main_menu')
def get_main_menu():
    menu = [{'title': 'About site', 'url': 'about'},
            {'title': 'Create article', 'url': 'create_article'},
            {'title': 'Sign in', 'url': 'sign_in'}]
    return menu


# register.simple_tag(get_main_menu, name='main_menu')
