import hashlib

def hash_code(s, salt='myweb'):# 加点盐
    h = hashlib.sha256()
    s = s + salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
