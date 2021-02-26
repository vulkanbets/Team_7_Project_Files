#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import pigpio

pi = pigpio.pi()
pi.hardware_PWM(12, 800, 10000)   # <---- Research this more to understand better


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

while True:
    GPIO.output(29,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(29,GPIO.LOW)
    GPIO.output(31,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(31,GPIO.LOW)
    GPIO.output(37,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(37,GPIO.LOW)
    GPIO.output(36,GPIO.HIGH)
    time.sleep(0.10)
    GPIO.output(36,GPIO.LOW)
    