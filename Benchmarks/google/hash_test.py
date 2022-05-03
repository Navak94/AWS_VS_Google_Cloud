import hmac
import hashlib 
import time
def hash_test(request):
    request_json = request.get_json()
    pt = request_json['plain_text']
    pt = pt.encode()
    key= "575049206973206120574950"

    pre = time.time_ns()
    cipher_text = hmac.new(key.encode(), pt, digestmod=hashlib.sha256).digest()
    hashed = cipher_text.hex()
    post = time.time_ns()
    delta = post - pre

    json_dict = {
        "Delta": delta,
        "Hashed":hashed
    }
    if request_json and 'plain_text' in request_json:
        return f'{json_dict}'
    else:
        return f'error!'
