##GPIO pins stuff==========
from time import sleep
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
##End GPIO pins stuff==========

## multithreading stuff
import threading
import time
import json

class MyThread(threading.Thread):
    
    def __init__(self, threadID, name, servo_pin, target_angle):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.servo_pin = servo_pin
      self.target_angle = target_angle

    
    def run(self):
        self.set_servo_angle(self.servo_pin, self.target_angle)
        # self.name.exit() # finish this thread

    def set_servo_angle(self, servo, angle):
        pwm = GPIO.PWM(servo, 50)
        pwm.start(8)
        dutyCycle = angle / 18. + 3.
        pwm.ChangeDutyCycle(dutyCycle)
        sleep(0.3)
        pwm.stop()


class Motor_Module:    
    pass
    # # Servo code =====================================
    # pan = 23 # look for GPIO 23 on raspberry pi pin chart
    # tilt = 22 # look for GPIO 22 on raspberry pi pin chart
    # pan_task_name = "pan_servo_task"
    # tilt_task_name = "tilt_servo_task"
    # pan_task = None
    # tilt_task = None
    # current_threads = []

    # def __init__(self):        
    #     self.initialize_servos()
    
    # def set_servo_angle(self, servo, angle):
    #         pwm = GPIO.PWM(servo, 50)
    #         pwm.start(8)
    #         dutyCycle = angle / 18. + 3.
    #         pwm.ChangeDutyCycle(dutyCycle)
    #         sleep(0.3)
    #         pwm.stop()

    # def debug_servo_positions(self):
    #     self.set_servo_angle(self.tilt, 50) #default head position
    #     self.set_servo_angle(self.pan, 70) #default head position
    #     sleep(1.5)

    #     self.set_servo_angle(self.pan, 190) #look left
    #     sleep(0.5)
    #     self.set_servo_angle(self.pan, 0) #look right
    #     sleep(0.5)
    #     self.set_servo_angle(self.pan, 70) #default head position
    #     sleep(1.0)

    #     self.set_servo_angle(self.tilt, -20) #look up
    #     sleep(0.5)
    #     self.set_servo_angle(self.tilt, 160) #look down
    #     sleep(0.5)
    #     self.set_servo_angle(self.tilt, 50) #default head position
    #     sleep(1.0)    

    # def initialize_servos(self): 
    #     print("initializing servos")   
    #     GPIO.setup(self.tilt, GPIO.OUT) # white => TILT
    #     GPIO.setup(self.pan, GPIO.OUT) # gray ==> PAN           

    # def manual_move_servos(self, json_obj):
    #     self.set_servo_angle(self.pan, json_obj['x'])
    #     self.set_servo_angle(self.tilt, json_obj['y'])

    # def process_ingress_data(self, json_obj):
    #     print("data: " + json.dumps(json_obj))        
    #     self.ensure_remove_tasks_done()
    #     self.ensure_only_move_servos_when_both_are_done(json_obj)           

    # def ensure_remove_tasks_done(self):
    #     for t in self.current_threads:
    #         if not t.is_alive():
    #             # get results from thread
    #             t.handled = True
    #     # update current_threads list with only threads that are still alive
    #     self.current_threads = [t for t in self.current_threads if not t.handled]
    #     print('current_threads: ')
    #     print(self.current_threads)

    # def ensure_only_move_servos_when_both_are_done(self, ingress_data):        
    #     self.pan_task = MyThread(0, self.pan_task_name, self.pan, ingress_data['servoPan'])
    #     self.current_threads.append(self.pan_task)
    #     self.pan_task.start()        
        
    #     self.tilt_task = MyThread(1, self.tilt_task_name, self.tilt, ingress_data['servoNod'])
    #     self.current_threads.append(self.tilt_task) 
    #     self.tilt_task.start()
    

# END servo code =====================================

