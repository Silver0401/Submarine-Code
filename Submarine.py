import RPi.GPIO as gpio
import time

def init():

	gpio.setmode(gpio.BCM)

	gpio.setup(6,gpio.OUT)
	gpio.setup(13,gpio.OUT)
	gpio.setup(19,gpio.OUT)
	gpio.setup(26,gpio.OUT)
	

def Forward():
	init()
	gpio.output(6,gpio.LOW)
	gpio.output(13,gpio.LOW)
	gpio.output(19,gpio.HIGH)
	gpio.output(26,gpio.HIGH)
	gpio.cleanup()



def Backward():
	init()
	gpio.output(6,gpio.LOW)
	gpio.output(13,gpio.LOW)
	gpio.output(19,gpio.HIGH)
	gpio.output(26,gpio.HIGH)
	gpio.cleanup()

Forward()

