# from api.models import Users

class Normalpermission(object):
    def has_permission(self, request, view):
        # if Users.objects.filter(user_id=request.user.id, is_delete=0).exists():
        #     vip = Users.objects.get(user_id=request.user.id, is_delete=0).vip
        #     if vip == 0:
        #         return True
        #     else:
        #         return True
        return True

    def has_object_permission(self, request, *args, **kwargs):
        # if Users.objects.filter(user_id=request.user.id, is_delete=0).exists():
        #     vip = Users.objects.get(user_id=request.user.id, is_delete=0).vip
        #     if vip == 0:
        #         return True
        #     else:
        #         return True
        return True
