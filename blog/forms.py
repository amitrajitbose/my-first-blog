#importing forms from django
from django import forms
#importing the model Post that we created from models
from .models import Post

#PostForm will be the name of our form
#We need to tell Django that this form is a model form
class PostForm(forms.ModelForm):
    class Meta:
        #what does meta do ?
        #tells django which model should be used to 
        #create the form, viz. Post model
        #the fields that need to be exposed on the form are passed
        model = Post
        fields = ('title', 'text',)

