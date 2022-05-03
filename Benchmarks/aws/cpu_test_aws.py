import json
import random
import time
def cpu_test(request,context):
    number_of_iterations = request['iterations']
    i=0

    #timestamp
    pre=time.time_ns()

    while i < number_of_iterations:
      i= i+1
    #timestamp

    post=time.time_ns()
    delta=post-pre
    json_dict={
        "iterations":number_of_iterations,
        "delta":delta
    }
    return{
       'statusCode': 200, 
       'body': json.dumps(json_dict)
   }