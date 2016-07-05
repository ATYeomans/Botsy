#!/usr/bin/env python

from neato_driver.neato_driver import Botvac

import time

class Botvactest:
	def __init__(self):
		self.port = "/dev/ttyUSB0"
		self.robot = Botvac(self.port)
		
	def get_data(self):
		self.setBacklight(1)
		time.sleep(0.1)
		buttons = self.robot.getButtons()
		print buttons
		time.sleep(0.1)
		pos = self.robot.getMotors()
		print pos
		time.sleep(0.1)	
		ranges = self.robot.getScanRanges()
		print ranges
		self.setBacklight(0)

if __name__ == "__main__":
	test = Botvactest()
	while True:
		test.get_data()
		time.sleep(1)
		