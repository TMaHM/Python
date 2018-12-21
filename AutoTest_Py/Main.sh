#!/bin/sh

#工作目录
current_dir=`pwd`

#环境变量设置
export CONFIG_PATH="$current_dir"
export log_file="$current_dir/Backup/Syslog.txt"

##各脚本日志
export EndCall_SoftKey_log="$current_dir/Backup/EndCall_SoftKey_log.txt"
export EndCall_Speaker_log="$current_dir/Backup/EndCall_Speaker_log.txt"

export Call_Function_log_file="$current_dir/Backup/Call_Function_Syslog.txt"
export Cancel_A_X_Function_log_file="$current_dir/Backup/Cancel_A_X_Function_Syslog.txt"
export Cancel_B_X_Function_log_file="$current_dir/Backup/Cancel_B_X_Function_Syslog.txt"
export Reject_B_Function_log_file="$current_dir/Backup/Reject_B_Function_Syslog.txt"
export Hold_Resume_A_Function_log_file="$current_dir/Backup/Hold_Resume_A_Function_Syslog.txt"
export Hold_Resume_B_Function_log_file="$current_dir/Backup/Hold_Resume_B_Function_Syslog.txt"
export Redial_Softkey_Function_log_file="$current_dir/Backup/Redial_Softkey_Function_Syslog.txt"
export Redial_Button_Function_log_file="$current_dir/Backup/Redial_Button_Function_Syslog.txt"
export Call_Return_Function_log_file="$current_dir/Backup/Call_Return_Function_Syslog.txt"
export Input_Function_log_file="$current_dir/Backup/Input_Function_Syslog.txt"
export Input_Delete_Function_log_file="$current_dir/Backup/Input_Delete_Function_Syslog.txt"
export Blind_Transfer_Function_log_file="$current_dir/Backup/Blind_Transfer_Function_Syslog.txt"
export Semi_Attend_Transfer_Function_log_file="$current_dir/Backup/Semi_Attend_Transfer_Function_Syslog.txt"
export Attend_Transfer_Function_log_file="$current_dir/Backup/Attend_Transfer_Function_Syslog.txt"
export Attend_C_Reject_Transfer_Function_log_file="$current_dir/Backup/Attend_C_Reject_Transfer_Function_Syslog.txt"
export Semi_Attend_B_Cancel_Transfer_Function_log_file="$current_dir/Backup/Semi_Attend_B_Cancel_Transfer_Function_Syslog.txt"
export Always_Forward_Function_log_file="$current_dir/Backup/Always_Forward_Function_Syslog.txt"
export Busy_Forward_Function_log_file="$current_dir/Backup/Busy_Forward_Function_Syslog.txt"
export No_Answer_Forward_Function_log_file="$current_dir/Backup/No_Answer_Forward_Function_Syslog.txt"
export Button_Forward_Function_log_file="$current_dir/Backup/Button_Forward_Function_Syslog.txt"
export Call_Switch_Linekey_Function_log_file="$current_dir/Backup/Call_Switch_Linekey_Function_Syslog.txt"
export Call_Switch_Button_Function_log_file="$current_dir/Backup/Call_Switch_Button_Function_Syslog.txt"
export Ring_Group_Function_log_file="$current_dir/Backup/Ring_Group_Function_log_file.txt"
export Conference_A_Function_log_file="$current_dir/Backup/Conference_A_Function_Syslog.txt"
export Conference_A_Other_Exit_Function_log_file="$current_dir/Backup/Conference_A_Other_Exit_Function_Syslog.txt"
export Conference_Other_Function_log_file="$current_dir/Backup/Conference_Other_Function_Syslog.txt"
export Conference_Other_Exit_Function_log_file="$current_dir/Backup/Conference_Other_Exit_Function_Syslog.txt"
export Blf_Dial_Function_log_file="$current_dir/Backup/Blf_Dial_Function_Syslog.txt"
export Blf_Blind_Transfer_Function_log_file="$current_dir/Backup/Blf_Blind_Transfer_Function_Syslog.txt"
export Blf_Attend_Transfer_Function_log_file="$current_dir/Backup/Blf_Attend_Transfer_Function_Syslog.txt"
export Call_Park_Function_log_file="$current_dir/Backup/Call_Park_Function_Syslog.txt"
export Call_PickUp_Function_log_file="$current_dir/Backup/Call_PickUp_Function_Syslog.txt"
export Blf_Call_PickUp_Function_log_file="$current_dir/Backup/Blf_Call_PickUp_Function_Syslog.txt"
export Alert_Blf_Call_PickUp_Function_log_file="$current_dir/Backup/Alert_Blf_Call_PickUp_Function_Syslog.txt"
export Three_Conference_A_Function_log_file="$current_dir/Backup/Three_Conference_A_Function_Syslog.txt"

