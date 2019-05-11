import time
import math
import IMU
import datetime
import os
from LSM9DS0 import *

import smbus
bus = smbus.SMBus(1)



class Submarine():
	def robotInit(self):
		
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG1_XM, 0b01100111)  #z,y,x axis enabled, continuos update,  100Hz data rate
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG2_XM, 0b00100000)  #+/- 16G full scale

		#Initialize the magnetometer
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG5_XM, 0b11110000)  #Temp enable, M data rate = 50Hz
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG6_XM, 0b01100000)  #+/-12gauss
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG7_XM, 0b00000000)  #Continuous-conversion mode

		#initialize the gyroscope
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG1_G, 0b00001111)   #Normal power mode, all axes enabled
		bus.write_byte_data(ACC_ADDRESS,LSM9DS0_CTRL_REG4_G, 0b00110000)   #Continuos update, 2000 dps full scale