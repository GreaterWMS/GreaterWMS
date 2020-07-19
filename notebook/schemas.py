import coreapi
from rest_framework.schemas import AutoSchema

class NoteBook(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_field = []
        if method.lower() in ['post']:
            extra_field = [
                coreapi.Field(name="openid",
                              location="query",
                              required=True,
                              description="openid是发送请求必须的一个参数，以'GET'形式出现",
                              type="string"),
                coreapi.Field(name="name", required=True, type="string"),
                coreapi.Field(name="password", required=True, type="boolean")
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_field
