from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from user.models import User


class AuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = 'username', 'password'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2')
