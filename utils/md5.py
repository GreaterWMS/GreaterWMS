import datetime

class Md5(object):
    def md5(s):
        import hashlib
        ctime = str(datetime.datetime.now())
        m = hashlib.md5(bytes(s, encoding="utf-8"))
        m.update(bytes(ctime, encoding="utf-8"))
        return m.hexdigest()