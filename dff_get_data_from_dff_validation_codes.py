#!/usr/bin/python

import cx_Oracle

def get_dff_validation_codes_data (dff_info_id):
	repo_db_conn = cx_Oracle.connect ( u'assist_db/assist_db@XE' )

	if repo_db_conn:
		print ("connected to repository")
	
	db_validation_codes_sql = u'select dff_validation_pk, dff_info_id, validation_type, validation_param from dff_validation where dff_info_id = :input_dff_info_id'

	db_validation_codes_cursor = repo_db_conn.cursor()
	db_validation_codes_cursor.execute ( db_validation_codes_sql, input_dff_info_id = dff_info_id )

	db_validation_codes_rs = []
	for rs in db_validation_codes_cursor:
		d = {}
		d['dff_validation_pk'] = rs[0]
		d['dff_validation_id'] = rs[1]
		d['validation_type'] = rs[2]
		d['validation_param'] = rs[3]
		db_validation_codes_rs.append ( d )

	db_validation_codes_cursor.close()
	repo_db_conn.close()
        print ('completed')

	return (db_validation_codes_rs)

