#!/usr/bin/python

import dff_get_data_from_dff_info
import dff_get_data_from_dff_validation
import dff_get_data_from_dff_validation_codes
import filewatcher
import dff_file_level_validations

def dataingest (DFF_INFO_PK):
    dff_info_rs = dff_get_data_from_dff_info.get_dff_info_data (DFF_INFO_PK)
    print ("The programs has reached the point where it is fetching data from the configuration table : dff_info")
    
    dff_validation_rs = dff_get_data_from_dff_validation.get_dff_validation_data (DFF_INFO_PK)
    print ("The programs has reached the point where it is fetching data from the configuration table : dff_validation")
    
    dff_validation_codes_rs = dff_get_data_from_dff_validation_codes.get_dff_validation_codes_data (DFF_INFO_PK)
    print ("The programs has reached the point where it is fetching data from the configuration table : dff_validation_codes")
    
    for rs in dff_info_rs:
        print (rs)

    for rs in dff_validation_rs:
        print (rs)
        
    for rs in dff_validation_codes_rs:
        print (rs)

    v = filewatcher.filewatcher (dff_info_rs, 0)
    print ("v = ", v)

    dff_file_level_validations.filevalidator (v[0], dff_validation_rs)
