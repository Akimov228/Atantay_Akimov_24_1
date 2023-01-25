from django import forms


class CreateProductForm(forms.Form):
    title = forms.CharField(min_length=3)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(required=False)


class CreateReviewForm(forms.Form):
    text = forms.CharField(min_length=1)
