import random
import time
def math_test(request):
    request_json = request.get_json()
    i = request_json['seed']
    i = int(i)
    pre = time.time_ns()
    a = 5 * i
    b = 4 **i
    c = 3 * i
    d = 2 **i

    slope = (b-a)/(d-c)
    post = time.time_ns()
    delta = post - pre

    json_dict = {
        "slope":slope,
        "delta":delta
    }
    if request_json and 'seed' in request_json:
        return f'{json_dict}'
    else:
        return f'error'
