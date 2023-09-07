from django import forms
from .models import Pitch

class PitchSubmissionForm(forms.ModelForm):
    pitch_images = forms.FileField(widget=forms.ClearableFileInput(attrs={"allow_multiple_selected": True}), required=False)

    class Meta:
        model = Pitch
        fields = ['pitch_title', 'pitch_description', 'pitch_category', 'pitch_images']
