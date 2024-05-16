import dramatiq
from django.core.mail import EmailMessage


@dramatiq.actor
def send_email_with_form_values(
    title: str, description: str, email: str, is_new_todo: bool
):
    subject = f"{'created' if is_new_todo else 'updated'} ToDo Item"
    body = f"""
    Title: {title}
    Description: {description}
    """
    print("sending email", body)
    msg = EmailMessage(subject=subject, body=body, to=[email])
    print(f"FROM {msg.from_email} \nTO {msg.to}")
    msg.send()
