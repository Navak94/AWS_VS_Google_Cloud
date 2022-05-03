import speedtest
import json
import time
def speed_test(request):
    request_json = request.get_json()
    size = request_json['data_size']
    pre = time.time()
    test = speedtest.Speedtest()
    dl = test.download()
    ul = test.upload()
    post = time.time()
    delta = post - pre

    if size == "Mbps":
        dl = dl * 0.000001
        ul = ul * 0.000001
    elif size == "mbps":
        dl=dl * 0.0000076294
        ul=ul * 0.0000076294
    else: 
        return f'error'    
    json_output= {
        "download":dl,
        "upload":ul,
        "size": size,
        "delta": delta
    }

    fix_json = json.dumps(json_output)

    if request_json and 'data_size' in request_json:
         return fix_json
    else:
        return f'error'
