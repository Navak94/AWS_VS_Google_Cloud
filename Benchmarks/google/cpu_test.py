import random
import time
def cpu_test(request):
    request_json = request.get_json()
    number_of_iterations = request_json['iterations']
    i=0

    #timestamp
    pre=time.time_ns()

    while i < number_of_iterations:
      i= i+1
    #timestamp

    post=time.time_ns()
    delta=post-pre

    if request_json and 'iterations' in request_json:
        return f'{delta}'
    else:
        return f'error'