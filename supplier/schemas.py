import coreapi
from rest_framework.schemas import AutoSchema

class APISchema(AutoSchema):
    def get_manual_fields(self, path, method):
        extra_field = []
        if method.lower() in ['get']:
            extra_field = [
                coreapi.Field(name="openid",
                              location="query",
                              required=True,
                              description="openid是发送请求必须的一个参数，以'GET'形式出现",
                              type="string"),
                coreapi.Field(name="max_page",
                              location="query",
                              required=False,
                              description="每页显示几条",
                              type="string"),
                coreapi.Field(name="page",
                              location="query",
                              required=False,
                              description="哪一页",
                              type="string"),
                coreapi.Field(name="name",
                              location="query",
                              required=False,
                              description="显示某个商品的数据",
                              type="string"),
                coreapi.Field(name="create_name",
                              location="query",
                              required=False,
                              description="该条数据是由谁创建的",
                              type="string"),
                coreapi.Field(name="sort",
                              location="query",
                              required=False,
                              description="排序",
                              type="string"),
            ]
        elif method.lower() in ['post']:
            extra_field = [
                coreapi.Field(name="openid",
                              location="query",
                              required=True,
                              description="openid是发送请求必须的一个参数，以'GET'形式出现",
                              type="string"),
                coreapi.Field('name'),
            ]
        elif method.lower() in ['patch']:
            extra_field = [
                coreapi.Field(name="openid",
                              location="query",
                              required=True,
                              description="openid是发送请求必须的一个参数，以'GET'形式出现",
                              type="string"),
                coreapi.Field('name'),
                coreapi.Field('t_code'),
            ]
        elif method.lower() in ['delete']:
            extra_field = [
                coreapi.Field(name="openid",
                              location="query",
                              required=True,
                              description="openid是发送请求必须的一个参数，以'GET'形式出现",
                              type="string"),
                coreapi.Field('t_code'),
            ]
        manual_fields = super().get_manual_fields(path, method)
        return manual_fields + extra_field
