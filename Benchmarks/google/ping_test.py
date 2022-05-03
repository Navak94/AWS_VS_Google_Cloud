import subprocess
import time
def ping_test(request):
    request_json = request.get_json()
    hostname = request_json['hostname']
    pre= time.time()
    result = subprocess.check_output(f'ping -c 2 {hostname} | sed -n 7p ', shell=True);
    post= time.time()
    delta = post-pre

    json_dict={
        "hostname":hostname,
        "result": result,
        "delta": delta
    }
    if request_json and 'hostname' in request_json:
        return f'{json_dict}'
    else:
        return f'Host Unavailable.'