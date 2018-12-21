#!/bin/sh

#基本呼叫

function Download_Syslog()
{	
#$1=AutoTest_SYSLOG1;

        echo "******************************************* start the test_download_syslog************************************************" 
        
		echo "******************************************* 在网页输入http://ip/download_log************************************************"
	
		wget --http-user=$USER --http-password=$PASS $1
		if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
		
		sleep 5
		
	    ChangesyslogFormat "syslog";
		
}


function ChangesyslogFormat {

#$1=syslog	

    	###获取下载syslog时间
    	GetCurrTime;
    	
    	###修改syslog名称为.tgz格式
    	for i in `ls download_log*`
    	do		
    		mv $i $1_$CurrTime.tgz
    	done
    
    	###拷贝syslog至Backup文件夹
    	cp $(find $CONFIG_PATH -name "*.tgz") $CONFIG_PATH/Backup/Syslog	
    	
    	###清除残余文件###
    	rm -fr *tgz
    
}




