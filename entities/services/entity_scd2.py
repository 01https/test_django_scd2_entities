from django.utils import timezone

from entities.models import Entity


def update_entity(entity: Entity, new_display_name=None):
    if entity.is_current:
        entity.is_current = False
        entity.valid_to = timezone.now()
        entity.save()

    new_entity = Entity.objects.create(
        uid=entity.uid,
        display_name=new_display_name or entity.display_name,
        type=entity.type,
        valid_from=timezone.now(),
        is_current=True
    )
    return new_entity