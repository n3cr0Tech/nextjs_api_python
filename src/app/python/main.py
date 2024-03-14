import sys, getopt
import json
from datetime import datetime
from motor_module import Motor_Module

def main():            
    motor_module = Motor_Module()  
    json_obj = json.loads(sys.argv[1])    
    print("args that python received: {}".format(sys.argv))        
    print('param1: ' + str(json_obj['testData']))
    # print('param2: ' + json_obj['servoNod'])
    # motor_module.process_ingress_data(json_obj)
    print("moved motor ts: {}".format(datetime.now()))

if __name__ == "__main__":
    sys.exit(main())