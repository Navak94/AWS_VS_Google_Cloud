import random
import json
import time
def math_test(event,context):
    i = event['seed']
    i = int(i)
    pre = time.time_ns()
    a = 5 * i
    b = 4 **i
    c = 3 * i
    d = 2 **i

    slope = (b-a)/(d-c)
    post = time.time_ns()
    delta = post - pre
    
    json_dict={
        "slope":slope,
        "delta": delta
    }

    return{
        'statusCode':200,
        'body': json.dumps(json_dict)
    } 
