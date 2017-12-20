from django.forms.models import ModelForm

from mysite.blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')