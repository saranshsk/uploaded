#!/usr/bin/python

import cx_Oracle

def get_dff_validation_data (dff_info_id):
	repo_db_conn = cx_Oracle.connect ( u'METADATA/METADATA@XE' )

	if repo_db_conn:
		print ("Connected to metadata database")
	
	db_validation_sql = "SELECT DFF_INFO_FK, \
    DFF_VALIDATION_PK, \
    DFF_VALIDATION_TYPE, \
    DFF_VALIDATION_PARAMETER,  \
    VALIDATION_CODE_PARAM \
    FROM \
    DFF_VALIDATION A, DFF_INFO B, DFF_VALIDATION_CODES C  \
    WHERE A.CURRENT_IND = 'Y'  \
    AND B.DFF_INFO_PK = A.DFF_INFO_FK \
    AND A.DFF_INFO_FK = :input_dff_info_id \
    AND C.DFF_VALIDATION_FK = A.DFF_VALIDATION_PK"

	db_validation_cursor = repo_db_conn.cursor()
	db_validation_cursor.execute ( db_validation_sql, input_dff_info_id = dff_info_id )
	
	db_validation_rs = []
        for rs in db_validation_cursor:
            d = {}
            d['DFF_INFO_FK'] = rs[0]
            d['DFF_VALIDATION_PK'] = rs[1]
            d['DFF_VALIDATION_TYPE'] = rs[2]
            d['DFF_VALIDATION_PARAMETER'] = rs[3]
            d['VALIDATION_CODE_PARAM'] = rs[4]
            db_validation_rs.append ( d )

	db_validation_cursor.close()
	repo_db_conn.close()
        print ('Function get_dff_validation_data completed successfully')

	return (db_validation_rs)

