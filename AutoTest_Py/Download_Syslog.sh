#!/bin/sh

#��������

function Download_Syslog()
{	
#$1=AutoTest_SYSLOG1;

        echo "******************************************* start the test_download_syslog************************************************" 
        
		echo "******************************************* ����ҳ����http://ip/download_log************************************************"
	
		wget --http-user=$USER --http-password=$PASS $1
		if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
		
		sleep 5
		
	    ChangesyslogFormat "syslog";
		
}


function ChangesyslogFormat {

#$1=syslog	

    	###��ȡ����syslogʱ��
    	GetCurrTime;
    	
    	###�޸�syslog����Ϊ.tgz��ʽ
    	for i in `ls download_log*`
    	do		
    		mv $i $1_$CurrTime.tgz
    	done
    
    	###����syslog��Backup�ļ���
    	cp $(find $CONFIG_PATH -name "*.tgz") $CONFIG_PATH/Backup/Syslog	
    	
    	###��������ļ�###
    	rm -fr *tgz
    
}




