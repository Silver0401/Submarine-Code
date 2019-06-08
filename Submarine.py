import RPi.GPIO as gpio
import time
import picamera
import os
import subprocess

def init():

	gpio.setmode(gpio.BCM)

	gpio.setup(6,gpio.OUT)
	gpio.setup(13,gpio.OUT)
	gpio.setup(19,gpio.OUT)
	gpio.setup(26,gpio.OUT)

	gpio.setup(9,gpio.OUT)
	gpio.setup(11,gpio.IN)

	gpio.setup(27,gpio.IN)

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
	init()

	gpio.output(6,gpio.LOW)
	gpio.output(13,gpio.LOW)
	gpio.output(19,gpio.LOW)
	gpio.output(26,gpio.LOW)


def Distancia():
	init()
	final = 0
	inicio = 0
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
		return distancia


def Video_Recording(video_name):
	camera = picamera.PiCamera()
	camera.start_recording(video_name +".h264")
	time.sleep(5)
	camera.stop_recording()

def Live_Video():
	camera = picamera.PiCamera()
	
	os.system("raspivid -o - -t 0 -vf -hf -w 600 -h 600 -fps 30 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264")
	# camera.start_preview()
	# time.sleep(10)
	# camera.stop_preview()


def Take_Photo(photo_name):
	camera = picamera.PiCamera()
	camera.capture(photo_name + ".jpg")


Take_Photo("foto_test")
	
# while True:
# 	print Distancia()
# 	if Distancia() > 10 and Distancia() < 2000:
# 		Forward()
# 	else:
# 		Detenerse()


#holo