export Paging_Function_log_file="$current_dir/Backup/Paging_Function_Syslog.txt"
#####打印截图函数日志#####
export ScreenShot_log_file="$current_dir/Backup/ScreenShot_log.txt"


######数据定义区引用
source $CONFIG_PATH/Config.sh    		#定义自动化测试的全局变量
source $CONFIG_PATH/Function.sh  		#定义自动化测试的工具函数


# ######测试功能引用--查错函数引用
# source $CONFIG_PATH/Check_Error.sh
######测试功能引用
source $CONFIG_PATH/EndCall_SoftKey.sh 			#定义自动化测试Call脚本函数
source $CONFIG_PATH/EndCall_Speaker.sh

source $CONFIG_PATH/Call.sh
source $CONFIG_PATH/Cancel_A_X.sh 			#定义自动化测试Call脚本函数
source $CONFIG_PATH/Cancel_B_X.sh 			#定义自动化测试Call脚本函数
source $CONFIG_PATH/Reject_B.sh 			#定义自动化测试Call脚本函数
source $CONFIG_PATH/Hold_Resume_A.sh 			#定义自动化测试Call脚本函数
source $CONFIG_PATH/Hold_Resume_B.sh 			#定义自动化测试Call脚本函数
source $CONFIG_PATH/Redial_Softkey.sh
source $CONFIG_PATH/Redial_Button.sh
source $CONFIG_PATH/Call_Return.sh
source $CONFIG_PATH/Input.sh
source $CONFIG_PATH/Input_Delete.sh
source $CONFIG_PATH/Blind_Transfer.sh
source $CONFIG_PATH/Semi_Attend_Transfer.sh
source $CONFIG_PATH/Attend_Transfer.sh
source $CONFIG_PATH/Attend_C_Reject_Transfer.sh
source $CONFIG_PATH/Semi_Attend_B_Cancel_Transfer.sh
source $CONFIG_PATH/Download_Syslog.sh
source $CONFIG_PATH/Always_Forward.sh
source $CONFIG_PATH/No_Answer_Forward.sh
source $CONFIG_PATH/Busy_Forward.sh
source $CONFIG_PATH/Button_Forward.sh
source $CONFIG_PATH/Call_Switch_Linekey.sh
source $CONFIG_PATH/Call_Switch_Button.sh
source $CONFIG_PATH/Ring_Group.sh
source $CONFIG_PATH/Conference_A.sh
source $CONFIG_PATH/Conference_A_Other_Exit.sh
source $CONFIG_PATH/Conference_Other.sh
source $CONFIG_PATH/Conference_Other_Exit.sh
source $CONFIG_PATH/Blf_Dial.sh
source $CONFIG_PATH/Blf_Blind_Transfer.sh
source $CONFIG_PATH/Blf_Attend_Transfer.sh
source $CONFIG_PATH/Call_Park.sh
source $CONFIG_PATH/Call_PickUp.sh
source $CONFIG_PATH/Blf_Call_PickUp.sh
source $CONFIG_PATH/Alert_Blf_Call_PickUp.sh
source $CONFIG_PATH/Paging.sh
source $CONFIG_PATH/Three_Conference_A.sh
## 判断备份文件夹是否存在，不存在则创建
if [ ! -d "$CONFIG_PATH/Backup" ]; then
	mkdir "$CONFIG_PATH/Backup"
