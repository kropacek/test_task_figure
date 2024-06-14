from django import forms


class UnloadCoordinatesForm(forms.Form):
    truck_id = forms.IntegerField(widget=forms.HiddenInput())
    unload_coordinates = forms.CharField(max_length=20, label='')

    def clean_unload_coordinates(self):
        data = self.cleaned_data['unload_coordinates']
        coords = data.split()
        if len(coords) == 2:
            try:
                point = float(coords[0]), float(coords[1])
            except:
                raise forms.ValidationError('Wrong type of coordinates')
        else:
            raise forms.ValidationError('Needs 2 coordinates: X Y')
        return data
