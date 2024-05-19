import dramatiq
from django.core.mail import EmailMessage


@dramatiq.actor
def send_email_with_form_values(
    title: str, description: str, email: str, is_done: bool, is_new_todo: bool
):
    subject = f"{'created' if is_new_todo else 'updated'} ToDo Item"
    body = f"""
    Title: {title}
    Description: {description}
    
    This item is {"Done!" if is_done else "Not Done, Yet!"}
    """
    print(f"sending email to {email}", body)
    msg = EmailMessage(subject=subject, body=body, to=[email])
    msg.send()