fi
## 判断截图文件夹是否存在，不存在则创建
if [ ! -d "$CONFIG_PATH/Backup/Screenshot" ]; then
	mkdir "$CONFIG_PATH/Backup/Screenshot"
fi
## 判断日志文件是否存在，不存在则创建
#if [ ! -f "$log_file" ]; then  
#	touch "$log_file" 
###################################创建各脚本日志文件####################################
###################################创建各脚本日志文件####################################
#fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$EndCall_SoftKey_log" ]; then  
	touch "$EndCall_SoftKey_log" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Call_Function_log_file" ]; then  
	touch "$Call_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$EndCall_Speaker_log" ]; then  
	touch "$EndCall_Speaker_log" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Cancel_A_X_Function_log_file" ]; then  
	touch "$Cancel_A_X_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Cancel_B_X_Function_log_file" ]; then  
	touch "$Cancel_B_X_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Reject_B_Function_log_file" ]; then  
	touch "$Reject_B_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Hold_Resume_A_Function_log_file" ]; then  
	touch "$Hold_Resume_A_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Hold_Resume_B_Function_log_file" ]; then  
	touch "$Hold_Resume_B_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Redial_Softkey_Function_log_file" ]; then  
	touch "$Redial_Softkey_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Redial_Button_Function_log_file" ]; then  
	touch "$Redial_Button_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Call_Return_Function_log_file" ]; then  
	touch "$Call_Return_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Input_Function_log_file" ]; then  
	touch "$Input_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Input_Delete_Function_log_file" ]; then  
	touch "$Input_Delete_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Blind_Transfer_Function_log_file" ]; then  
	touch "$Blind_Transfer_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Semi_Attend_Transfer_Function_log_file" ]; then  
	touch "$Semi_Attend_Transfer_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Attend_Transfer_Function_log_file" ]; then  
	touch "$Attend_Transfer_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Attend_C_Reject_Transfer_Function_log_file" ]; then  
	touch "$Attend_C_Reject_Transfer_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Semi_Attend_B_Cancel_Transfer_Function_log_file" ]; then  
	touch "$Semi_Attend_B_Cancel_Transfer_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Always_Forward_Function_log_file" ]; then  
	touch "$Always_Forward_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$No_Answer_Forward_Function_log_file" ]; then  
	touch "$No_Answer_Forward_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Busy_Forward_Function_log_file" ]; then  
	touch "$Busy_Forward_Function_log_file" 
fi  
## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Button_Forward_Function_log_file" ]; then  
	touch "$Button_Forward_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Call_Switch_Linekey_Function_log_file" ]; then  
	touch "$Call_Switch_Linekey_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Call_Switch_Button_Function_log_file" ]; then  
	touch "$Call_Switch_Button_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Ring_Group_Function_log_file" ]; then  
	touch "$Ring_Group_Function_log_file" 
fi
## 判断记录截图函数的日志是否存在，不存在则创建
if [ ! -f "$ScreenShot_log_file" ]; then  
	touch "$ScreenShot_log_file" 
fi

