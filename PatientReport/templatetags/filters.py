from django import template
from FJSharif.settings import MEDIA_URL

__author__ = 'navid'

register = template.Library()


@register.filter(name='age')
def age(delta):
    years = delta.days / 365
    if years > 100:
        return '%s Years!' % years
    else:
        return '%s Years.' % years


@register.filter(name='description')
def description(person):
    if person.description:
        return person.description
    return 'No description.'


@register.filter(name='diagnosis')
def diagnosis(order):
    if order.primary_diagnosis:
        return order.primary_diagnosis
    return 'N/A!'


@register.filter(name='email')
def email(person):
    if person.user.email:
        return person.user.email
    return 'N/A!'

@register.filter(name='address')
def address(surgeon):
    if surgeon.address:
        return surgeon.address
    return 'Unknown Address.'


@register.filter(name='person_picture')
def person_picture(person):
    if person.picture:
        return person.picture.url
    elif person.gender == 'F':
        return MEDIA_URL+'images/avatar/female_person.jpg'
    return MEDIA_URL+'images/avatar/male_person.jpg'


@register.filter
def object_date(object):
    try:
        date = object.date
        if date:
            return date
        else:
            return 'Unknown Date!'
    except Exception:
        return 'Unknown Date!'


@register.filter(name='picture')
def picture(input):
    if input.picture:
        return input.picture.url
    return MEDIA_URL+'images/avatar/image.jpg'


@register.simple_tag
def alignment_parameter_picture(**kwargs):
    order = kwargs['order']
    parameter_name = kwargs['parameter_name']
    type = kwargs['type']
    for p in order.report.alignmentparameter_set.all():
        if p.type == type and p.name.name == parameter_name:
            if p.picture:
                return p.picture.url
    return MEDIA_URL+'images/avatar/image.jpg'


@register.simple_tag
def alignment_parameter_value(**kwargs):
    order = kwargs['order']
    parameter_name = kwargs['parameter_name']
    type = kwargs['type']
    for p in order.report.alignmentparameter_set.all():
        if p.type == type and p.name.name == parameter_name:
            return round(p.value,1)
    return 'N/A'


@register.simple_tag
def alignment_parameter_color(**kwargs):
    order = kwargs['order']
    parameter_name = kwargs['parameter_name']
    type = kwargs['type']
    for p in order.report.alignmentparameter_set.all():
        if p.type == type and p.name.name == parameter_name:
            if p.value > p.name.max_value or p.value < p.name.min_value:
                return 'red'
    return 'green'


@register.simple_tag
def alignment_parameter_status(**kwargs):
    order = kwargs['order']
    parameter_name = kwargs['parameter_name']
    type = kwargs['type']
    for p in order.report.alignmentparameter_set.all():
        if p.type == type and p.name.name == parameter_name:
            if p.value > p.name.max_value:
                return 'Too high!'
            elif p.value < p.name.min_value:
                return 'Too low!'
            else:
                return 'Normal.'
    return 'N/A'




