from django.contrib.auth.models import User

def is_email_unique(email):
      """
      Check if the given email is unique among all User instances.

      Args:
          email (str): The email address to check for uniqueness.

      Returns:
          bool: True if the email is unique, False otherwise.
      """
      return not User.objects.filter(email=email).exists()