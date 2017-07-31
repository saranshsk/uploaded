#!/usr/bin/python

import cx_Oracle

def get_dff_info_data (dff_info_id):
	repo_db_conn = cx_Oracle.connect ( u'metadata/METADATA@XE' )

	if repo_db_conn:
		print ("Connected to metadata database")
	
	db_info_sql = u"SELECT DFF_INFO_PK,    \
    DFF_TYPE,\
    DFF_NAME,   \
    DFF_SYSTEM, \
    DFF_INFO, \
    DFF_CONNECTION_INFO, \
    DFF_FILE_DELIM,  \
    DFF_CONTAINS_HEADER,   \
    DFF_CONTAINS_TRAILER, \
    DFF_LINES_TO_SKIP, \
    DFF_POLL_INTERVAL, \
    DFF_POLL_COUNT FROM  \
    DFF_INFO WHERE \
    CURRENT_IND = 'Y' \
    AND DFF_INFO_PK = :input_dff_info_id"

	db_info_cursor = repo_db_conn.cursor()
	db_info_cursor.execute ( db_info_sql, input_dff_info_id = dff_info_id )

	db_info_rs = []
	for rs in db_info_cursor:
		d = {}
		d['dff_info_pk'] = rs[0]
		d['dff_type'] = rs[1]
		d['dff_name'] = rs[2]
		d['dff_system'] = rs[3]
		d['dff_info'] = rs[4]
		d['dff_connection_info'] = rs[5]
		d['dff_file_delim'] = rs[6]
		d['dff_contains_header'] = rs[7]
		d['dff_contains_trailer'] = rs[8]
		d['dff_lines_to_skip'] = rs[9]
		d['dff_poll_interval'] = rs[10]
		d['dff_poll_count'] = rs[11]
		db_info_rs.append ( d )

	
	db_info_cursor.close()
	repo_db_conn.close()
        print ('Function get_dff_info_data completed successfully')

	return (db_info_rs)

