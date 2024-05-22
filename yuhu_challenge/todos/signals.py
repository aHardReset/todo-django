from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ToDoItem
from .tasks import send_email_with_form_values


@receiver(post_save, sender=ToDoItem)
def create_attendance(sender, instance, created, **kwargs):
    print(f"signal triggered todo item {created=}")
    send_email_with_form_values.send(
        instance.name,
        instance.description,
        instance.user.email,
        instance.is_done,
        created,
    )
