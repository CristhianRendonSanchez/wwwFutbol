from django import forms


class LoginForm(forms.Form):
    class Meta:
        fields = [
            'name_user',
            'password_user'
            ]

        labels = {
            'name_user' : 'Nombre de usuario',
            'password_user' : 'Contraseña de usuario'
        }

        name_user = forms.CharField(max_length=20,required=True,label="",
                                    widget=(forms.TextInput(attrs={"placeholder":"@Nombre de Usuario","class":"imput-login"})))
        password_user = forms.CharField(max_length=20,required=True,label="",
                                        widget=(forms.PasswordInput(attrs={"placeholder":"Contraseña","class":"input:login"})))


class RegisterForm(forms.Form):
    email_user = forms.CharField(max_length=40,required=True,label="",
                                 widget=(forms.TextInput(attrs={"placeholder":"Correo Electronico", "class":"input-register"})))
    names_user = forms.CharField(max_length=40,required=True,label="",
                                 widget=(forms.TextInput(attrs={"placeholder":"Nombres Completos", "class":"input-register"})))
    password_user = forms.CharField(max_length=20,required=True,label="",
                                    widget=(forms.PasswordInput(attrs={"placeholder":"Contraseña","class":"input-register"})))