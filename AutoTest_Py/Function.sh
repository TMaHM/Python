#!/bin/sh

##################################################
#                  功能函数区
##################################################

##########################################################验证状态功能函数区##########################################################
#检查FXS状态
function CheckFXSState {

	FXSState=`grep "FXSState" AutoTest\&autoverify\=STATE*`						#取话机回复的200 OK中FXS状态一行
	FXS_State=`echo ${FXSState:5:1}`                         					#取FXS状态行中第六个字符（0 or 1）
	FXS_StateCode=`echo ${FXSState:16:4}`										#取FXS状态码
	if [ "$FXS_State" = "1" ]; then 											#为1则报错
		echo "!!! FXS_State error, FXS_State is ( $FXS_StateCode )."						
	fi		
}
#检查CallCtl状态
function CheckCallCtlState {

	CallCtlState=`grep "CallCtlState" AutoTest\&autoverify\=STATE*`				#取话机回复的200 OK中CallCtl状态一行
	CallCtl_State=`echo ${CallCtlState:9:1}`                        			#取CallCtl状态行中第十个字符（0 or 1）
	CallCtl_StateCode=`echo ${CallCtlState:24:4}`								#取CallCtl状态码
	if [ "$CallCtl_State" = "1" ]; then 										#为1则报错
		echo "!!! CallCtl_State error, CallCtl_State is ( $CallCtl_StateCode )."		
	fi		
}
#检查LCM状态
function CheckLCMState {

	LCMState=`grep "LCMState" AutoTest\&autoverify\=STATE*`						#取话机回复的200 OK中LCM状态一行
	LCM_State=`echo ${LCMState:5:1}`                        					#取LCM状态行中第六个字符（0 or 1）
	LCM_StateCode=`echo ${LCMState:16:2}`										#取LCM状态码
	if [ "$LCM_State" = "1" ]; then 											#为1则报错
		echo "!!! LCM_State error, LCM_State is ( $LCM_StateCode )."		
	fi		
}
#验证状态主函数
function CheckState_Main {
	#echo "***************** Verify State Start *****************";
	usleep $STIMEVerify
	###验证状态URI
	wget --http-user=$USER --http-password=$PASS $1"autoverify=STATE="$2 
	if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
	usleep $STIMEVerify	

	ReturnState=`grep "Return" AutoTest\&autoverify\=STATE*`					#取话机回复的200 OK中Return状态一行
	Return_State=`echo ${ReturnState:8:1}`                         				#取Return状态行中第九个字符（0 or 1）
	
	if [ "$Return_State" = "0" ]; then 											#判断取到的字符为0 or 1
		echo "************************************************************* Verify SUCCESS *************************************************************"
	else
		echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Verify ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		echo "!!! Return state error, state should be ( $2 )."
		
		########状态错误截图功能#########
		ScreenshotURL=`echo ${1%/*}`		
		Screenshot  $4 $ScreenshotURL"/download_screen" "State_Error_Should_Be_$2" 1 $3
		#Download_Syslog $ScreenshotURL"/download_log"
		sleep $STIME1
		
		CheckFXSState  
		CheckCallCtlState 
		CheckLCMState
		rm -fr AutoTest*
		continue
	fi
	rm -fr AutoTest*
	#echo "***************** Verify State End *****************";
}

##########################################################截图功能函数区##########################################################

#截图URI函数，调用时后面需带入参，如：Screenshot $FUNCNAME $SCREENURL1 "CALLS_STATE_IDLE" 10（其中SCREENURL1在Config.sh中设置）
function Screenshot {
	#判断ScreenInitialValue值是否能整除第三入参，为真则执行截图命令
	if [[ ScreenInitialValue%$4 -eq 0 ]]; then
		###截图URI
		
	    exec 1>>$ScreenShot_log_file
	    exec 2>>$ScreenShot_log_file
		
		wget --http-user=$USER --http-password=$PASS $2
		if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi	
		

		
		ChangePictureFormat $1 $3;
		
		exec 1>>$5
		exec 2>>$5
	fi
	
}
#修改截图名称为对应验证状态.bmp
function ChangePictureFormat {

	###获取截图修改时间
	GetCurrTime;
	
	###修改截图名称为bmp格式
	for i in `ls download_screen*`
	do		
		mv $i $1---$2_$CurrTime.bmp
	done

	###拷贝截图文件至Backup文件夹
	cp $(find $CONFIG_PATH -name "*.bmp") $CONFIG_PATH/Backup/Screenshot	
	
	###清除残余文件###
	rm -fr *bmp

}

