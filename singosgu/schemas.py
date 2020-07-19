import coreapi
from rest_framework.schemas import AutoSchema

class RegisterUserSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_field = []
        if method.lower() in ['post']:
            extra_field = [
                coreapi.Field('name'),
                coreapi.Field('password1'),
                coreapi.Field('password2')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_field

class LoginUserSchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_field = []
        if method.lower() in ['post']:
            extra_field = [
                coreapi.Field('name'),
                coreapi.Field('password')
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_field