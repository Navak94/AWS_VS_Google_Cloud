import json
import hmac
import hashlib 
import time
def hash_test(event, context):
    pt = event['plain_text']
    pt = pt.encode()
    key= "575049206973206120574950"
    
    pre= time.time_ns()
    cipher_text = hmac.new(key.encode(), pt, digestmod=hashlib.sha256).digest()
    hashed = cipher_text.hex()
    post = time.time_ns()
    delta = post - pre


    json_dict={
        "Delta": delta,
        "hashed": hashed
    }
    
    return {
        'statusCode':200,
        'body': json.dumps(json_dict)
    }