#获取当前时间
function GetCurrTime {
	
	###获取当前时间
	CurrTime=$(date "+%Y%m%d%H%M%S")
	
}



##########################################################拨号功能函数区##########################################################

#拨号函数，调用时后面需带入参，如：Dial $AutoTest_URL1 $AutoTest_Num2（其中AutoTest_URL1、AutoTest_Num2在Config.sh中设置）
function Dial {
	#usleep $STIMEVerify
	#sleep $STIME3
	Number=$2
	#取Number中5位号码，若有多位号码，可在此处依次添加
	number1=`echo ${Number:0:1}` 
	number2=`echo ${Number:1:1}`
	number3=`echo ${Number:2:1}`
	number4=`echo ${Number:3:1}`
	number5=`echo ${Number:4:1}`
	#usleep $STIME5
	#拨号，若有多位号码，可在此处依次添加
	wget --http-user=$USER --http-password=$PASS $1"keyboard=$number1"
	#if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; ; fi
	sleep $STIME3
	wget --http-user=$USER --http-password=$PASS $1"keyboard=$number2"
	#if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; ; fi
	sleep $STIME3
	wget --http-user=$USER --http-password=$PASS $1"keyboard=$number3"
	#if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; ; fi
	
	#判断第四位号码是否存在
	if [ -n "$number4" ]; then
		sleep $STIME3
		wget --http-user=$USER --http-password=$PASS $1"keyboard=$number4"
		#if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; ; fi
		
		#判断第五位号码是否存在
		if [ -n "$number5" ]; then
			sleep $STIME3
			wget --http-user=$USER --http-password=$PASS $1"keyboard=$number5"
			#if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; ; fi
			usleep $STIMEVerify   
		else
			usleep $STIMEVerify
		fi
	else
		usleep $STIMEVerify
	fi	
}


# ##########################################################拨号功能函数区##########################################################

# #拨号函数，调用时后面需带入参，如：Dial $Num2（其中Num2在Config.sh中设置）
# function Dial {
	
	# Number=$2
	# #取Number中3位号码，若有多位号码，可在此处依次添加
	# number1=`echo ${Number:0:1}` 
	# number2=`echo ${Number:1:1}`
	# number3=`echo ${Number:2:1}`
	# number4=`echo ${Number:3:1}`
	
	# #拨号，若有多位号码，可在此处依次添加
	# wget --http-user=$USER --http-password=$PASS $1"keyboard=$number1"
	# if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
	# usleep $STIME5
	# wget --http-user=$USER --http-password=$PASS $1"keyboard=$number2"
	# if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
	# usleep $STIME5
	# wget --http-user=$USER --http-password=$PASS $1"keyboard=$number3"
	# if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
	# usleep $STIME5
	# wget --http-user=$USER --http-password=$PASS $1"keyboard=$number4"
	# if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi
	# usleep $STIME5

# }

##########################################################获取内存信息功能函数区##########################################################

#获取内存信息
function Get_MemoryFree {
	
	###获取内存URI
	wget --http-user=$USER --http-password=$PASS $1"autoverify=MEMORYFREE"
	if [[ $? -ne 0 ]]; then echo "***************** Command Fail, Please Check.*****************"; continue; fi

	ReturnMemory=`grep "MemoryFree" AutoTest\&autoverify\=MEMORYFREE*`				#取话机回复的200 OK中MemoryFree状态一行
	Return_Memory=`echo ${ReturnMemory:12:27}`                         				#取MemoryFree状态行中第13个字符后共27个字符
	
	echo "************************************************************* $Return_Memory *************************************************************"

	rm -fr AutoTest*
}

function Idle_State_Set {
	wget --http-user=$USER --http-password=$PASS $1"keyboard=F4"
	if [[ $? -ne 0 ]]; then echo "************ Command Fail, Please Check. ************"; continue; fi
	usleep $STIME5
	
	wget --http-user=$USER --http-password=$PASS $1"keyboard=X"
	if [[ $? -ne 0 ]]; then echo "************ Command Fail, Please Check. ************"; continue; fi
	usleep $STIME5

	rm -rf AutoTest*
}

function SoftKey_End_Call {
	wget --http-user=$USER --http-password=$PASS $1"keyboard=F4"   
	if [[ $? -ne 0 ]]; then echo "************ Command Fail, Please Check. ************"; continue; fi
		
}