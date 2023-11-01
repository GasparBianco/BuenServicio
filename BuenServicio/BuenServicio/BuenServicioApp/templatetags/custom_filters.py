from django import template

register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    group_ranks = {
        'Mesero': 1,
        'Cajero': 2,
        'Encargado': 3,
        'Administrador': 4,
    }

    user_group = user.groups.first()
    required_rank = group_ranks.get(group_name, None)

    if user_group and required_rank is not None:
        return group_ranks.get(user_group.name, 0) >= required_rank

    return False
