from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", max_length=100, help_text="100 caracteres máximo")
    url = forms.URLField(label="Tu sitio web", required=False, initial="http://")
    comment = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre:", 
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control border border-secondary'}))
    email = forms.EmailField(
        label="Email:", 
        max_length=50,
        widget=forms.EmailInput(attrs={'class':'form-control border border-secondary'}))        
    message = forms.CharField(
        label="Mensaje:",
        widget=forms.Textarea(attrs={'class':'form-control border border-secondary'}))

    def clean_name(self):
        name = self.cleaned_data.get("name") 
        if name != "Open":
            raise forms.ValidationError("Tan solo el valor Open está permitido para este campo")
        else:
            return name