#!/usr/bin/python

import glob
import time

def filewatcher (dff_info_rs, rs_index):
	# following inputs needed -
	# dff_type
	# dff_name
	# connection_info
	# poll_interval
	# poll_count
	rs_dict = dff_info_rs[rs_index]
	dff=[]

	for iteration_count in range(0, rs_dict['dff_poll_count']):
		print ("Iteration %d: looking for %s/%s") % (iteration_count, rs_dict['dff_connection_info'], rs_dict['dff_name'])
		dff = glob.glob (rs_dict['dff_connection_info'] + '/' + rs_dict['dff_name'])
		if dff:
			print ("found file: ", dff)
			break
		else:
			print ("file not found, sleeping for %d seconds" % rs_dict['DFF_poll_interval'])
		time.sleep (rs_dict['DFF_poll_interval'])
	return dff

