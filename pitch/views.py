from django.shortcuts import render, redirect
from .forms import PitchSubmissionForm 
from .models import Pitch , Image

from django.shortcuts import render
from .forms import PitchSubmissionForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


def submit_pitch(request):
    if request.method == 'POST':
        form = PitchSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            pitch = form.save(commit=False)
            pitch.user = request.user
            pitch.save()

            # Handle multiple images
            for image_file in request.FILES.getlist('pitch_images'):
                # Create an Image instance for each uploaded file
                Image.objects.create(pitch=pitch, image=image_file)

            # Redirect to a success page or do other processing
    else:
        form = PitchSubmissionForm()
    return render(request, 'pitch_form.html', {'form': form})

# def view_pitches(request):
#     pitches = Pitch.objects.all()
#     return render(request, 'pitch_list.html', {'pitches': pitches})

def view_pitches(request):
    pitches = Pitch.objects.all().order_by('-submission_date')  # Order by the user
    return render(request, 'pitch_list.html', {'pitches': pitches})



def my_pitches(request):
    # Retrieve the user's pitches
    user_pitches = Pitch.objects.filter(user=request.user)
    
    # You can add additional context if needed
    context = {
        'user_pitches': user_pitches,
    }
    
    return render(request, 'my_pitches.html', context)


def delete_pitch(request, pitch_id):
    # Get the pitch object to be deleted
    pitch = get_object_or_404(Pitch, id=pitch_id)

    # Check if the logged-in user is the owner of the pitch
    if request.user == pitch.user:
        # Delete the pitch
        pitch.delete()
        messages.success(request, 'Pitch deleted successfully.')
    else:
        messages.error(request, 'You do not have permission to delete this pitch.')

    # Redirect back to the user's pitches page
    return redirect('pitch:my_pitches')
