from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string

def request_details(request, username):
    try:
        # Attempt to get the user based on the provided username
        user = User.objects.get(username=username)
        user_email = user.email  # Assuming the email is stored in the User model

        # Send an email to the user
        context = {
            'recipient': user,
            'requester': request.user,  # Assuming the current user is the requester
        }

        email_subject = 'Request From PitchUp'
        email_message = render_to_string('request_details_email.html', context)
        send_mail(
            email_subject,
            'Plain text version of your message',
            'pitchup11@gmail.com',
            [user_email],
            html_message=email_message,  # Include the HTML content here
            fail_silently=False,
        )
        print(f"Email sent to {user_email}")
        # Create a JSON response with success message
        response_data = {'success': True, 'message': 'Email sent successfully!'}
        return JsonResponse(response_data)

    except User.DoesNotExist:
        # Handle the case where the user does not exist
        response_data = {'success': False, 'message': 'User not found.'}
        return JsonResponse(response_data, status=404)
