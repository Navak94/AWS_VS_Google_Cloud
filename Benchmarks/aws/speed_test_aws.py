import speedtest
import json
import time
def speed_test(event,context):
 
    size = events['data_size']
    pre = time.time()
    test = speedtest.Speedtest()
    dl = test.download()
    ul = test.upload()
    post = time.time()
    delta = post-pre
    if size == "Mbps":
        dl = dl * 0.000001
        ul = ul * 0.000001
    elif size == "mbps":
        dl=dl * 0.0000076294
        ul=ul * 0.0000076294
 
    json_output= {
        "download":dl,
        "upload":ul,
        "size": size,
        "delta":delta
    }

    fix_json = json.dumps(json_output)

    return{
        "statusCode": 200,
        "body": fix_json
    }
