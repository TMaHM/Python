#!/bin/sh

### 定义相关工作路径 ###

### 定义相关工作路径 ###
#################循环次数

Control_times=2
####呼叫控制循环次数
#Call_times=2
####基础呼叫控制循环次数
#Basic_Call_times=2
####hold_resume控制循环次数
#Hold_Resume_times=2
####redial_return控制循环次数
#Redial_Return_times=2
####Input_Delete控制循环次数
#Input_Delete_times=2
####Transfer控制循环次数
#Transfer_times=2
####Forward控制循环次数
#Forward_times=2
####Call_Switch控制循环次数
#Call_Switch_times=2
####RingGroup_Paging控制循环次数
#RingGroup_Paging_times=2
####Five_Conference控制循环次数
#Five_Conference_times=2
####Blf_Dial控制循环次数
#Blf_Dial_times=2
####Blf_Function控制循环次数
#Blf_Function_times=2
####CallPark_PickUp控制循环次数
#CallPark_PickUp_times=2
####Three_Conference控制循环次数
#Three_Conference_times=2


####################被测话机####################
#DUT1
HOST1="http://10.10.5.45/"
#DUT2
HOST2="http://10.10.5.17/"
#DUT3
HOST3="http://10.10.5.53/"
#DUT4
HOST4="http://10.10.5.25/"
#DUT5
HOST5="http://10.10.5.39/"


#xmlbrowser的文件地址
XMLBrowser="http://10.3.0.51/test/xmlbrowser/TextMenu.xml"

#xmlbrowserURL设置
XMLBrowserURL=$XMLBrowser$COMMPATH

#SIPServer地址
SIPServer=192.168.0.107

#设置用于CTI接入的户名/密码
USER="admin"
PASS="admin"
COMMPATH="AutoTest&"
SCREENSHOT="download_screen"
SYSLOG="download_log"

#测试URL设置
AutoTest_URL1=$HOST1$COMMPATH
AutoTest_URL2=$HOST2$COMMPATH
AutoTest_URL3=$HOST3$COMMPATH
AutoTest_URL4=$HOST4$COMMPATH
AutoTest_URL5=$HOST5$COMMPATH

#定义URL数组
array_URL=($AutoTest_URL1 $AutoTest_URL2 $AutoTest_URL3 $AutoTest_URL4 $AutoTest_URL5)

#设置用于产品体验室话机的number
#DUT1
AutoTest_Num1=1040
#DUT2
AutoTest_Num2=1043
#DUT3
AutoTest_Num3=1049
#DUT4
AutoTest_Num4=1041
#DUT5
AutoTest_Num5=1042

#定义Num数组
array_Num=($AutoTest_Num1 $AutoTest_Num2 $AutoTest_Num3 $AutoTest_Num4 $AutoTest_Num5)

#DUT4  ring group组名
Ring_Group_Num1=958  

#DUT5  Paging组名
Paging_Num1=970

#产品体验室用
#DUT1
AutoTest_NumPwd1=222222
#DUT2
AutoTest_NumPwd2=222222
#DUT3
AutoTest_NumPwd3=222222
#DUT1
AutoTest_NumPwd4=222222
#DUT2
AutoTest_NumPwd5=222222

#定义pwd数组
array_NumPwd=($AutoTest_NumPwd1 $AutoTest_NumPwd2 $AutoTest_NumPwd3 $AutoTest_NumPwd4 $AutoTest_NumPwd5)

#截图URL设置
AutoTest_SCREENURL1=$HOST1$SCREENSHOT
AutoTest_SCREENURL2=$HOST2$SCREENSHOT
AutoTest_SCREENURL3=$HOST3$SCREENSHOT
AutoTest_SCREENURL4=$HOST4$SCREENSHOT
AutoTest_SCREENURL5=$HOST5$SCREENSHOT

array_SCREENURL=($AutoTest_SCREENURL1 $AutoTest_SCREENURL2 $AutoTest_SCREENURL3 $AutoTest_SCREENURL4 $AutoTest_SCREENURL5)

#下载syslog设置
AutoTest_SYSLOG1=$HOST1$SYSLOG
AutoTest_SYSLOG2=$HOST2$SYSLOG
AutoTest_SYSLOG3=$HOST3$SYSLOG
AutoTest_SYSLOG4=$HOST4$SYSLOG
AutoTest_SYSLOG5=$HOST5$SYSLOG

array_SYSLOG=($AutoTest_SYSLOG1 $AutoTest_SYSLOG2 $AutoTest_SYSLOG3 $AutoTest_SYSLOG4 $AutoTest_SYSLOG5)




#常用变量设置
STIMEVerify=500000	#验证等待时间us
STIME1=2		#按其他键间隔s，一般情况下用
STIME2=3		#通话持续时间s
STIME3=0.3      #连续按键间隔时间
STIME6=3		#接通前等待间隔s
#usleep时间设置
STIME5=500000	#数字键拨号间隔us
STIMEScreen=600000	#截屏延迟时间us
STIMEPW=200000	#同一按键切换间隔us
#截图初始参数设置
ScreenInitialValue=0

#执行话机总数
TotalPhone=3

#话机状态
CALLS_STATE_IDLE=0                #FXSState=0x80 CallCtlState=0x60 LCMState=-1  /* 空闲态 */
CALLS_STATE_OFFHOOK=1     		  #FXSState=0x82 CallCtlState=0x61 LCMState=4   /* Sperker摘机态 */
CALLS_STATE_OUT_GOING=2           #FXSState=0x82 CallCtlState=0x62 LCMState=5   /* Sperker呼出态 */
CALLS_STATE_TALK=3                #FXSState=0x82 CallCtlState=0x64 LCMState=6   /* Sperker基本通话态 */
CALLS_STATE_RING=4                #FXSState=0x80 CallCtlState=0x63 LCMState=3   /* 振铃态 */
CALLS_STATE_HOLD=5                #FXSState=0x82 CallCtlState=0x87 LCMState=7   /* 普通IPPhone Hold对方 */
CALLS_STATE_NS_INITIATE=6         #FXSState=0x82 CallCtlState=0x81 LCMState=11  /* 新业务等待用户拨号态 */
CALLS_STATE_NS_TALK=7         	  #FXSState=0x82 CallCtlState=0x82 LCMState=6   /* 新业务通话态（和其中一方） */
CALLS_STATE_CONFERENCE=8          #FXSState=0x82 CallCtlState=0x88 LCMState=9   /* 会议状态 */
CALLS_STATE_CONF_HOLD=9           #FXSState=0x82 CallCtlState=0x8d LCMState=9   /* 会议HOLD状态 */





######################################################################################################

######################################################################################################
