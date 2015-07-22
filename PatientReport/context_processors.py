from django.core.exceptions import ObjectDoesNotExist


def logged_in_user(request):
    user = request.user
    try:
        surgeon = user.surgeon
        return {'surgeon': surgeon}
    except ObjectDoesNotExist:
        pass
    except AttributeError:
        pass
    return {}