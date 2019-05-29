import RPi.GPIO as gpio
import time

def init():

	gpio.setmode(gpio.BCM)

	gpio.setup(6,gpio.OUT)
	gpio.setup(13,gpio.OUT)
	gpio.setup(19,gpio.OUT)
	gpio.setup(26,gpio.OUT)

	gpio.setup(9,gpio.OUT)
	gpio.setup(11,gpio.IN)
	

def Forward():
	init()
	gpio.output(6,gpio.LOW)
	gpio.output(13,gpio.HIGH)
	gpio.output(19,gpio.LOW)
	gpio.output(26,gpio.HIGH)
	# time.sleep(t)
	gpio.cleanup()



def Backward():
	init()
	gpio.output(6,gpio.HIGH)
	gpio.output(13,gpio.LOW)
	gpio.output(19,gpio.HIGH)
	gpio.output(26,gpio.LOW)
	# time.sleep(t)
	gpio.cleanup()

def Detenerse():

	gpio.output(6,gpio.LOW)
	gpio.output(13,gpio.LOW)
	gpio.output(19,gpio.LOW)
	gpio.output(26,gpio.LOW)


def Distancia():
	while True:
		gpio.output(9,gpio.LOW)
		time.sleep(0.5)
		gpio.output(9,gpio.HIGH)
		time.sleep(0.0001)
		gpio.output(9,gpio.LOW)
		inicio= time.time()
		while gpio.input(11) ==0:
			inicio=time.time()
		while gpio.input(11) == 1:
			final= time.time()
		distancia= ((final-inicio)*34000)/2
		print return distancia

	

if Distancia() < 10:
	Detenerse()
else:
	Forward()


