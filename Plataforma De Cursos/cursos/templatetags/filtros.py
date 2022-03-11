from django import template

# Uma library carregada para o Django
register = template.Library()


@register.filter
def return_list(value, arg):
    return [i for i in range(int(arg))]