if [ ! -f "$Conference_A_Function_log_file" ]; then  
	touch "$Conference_A_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Conference_A_Other_Exit_Function_log_file" ]; then  
	touch "$Conference_A_Other_Exit_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Conference_Other_Function_log_file" ]; then  
	touch "$Conference_Other_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Conference_Other_Exit_Function_log_file" ]; then  
	touch "$Conference_Other_Exit_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Blf_Dial_Function_log_file" ]; then  
	touch "$Blf_Dial_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Blf_Blind_Transfer_Function_log_file" ]; then  
	touch "$Blf_Blind_Transfer_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Blf_Attend_Transfer_Function_log_file" ]; then  
	touch "$Blf_Attend_Transfer_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Call_Park_Function_log_file" ]; then  
	touch "$Call_Park_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Call_PickUp_Function_log_file" ]; then  
	touch "$Call_PickUp_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Blf_Call_PickUp_Function_log_file" ]; then  
	touch "$Blf_Call_PickUp_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Alert_Blf_Call_PickUp_Function_log_file" ]; then  
	touch "$Alert_Blf_Call_PickUp_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Paging_Function_log_file" ]; then  
	touch "$Paging_Function_log_file" 
fi

## 判断日志文件是否存在，不存在则创建
if [ ! -f "$Three_Conference_A_Function_log_file" ]; then  
	touch "$Three_Conference_A_Function_log_file" 
fi

# ###################################创建查错脚本的日志文件####################################
# ###################################创建查错脚本的日志文件####################################
 if [ ! -f "$Check_Error_Function_log_file" ]; then  
	 touch "$Check_Error_Function_log_file" 
 fi

###修改文件属性, 修改为777
chmod -R 777 $CONFIG_PATH

## 清空各个脚本日志文件内容
cat /dev/null > $log_file
cat /dev/null > $EndCall_SoftKey_log
cat /dev/null > $EndCall_Speaker_log

cat /dev/null > $Call_Function_log_file
cat /dev/null > $Cancel_A_X_Function_log_file
cat /dev/null > $Cancel_B_X_Function_log_file
cat /dev/null > $Reject_B_Function_log_file
cat /dev/null > $Hold_Resume_A_Function_log_file
cat /dev/null > $Hold_Resume_B_Function_log_file
cat /dev/null > $Redial_Softkey_Function_log_file
cat /dev/null > $Redial_Button_Function_log_file
cat /dev/null > $Call_Return_Function_log_file
cat /dev/null > $Input_Function_log_file
cat /dev/null > $Input_Delete_Function_log_file
cat /dev/null > $Blind_Transfer_Function_log_file
cat /dev/null > $Semi_Attend_Transfer_Function_log_file
cat /dev/null > $Attend_Transfer_Function_log_file
cat /dev/null > $Attend_C_Reject_Transfer_Function_log_file
cat /dev/null > $Semi_Attend_B_Cancel_Transfer_Function_log_file
cat /dev/null > $Always_Forward_Function_log_file
cat /dev/null > $Busy_Forward_Function_log_file
cat /dev/null > $No_Answer_Forward_Function_log_file
cat /dev/null > $Button_Forward_Function_log_file
cat /dev/null > $Call_Switch_Linekey_Function_log_file
cat /dev/null > $Call_Switch_Button_Function_log_file
cat /dev/null > $Ring_Group_Function_log_file
cat /dev/null > $Conference_A_Function_log_file
cat /dev/null > $Conference_A_Other_Exit_Function_log_file
cat /dev/null > $Conference_Other_Function_log_file
cat /dev/null > $Conference_Other_Exit_Function_log_file
cat /dev/null > $Blf_Dial_Function_log_file
cat /dev/null > $Blf_Blind_Transfer_Function_log_file
cat /dev/null > $Blf_Attend_Transfer_Function_log_file
cat /dev/null > $Call_Park_Function_log_file
cat /dev/null > $Call_PickUp_Function_log_file
cat /dev/null > $Blf_Call_PickUp_Function_log_file
cat /dev/null > $Alert_Blf_Call_PickUp_Function_log_file
cat /dev/null > $Paging_Function_log_file
cat /dev/null > $Three_Conference_A_Function_log_file
#####记录截图函数打印信息#####
cat /dev/null > $ScreenShot_log_file
# ## 清空查错日志文件内容
# cat /dev/null > $Check_Error_Function_log_file

