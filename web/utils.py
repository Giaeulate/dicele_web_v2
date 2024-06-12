""" Utils """
# pylint: disable=too-few-public-methods, missing-class-docstring, protected-access, no-member, wildcard-import, unused-wildcard-import, missing-function-docstring


def get_custom_admin_list(model):
    return [
        x.name for x in model._meta.fields
        if not x.name == 'active' and
        not x.name == 'created' and
        not x.name == 'updated'
    ]
