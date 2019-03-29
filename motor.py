import sys
import time
import RPi.GPIO as GPIO

class Motor():
    def __init__(self):
        self.stepper_pins = [17, 18, 27, 22]
        self.sequence = [[1,0,0,0],
                        [1,1,0,0],
                        [0,1,0,0],
                        [0,1,1,0],
                        [0,0,1,0],
                        [0,0,1,1],
                        [0,0,0,1],
                        [1,0,0,1]]

        self.steps_per_revolution = 64 * 64
        self.sequence_count = len(self.sequence)
        self.current_step = 0
        self.sequence_id = 0
        self.wait_time = 0.001
        
        GPIO.setmode(GPIO.BCM)
        for pin in self.stepper_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
    
    def reset(self):
        self.rotate(0)

    def rotate(self, round):
        target_step = int(round * self.steps_per_revolution)
        direction = 1 if target_step > self.current_step else -1

        while (self.current_step != target_step):
            self.output_sequence(self.sequence_id)
            current_step += direction
            self.sequence_id = (self.sequence_id + direction) % self.sequence_count
            time.sleep(self.wait_time)

    def output_sequence(self, sequence_id):
        for i, pin in enumerate(self.stepper_pins):
            GPIO.output(pin, self.sequence[sequence_id][i])

if __name__ == '__main__':
    print('- motor -')
    motor = Motor()
    motor.rotate(1/4)