## 清空截图和下载syslog
rm -fr /$CONFIG_PATH/Backup/Screenshot/*bmp
rm -fr /$CONFIG_PATH/Backup/Syslog/*tgz
#记录正确及错误信息到日志文件
exec 1>>$log_file
exec 2>>$log_file

###清除脚本中断后的残余文件###
rm -fr AutoTest*
rm -fr download_screen*
rm -fr *bmp
rm -fr TextMenu*


###############################开始测试####################################
###############################开始测试####################################
echo "************************************************************* AutoTest Start *************************************************************"
 
 for((j=0;j<5;j++))   #控制执行次数
	do
	    echo "20台话机"
	    if [ $1 = "EndCall_SoftKey" ]; then
	  	  echo "Auto Test EndCall_SoftKey Function!!!"
	  	  EndCall_SoftKey_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "EndCall_Speaker" ]; then
	  	  echo "Auto Test DND Function!!!"
	  	  EndCall_Speaker_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "CANCEL_A_X" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	  Cancel_A_X_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "CANCEL_B_X" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	  Cancel_B_X_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "REJECT_B" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	  Reject_B_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "HOLD_RESUME_A" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	  Hold_Resume_A_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "HOLD_RESUME_B" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	  Hold_Resume_B_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "REDIAL_SOFTKEY" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	  Redial_Softkey_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
		  
		echo "20台话机"
		elif [ $1 = "CALL" ]; then
	  	  echo "Auto Test DND Function!!!"
	  	  Call_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif [ $1 = "REDIAL_BUTTON" ]; then
	  	  echo "Auto Test Hold Resume Function!!!"
	  	 Redial_Button_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ; 
        elif [ $1 = "CALL_RETURN" ]; then
		  echo "Auto Test Hold Resume Function!!!"
		  Call_Return_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
        elif [ $1 = "INPUT" ]; then
		  echo "Auto Test Hold Resume Function!!!"
		  Input_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;	
        elif [ $1 = "INPUT_DELETE" ]; then
		  echo "Auto Test Hold Resume Function!!!"
		  Input_Delete_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
	    elif 	[ $1 = "BLIND_TRANSFER" ]; then
		      echo "Auto Test Hold Resume Function!!!"
		  	  Blind_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
	    elif 	[ $1 = "SEMI_ATTEND_TRANSFER" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			 Semi_Attend_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
	    elif 	[ $1 = "ATTEND_TRANSFER" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Attend_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			  
		################################################40台话机################################################	  
		################################################40台话机################################################
		
		echo "20台话机"	  
	    elif 	[ $1 = "ATTEND_C_REJECT_TRANSFER" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Attend_C_Reject_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
		elif 	[ $1 = "SEMI_ATTEND_B_CANCEL_TRANSFER" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			 Semi_Attend_B_Cancel_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	 
        elif 	[ $1 = "ALWAYS_FORWARD" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			 Always_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	 
        elif 	[ $1 = "NO_ANSWER_FORWARD" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  No_Answer_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};  
		elif 	[ $1 = "BUSY_FORWARD" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Busy_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};		  
		elif 	[ $1 = "BUTTON_FORWARD" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Button_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	  	  
		elif 	[ $1 = "CALL_SWITCH_LINEKEY" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Call_Switch_Linekey_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};		
        elif 	[ $1 = "CALL_SWITCH_BUTTON" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Call_Switch_Button_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};			  
		elif 	[ $1 = "RING_GROUP" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Ring_Group_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${Ring_Group_Num2};	 
		#elif 	[ $1 = "CONFERENCE_A" ]; then
			#  echo "Auto Test Hold Resume Function!!!"
			#  Conference_A_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} #${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} #${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} #${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};	
		#elif 	[ $1 = "CONFERENCE_A_OTHER_EXIT" ]; then
		#	  echo "Auto Test Hold Resume Function!!!"
		#	 Conference_A_Other_Exit_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} #${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} #${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} #${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};	
		# elif 	[ $1 = "CONFERENCE_OTHER" ]; then
			#  echo "Auto Test Hold Resume Function!!!"
			 # Conference_Other_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} #${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} #${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} #${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};		
			  
        ################################################40台话机################################################	  
		################################################40台话机################################################
       # elif 	[ $1 = "CONFERENCE_OTHER_EXIT" ]; then
			#  echo "Auto Test Hold Resume Function!!!"
			 # Conference_Other_Exit_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} #${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} #${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} #${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};
		
		elif 	[ $1 = "BLF_DIAL" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Blf_Dial_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]};
        elif 	[ $1 = "BLF_BLIND_TRANSFER" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Blf_Blind_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
        elif 	[ $1 = "BLF_ATTEND_TRANSFER" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Blf_Attend_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
		elif 	[ $1 = "CALL_PARK" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Call_Park_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
        elif 	[ $1 = "CALL_PICKUP" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Call_PickUp_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
        elif 	[ $1 = "BLF_CALL_PICKUP" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Blf_Call_PickUp_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
        			  
        elif 	[ $1 = "ALERT_BLF_CALL_PICKUP" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Alert_Blf_Call_PickUp_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};

        elif 	[ $1 = "THREE_CONFERENCE_A" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Three_Conference_A_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	






			  
			  
        elif 	[ $1 = "PAGING" ]; then
			  echo "Auto Test Hold Resume Function!!!"
			  Paging_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${Paging_Num1};
		
        elif 	[ $1 = "DOWNLOAD_SYSLOG" ]; then
	          echo "Auto Test Hold Resume Function!!!"
	          download_syslog ${array_SYSLOG[0]};	  
			  
	    elif 	[ $1 = "CHECKERROR" ]; then
	          echo "Auto Test Check_Error Function!!!"
	          Check_Error_Function;  		  
			  
		elif [ $1 = "ALL" ]; then
		    
			EndCall_SoftKey_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			EndCall_Speaker_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			
			Cancel_A_X_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Cancel_B_X_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Reject_B_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Hold_Resume_A_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Hold_Resume_B_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Redial_Softkey_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Call_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Redial_Button_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Call_Return_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
			Input_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;	
			Input_Delete_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ;
            Blind_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Semi_Attend_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Attend_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			
			
			Attend_C_Reject_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Semi_Attend_B_Cancel_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
            #Always_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
			#No_Answer_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};  
			#Busy_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
			#Button_Forward_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Call_Switch_Linekey_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
			Call_Switch_Button_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
           # Ring_Group_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${Ring_Group_Num2};		
            #Paging_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${Paging_Num1};
            Conference_A_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} ${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};	
		    Conference_A_Other_Exit_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} ${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};
			Conference_Other_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} ${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};
			Conference_Other_Exit_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]} ${array_URL[3]} ${array_Num[3]} ${array_SCREENURL[3]} ${array_URL[4]} ${array_Num[4]} ${array_SCREENURL[4]};
			Blf_Dial_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]};
			Blf_Blind_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Blf_Attend_Transfer_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Call_Park_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
			Call_PickUp_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Blf_Call_PickUp_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
			Alert_Blf_Call_PickUp_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};	
			Three_Conference_A_Function ${array_URL[0]} ${array_URL[1]} ${array_Num[0]} ${array_Num[1]} ${array_SCREENURL[0]} ${array_SCREENURL[1]} ${array_URL[2]} ${array_Num[2]} ${array_SCREENURL[2]};
		else
			echo "Please make sure the positon variable is valide.!!!"
		fi
	done
###############################结束测试####################################
###############################结束测试####################################

###清除残余文件###
rm -fr AutoTest*
rm -fr *bmp
rm -fr TextMenu*

echo "************************************************************* AutoTest End *************************************************************"


