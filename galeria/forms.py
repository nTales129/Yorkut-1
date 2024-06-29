from django import forms

from galeria.models import Post, Comentario

from django.contrib.auth.models import User  

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'nome_usuario', 'imagem', 'legenda']  
        widgets = {
            'legenda': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),  
            'imagem': forms.FileInput(attrs={'class': 'form-control'}), 
            'nome_usuario': forms.TextInput(attrs={'class': 'form-control'}),  
        }

    def clean_imagem(self):
        imagem = self.cleaned_data['imagem']
        if imagem:
            content_type = imagem.content_type
            if content_type not in ['image/jpeg', 'image/png', 'image/gif']:
                raise forms.ValidationError('Somente JPEG, PNG, and GIF sao aceitas como formato de imagem.')
        return imagem

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Digite seu comentário aqui...'}),
        }