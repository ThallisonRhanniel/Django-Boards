from django import template

register = template.Library()

@register.filter
def field_type(bound_field): # pego o tipo do campo. Ex 'TextInput'
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field): # Retorno a classe. Ex: 'form-control'
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)