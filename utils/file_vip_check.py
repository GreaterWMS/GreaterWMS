class FileVipCheck(object):
    def FileVipCheck(file_vip, vip_id):
        if vip_id == 0:
            if file_vip >= 102400:
                return "N"
            else:
                return "Y"
        elif vip_id == 1:
            if file_vip >= 512000:
                return "N"
            else:
                return "Y"
        elif vip_id == 2:
            if file_vip >= 1024000:
                return "N"
            else:
                return "Y"
        elif vip_id == 3:
            if file_vip >= 2048000:
                return "N"
            else:
                return "Y"
        elif vip_id == 9:
            return "Y"
        else:
            return "N"
