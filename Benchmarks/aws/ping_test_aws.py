import subprocess
import json
def ping_test(event,context):
   
    hostname = event['hostname']
    
    result = subprocess.check_output(f'ping -c 2 {hostname} | sed -n 7p ', shell=True);

    json_dict = {
        "hostname": hostname,
        "result": result
    }
    
    return {
        "statusCode":200,
        "body": json.dumps(json_dict)
    }