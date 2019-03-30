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
            self.current_step += direction
            self.sequence_id = (self.sequence_id + direction) % self.sequence_count
            time.sleep(self.wait_time)

    def output_sequence(self, sequence_id):
        for i, pin in enumerate(self.stepper_pins):
            GPIO.output(pin, self.sequence[sequence_id][i])

    def __del__(self):
        self.rotate(0)
        for pin in self.stepper_pins:
            GPIO.output(pin, GPIO.LOW)

if __name__ == '__main__':
    print('- motor -')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    motor = Motor()
    while True:
        s = input('rotate round:')
        if s == 'q':break
        r = float(s)
        motor.rotate(r)
