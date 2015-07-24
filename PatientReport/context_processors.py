from django.core.exceptions import ObjectDoesNotExist


def logged_in_user(request):
    user = request.user
    try:
        surgeon = user.surgeon
        return {'surgeon_user': surgeon, 'template_base': 'surgeonBase.html'}
    except ObjectDoesNotExist:
        pass
    except AttributeError:
        pass
    try:
        patient = user.patient
        return {'patient_user': patient, 'template_base': 'patientBase.html'}
    except ObjectDoesNotExist:
        pass
    except AttributeError:
        pass
    try:
        staff = user.staff
        return {'staff_user': staff, 'template_base': 'staffBase.html'}
    except ObjectDoesNotExist:
        pass
    except AttributeError:
        pass
    return {'template_base': 'base.html'}