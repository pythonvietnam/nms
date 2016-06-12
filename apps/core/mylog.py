#--------------------------------------------------
# @author: Tran Duc Loi 
# @email: loitranduc@gmail.com
# @version: 1.0
# @project: NMS - Jetpjng.com
# @community: Pythonvietnam
#--------------------------------------------------

# mylog for nms
# loitd

import logging
import os.path

def initialize_logger():
	output_dir = os.path.dirname(os.path.abspath(__file__)) #yes, get the current folder

	# disable pika log
	logging.getLogger("pika").propagate = False

	logger = logging.getLogger()
	
	# logger.setLevel(logging.DEBUG)
	 
	# create console handler and set level to info
	# handler = logging.StreamHandler()
	# handler.setLevel(logging.INFO)
	# formatter = logging.Formatter("%(asctime)s [%(threadName)-10s] %(message)s")
	# handler.setFormatter(formatter)
	# logger.addHandler(handler)

	# create error file handler and set level to error
	handler = logging.FileHandler(os.path.join(output_dir, "error.log"),"w", encoding=None, delay="true")
	handler.setLevel(logging.CRITICAL)
	formatter = logging.Formatter("%(asctime)s [%(threadName)-10s] %(message)s")
	handler.setFormatter(formatter)
	logger.addHandler(handler)

	# create debug file handler and set level to debug
	# handler = logging.FileHandler(os.path.join(output_dir, "all.log"),"w")
	# handler.setLevel(logging.DEBUG)
	# formatter = logging.Formatter("%(levelname)s - %(message)s")
	# handler.setFormatter(formatter)
	# logger.addHandler(handler)		

if __name__ == '__main__':
	pass
