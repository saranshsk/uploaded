#!/usr/bin/python

from subprocess import Popen, PIPE

def filevalidator (dff_path, dff_validation_rs):
    
    for rs_dict in dff_validation_rs:
	apply_validation ( dff_path, rs_dict['DFF_VALIDATION_TYPE'], rs_dict['DFF_VALIDATION_PARAMETER'], rs_dict['VALIDATION_CODE_PARAM'])

def apply_validation (dff_path, DFF_VALIDATION_TYPE, DFF_VALIDATION_PARAMETER, VALIDATION_CODE_PARAM):
    validation_cmd = VALIDATION_CODE_PARAM
    validation_cmd = validation_cmd.replace('<INP>', dff_path)
    print "Executing the command pre-configured for : ", DFF_VALIDATION_TYPE, validation_cmd
    p = Popen ( validation_cmd, shell = True, stdout = PIPE, stderr = PIPE )
    validation_cmd_result, err = p.communicate()
    print "Execution return code: ", p.returncode
    print validation_cmd_result.rstrip(), err.rstrip()
    if p.returncode == 0:
        print "Command executed for : ", DFF_VALIDATION_TYPE
        print ("Applying check", DFF_VALIDATION_PARAMETER)
        if eval ( validation_cmd_result.rstrip() + ' ' + DFF_VALIDATION_PARAMETER ):
            print (validation_cmd_result.rstrip())
            print "Validation successful"
        else:
            print "Validation failed"

