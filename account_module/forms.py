from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        label='ایمیل',
        min_length=6,
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'input100',
            'placeholder': 'ایمیل خود را وارد کنید',
            'autocomplete': 'new-password',
        })
    )
    password = forms.CharField(
        label='کلمه عبور',
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput(attrs={
            'class': 'input100',
            'placeholder': 'کلمه عبور خود را وارد کنید',
            'autocomplete': 'new-password',
        })
    )
