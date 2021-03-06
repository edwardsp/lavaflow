# Copyright 2011 David Irvine
# 
# This file is part of LavaFlow
#
# LavaFlow is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at 
# your option) any later version.
#
# LavaFlow is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License 
# along with LavaFlow.  If not, see <http://www.gnu.org/licenses/>.
#
# $Rev: 158 $:   
# $Author: irvined $: 
# $Date: 2012-10-31 23:42:17 +0100 (Wed, 31 Oct 2012) $:  
#


TERMINFO={
		"-1":{
			"name":"TERM_UNTERMINATED",
			"desc":"Job was not terminaed",
			"number":-1,
			},
		"0":{
			"name":"TERM_UNKNOWN",
			"desc":"LSF cannot determine a termination reason.0 is logged but TERM_UNKNOWN is not displayed (0)			",
			"number":0,
			},
		"1":{
			"name":"TERM_PREEMPT",
			"desc":"Job killed after preemption (1)",
			"number":1,
			},
		"2":{
			"name":"TERM_WINDOW",
			"desc":"Job killed after queue run window closed (2)",
			"number":2,
			},
		"3":{
			"name":"TERM_LOAD",
			"desc":"Job killed after load exceeds threshold (3)",
			"number":3,
			},
		"4":{
			"name":"TERM_OTHER",
			"desc":"NOT SPECIFIED",
			"number":4,
			},
		"5":{
			"name":"TERM_RUNLIMIT",
			"desc":"Job killed after reaching LSF run time limit (5)",
			"number":5,
			},
		"6":{
			"name":"TERM_DEADLINE",
			"desc":"Job killed after deadline expires (6)",
			"number":6,
			},
		"7":{
			"name":"TERM_PROCESSLIMIT",
			"desc":"Job killed after reaching LSF process limit (7)",
			"number":7,
		},
		"8":{
			"name":"TERM_FORCE_OWNER",
			"desc":"Job killed by owner without time for cleanup (8)",
			"number":8,
			},
		"9":{
			"name":"TERM_FORCE_ADMIN",
			"desc":"Job killed by root or LSF administrator without time for cleanup (9)",
			"number":9,
			},
		"10":{
			"name":"TERM_REQUEUE_OWNER",
			"desc":"Job killed and requeued by owner (10)",
			"number":10,
			},
		"11":{
			"name":"TERM_REQUEUE_ADMIN",
			"desc":"Job killed and requeued by root or LSF administrator (11)",
			"number":11,
			},
		"12":{
			"name":"TERM_CPULIMIT",
			"desc":"Job killed after reaching LSF CPU usage limit (12)",
			"number":12,
		},
		"13":{
			"name":"TERM_CHKPNT",
			"desc":"Job killed after checkpointing (13)",
			"number":13,
			},
		"14":{
			"name":"TERM_OWNER",
			"desc":"Job killed by owner (14)",
			"number":14,
		},
		"15":{
			"name":"TERM_ADMIN",
			"desc":"Job killed by root or LSF administrator (15)",
			"number":15,
			},
		"16":{
			"name":"TERM_MEMLIMIT",
			"desc":"Job killed after reaching LSF memory usage limit (16)",
			"number":16,
			},
		"17":{
			"name":"TERM_EXTERNAL_SIGNAL",
			"desc":"Job killed by a signal external to LSF (17)",
			"number":16,
			},
		"18":{
			"name":"TERM_RMS",
			"desc":"NOT SPECIFIED",
			"number":18,
			},
		"19":{
			"name":"TERM_ZOMBIE",
			"desc":"Job exited while LSF is not available (19)",
			"number":19,
				},
		"20":{
			"name":"TERM_SWAP",
			"desc":"Job killed after reaching LSF swap usage limit (20)",
			"number":20,
			},
		"21":{
			"name":"TERM_THREADLIMIT",
			"desc":"Job killed after reaching LSF thread limit (21)",
			"number":21,
			},
		"22":{
			"name":"TERM_SLURM",
			"desc":"Job terminated abnormally in SLURM (node failure) (22)",
			"number":22,
			},
		"23":{
			"name":"TERM_BUCKET_KILL",
			"desc":"Job killed with bkill -b (23)",
			"number":23,
			},
		}


## When a job is terminated, LSF stores details on the reason why the job was terminated, this
#  class takes the error number and provides an error name and description as attributes.
class JobTermInfo:
	def __init__(self, id):
		id=str(id)
		if (not id in TERMINFO):
			id="0"
		## The name of the error as specified in lsbatch.h, for example TERM_RUNLIMIT
		self.name=TERMINFO[id]['name']
		## Description of the error as specified in the LSF documenation.
		#  For example: "Job killed after reaching LSF run time limit"
		self.description=TERMINFO[id]['desc']
		## The error number, for example: 5.
		self.number=int(TERMINFO[id]['number'])

FIELD_LOOKUP=	{
		'JOB_FINISH':{
			'6.0':{
				'vfields':[
					{
						'tag':22,
						'fieldStart':23,
						'fieldName':'askedHosts',
					},
					{
						'tag':23,
						'fieldStart':24,
						'fieldName':'execHosts',
					},
					],
				'fields':{
					'eventType':{ 'field':0, 'type':'str' },
					'versionNumber':{ 'field':1, 'type':'str' },
					'eventTime':{ 'field':2, 'type':'int' },
					'jobId':{ 'field':3, 'type':'int' },
					'userId':{ 'field':4, 'type':'int' },
					'options':{ 'field':5, 'type':'int' },
					'numProcessors':{ 'field':6, 'type':'int' },
					'submitTime':{ 'field':7, 'type':'int' },
					'beginTime':{ 'field':8, 'type':'int' },
					'termTime':{ 'field':9, 'type':'int' },
					'startTime':{ 'field':10, 'type':'int' },
					'userName':{ 'field':11, 'type':'str' },
					'queue':{ 'field':12, 'type':'str' },
					'resReq':{ 'field':13, 'type':'str' },
					'dependCond':{ 'field':14, 'type':'str' },
					'preExecCmd':{ 'field':15, 'type':'str' },
					'submitHost':{ 'field':16, 'type':'str' },
					'cwd':{ 'field':17, 'type':'str' },
					'inFile':{ 'field':18, 'type':'str' },
					'outFile':{ 'field':19, 'type':'str' },
					'errFile':{ 'field':20, 'type':'str' },
					'jobFile':{ 'field':21, 'type':'str' },
					'numAskedHosts':{ 'field':22, 'type':'int' },
					'numExHosts':{ 'field':23, 'type':'int' },
					'jStatus':{ 'field':24, 'type':'int' },
					'hostFactor':{ 'field':25, 'type':'float' },
					'jobName':{ 'field':26, 'type':'str' },
					'command':{ 'field':27, 'type':'str' },
					'utime':{ 'field':28, 'type':'float' },
					'stime':{ 'field':29, 'type':'float' },
					'maxrss':{ 'field':30, 'type':'float' },
					'ixrss':{ 'field':31, 'type':'float' },
					'ismrss':{ 'field':32, 'type':'float' },
					'idrss':{ 'field':33, 'type':'float' },
					'isrss':{ 'field':34, 'type':'float' },
					'minflt':{ 'field':35, 'type':'float' },
					'majflt':{ 'field':36, 'type':'float' },
					'nswap':{ 'field':37, 'type':'float' },
					'inblock':{ 'field':38, 'type':'float' },
					'oublock':{ 'field':39, 'type':'float' },
					'ioch':{ 'field':40, 'type':'float' },
					'msgsnd':{ 'field':41, 'type':'float' },
					'msgrcv':{ 'field':42, 'type':'float' },
					'nsignals':{ 'field':43, 'type':'float' },
					'nvcsw':{ 'field':44, 'type':'float' },
					'nivcsw':{ 'field':45, 'type':'float' },
					'exutime':{ 'field':46, 'type':'float' },
					'mailUser':{ 'field':47, 'type':'str' },
					'projectName':{ 'field':48, 'type':'str' },
					'exitStatus':{ 'field':49, 'type':'int' },
					'maxNumProcessors':{ 'field':50, 'type':'int' },
					'loginShell':{ 'field':51, 'type':'str' },
					'timeEvent':{ 'field':52, 'type':'str' },
					'idx':{ 'field':53, 'type':'int' },
					'maxRMem':{ 'field':54, 'type':'int' },
					'maxRSwap':{ 'field':55, 'type':'int' },
					'inFileSpool':{ 'field':56, 'type':'str' },
					'commandSpool':{ 'field':57, 'type':'str' },
					'rsvId':{ 'field':58, 'type':'str' },
					'sla':{ 'field':59, 'type':'str' },
					'exceptMask':{ 'field':60, 'type':'int' },
					'additionalInfo':{ 'field':61, 'type':'str' },
					'exitInfo':{ 'field':62, 'type':'int' },
					'warningAction':{ 'field':63, 'type':'str' },
					'warningTimePeriod':{ 'field':64, 'type':'int' },
					'chargedSAAP':{ 'field':65, 'type':'str' },
					},
				},
			'6.2':{
				'vfields':[
					{
						'tag':22,
						'fieldStart':23,
						'fieldName':'askedHosts',
					},
					{
						'tag':23,
						'fieldStart':24,
						'fieldName':'execHosts',
					},
					],
				'fields':{
					'eventType':{ 'field':0, 'type':'str' },
					'versionNumber':{ 'field':1, 'type':'str' },
					'eventTime':{ 'field':2, 'type':'int' },
					'jobId':{ 'field':3, 'type':'int' },
					'userId':{ 'field':4, 'type':'int' },
					'options':{ 'field':5, 'type':'int' },
					'numProcessors':{ 'field':6, 'type':'int' },
					'submitTime':{ 'field':7, 'type':'int' },
					'beginTime':{ 'field':8, 'type':'int' },
					'termTime':{ 'field':9, 'type':'int' },
					'startTime':{ 'field':10, 'type':'int' },
					'userName':{ 'field':11, 'type':'str' },
					'queue':{ 'field':12, 'type':'str' },
					'resReq':{ 'field':13, 'type':'str' },
					'dependCond':{ 'field':14, 'type':'str' },
					'preExecCmd':{ 'field':15, 'type':'str' },
					'submitHost':{ 'field':16, 'type':'str' },
					'cwd':{ 'field':17, 'type':'str' },
					'inFile':{ 'field':18, 'type':'str' },
					'outFile':{ 'field':19, 'type':'str' },
					'errFile':{ 'field':20, 'type':'str' },
					'jobFile':{ 'field':21, 'type':'str' },
					'numAskedHosts':{ 'field':22, 'type':'int' },
					'numExHosts':{ 'field':23, 'type':'int' },
					'jStatus':{ 'field':24, 'type':'int' },
					'hostFactor':{ 'field':25, 'type':'float' },
					'jobName':{ 'field':26, 'type':'str' },
					'command':{ 'field':27, 'type':'str' },
					'utime':{ 'field':28, 'type':'float' },
					'stime':{ 'field':29, 'type':'float' },
					'maxrss':{ 'field':30, 'type':'float' },
					'ixrss':{ 'field':31, 'type':'float' },
					'ismrss':{ 'field':32, 'type':'float' },
					'idrss':{ 'field':33, 'type':'float' },
					'isrss':{ 'field':34, 'type':'float' },
					'minflt':{ 'field':35, 'type':'float' },
					'majflt':{ 'field':36, 'type':'float' },
					'nswap':{ 'field':37, 'type':'float' },
					'inblock':{ 'field':38, 'type':'float' },
					'oublock':{ 'field':39, 'type':'float' },
					'ioch':{ 'field':40, 'type':'float' },
					'msgsnd':{ 'field':41, 'type':'float' },
					'msgrcv':{ 'field':42, 'type':'float' },
					'nsignals':{ 'field':43, 'type':'float' },
					'nvcsw':{ 'field':44, 'type':'float' },
					'nivcsw':{ 'field':45, 'type':'float' },
					'exutime':{ 'field':46, 'type':'float' },
					'mailUser':{ 'field':47, 'type':'str' },
					'projectName':{ 'field':48, 'type':'str' },
					'exitStatus':{ 'field':49, 'type':'int' },
					'maxNumProcessors':{ 'field':50, 'type':'int' },
					'loginShell':{ 'field':51, 'type':'str' },
					'timeEvent':{ 'field':52, 'type':'str' },
					'idx':{ 'field':53, 'type':'int' },
					'maxRMem':{ 'field':54, 'type':'int' },
					'maxRSwap':{ 'field':55, 'type':'int' },
					'inFileSpool':{ 'field':56, 'type':'str' },
					'commandSpool':{ 'field':57, 'type':'str' },
					'rsvId':{ 'field':58, 'type':'str' },
					'sla':{ 'field':59, 'type':'str' },
					'exceptMask':{ 'field':60, 'type':'int' },
					'additionalInfo':{ 'field':61, 'type':'str' },
					'exitInfo':{ 'field':62, 'type':'int' },
					'warningAction':{ 'field':63, 'type':'str' },
					'warningTimePeriod':{ 'field':64, 'type':'int' },
					'chargedSAAP':{ 'field':65, 'type':'str' },
					'licenseProject':{ 'field':66, 'type':'str' },
					},
				},
			'8.0.1':{
				'vfields':[
					{
						'tag':22,
						'fieldStart':23,
						'fieldName':'askedHosts',
					},
					{
						'tag':23,
						'fieldStart':24,
						'fieldName':'execHosts',
					},
					],
				'fields':{
					'eventType':{ 'field':0, 'type':'str' },
					'versionNumber':{ 'field':1, 'type':'str' },
					'eventTime':{ 'field':2, 'type':'int' },
					'jobId':{ 'field':3, 'type':'int' },
					'userId':{ 'field':4, 'type':'int' },
					'options':{ 'field':5, 'type':'int' },
					'numProcessors':{ 'field':6, 'type':'int' },
					'submitTime':{ 'field':7, 'type':'int' },
					'beginTime':{ 'field':8, 'type':'int' },
					'termTime':{ 'field':9, 'type':'int' },
					'startTime':{ 'field':10, 'type':'int' },
					'userName':{ 'field':11, 'type':'str' },
					'queue':{ 'field':12, 'type':'str' },
					'resReq':{ 'field':13, 'type':'str' },
					'dependCond':{ 'field':14, 'type':'str' },
					'preExecCmd':{ 'field':15, 'type':'str' },
					'submitHost':{ 'field':16, 'type':'str' },
					'cwd':{ 'field':17, 'type':'str' },
					'inFile':{ 'field':18, 'type':'str' },
					'outFile':{ 'field':19, 'type':'str' },
					'errFile':{ 'field':20, 'type':'str' },
					'jobFile':{ 'field':21, 'type':'str' },
					'numAskedHosts':{ 'field':22, 'type':'int' },
					'numExHosts':{ 'field':23, 'type':'int' },
					'jStatus':{ 'field':24, 'type':'int' },
					'hostFactor':{ 'field':25, 'type':'float' },
					'jobName':{ 'field':26, 'type':'str' },
					'command':{ 'field':27, 'type':'str' },
					'utime':{ 'field':28, 'type':'float' },
					'stime':{ 'field':29, 'type':'float' },
					'maxrss':{ 'field':30, 'type':'float' },
					'ixrss':{ 'field':31, 'type':'float' },
					'ismrss':{ 'field':32, 'type':'float' },
					'idrss':{ 'field':33, 'type':'float' },
					'isrss':{ 'field':34, 'type':'float' },
					'minflt':{ 'field':35, 'type':'float' },
					'majflt':{ 'field':36, 'type':'float' },
					'nswap':{ 'field':37, 'type':'float' },
					'inblock':{ 'field':38, 'type':'float' },
					'oublock':{ 'field':39, 'type':'float' },
					'ioch':{ 'field':40, 'type':'float' },
					'msgsnd':{ 'field':41, 'type':'float' },
					'msgrcv':{ 'field':42, 'type':'float' },
					'nsignals':{ 'field':43, 'type':'float' },
					'nvcsw':{ 'field':44, 'type':'float' },
					'nivcsw':{ 'field':45, 'type':'float' },
					'exutime':{ 'field':46, 'type':'float' },
					'mailUser':{ 'field':47, 'type':'str' },
					'projectName':{ 'field':48, 'type':'str' },
					'exitStatus':{ 'field':49, 'type':'int' },
					'maxNumProcessors':{ 'field':50, 'type':'int' },
					'loginShell':{ 'field':51, 'type':'str' },
					'timeEvent':{ 'field':52, 'type':'str' },
					'idx':{ 'field':53, 'type':'int' },
					'maxRMem':{ 'field':54, 'type':'int' },
					'maxRSwap':{ 'field':55, 'type':'int' },
					'inFileSpool':{ 'field':56, 'type':'str' },
					'commandSpool':{ 'field':57, 'type':'str' },
					'rsvId':{ 'field':58, 'type':'str' },
					'sla':{ 'field':59, 'type':'str' },
					'exceptMask':{ 'field':60, 'type':'int' },
					'additionalInfo':{ 'field':61, 'type':'str' },
					'exitInfo':{ 'field':62, 'type':'int' },
					'warningAction':{ 'field':63, 'type':'str' },
					'warningTimePeriod':{ 'field':64, 'type':'int' },
					'chargedSAAP':{ 'field':65, 'type':'str' },
					'licenseProject':{ 'field':66, 'type':'str' },
					'app':{ 'field':67, 'type':'str' },
					'postExecCmd':{ 'field':68, 'type':'str' },
					'runtimeEstimation':{ 'field':69, 'type':'int' },
					'jobGroupName':{ 'field':70, 'type':'str' },
					'requeueEValues':{ 'field':71, 'type':'str' },
					'options2':{ 'field':72, 'type':'int' },
					'resizeNotifyCmd':{ 'field':73, 'type':'str' },
					'lastResizeTime':{ 'field':74, 'type':'int' },
					'rsvId':{ 'field':75, 'type':'str' },
					'jobDescription':{ 'field':76, 'type':'str' },
					},
				},
			},

		'JOB_NEW':{
			'6.2':{
				'vfields':[
						{
						'tag':38,
						'fieldStart':39,
						'fieldName':"askedHosts",
						},
					],

				'fields':{
					'eventType':{ 'field':0, 'type':'str' },
					'versionNumber':{ 'field':1, 'type':'str' },
					'eventTime':{'field':2, 'type':'int'},
					'jobId':{ 'field':3, 'type':'int' },
					'userId':{ 'field':4, 'type':'int' },
					'options':{ 'field':5, 'type':'int' },
					'numProcessors':{ 'field':6, 'type':'int' },
					'submitTime':{ 'field':7, 'type':'int' },
					'beginTime':{ 'field':8, 'type':'int' },
					'termTime':{ 'field':9, 'type':'int' },
					'sigValue':{ 'field':10,'type':'int' },
					'chkpntPeriod':{ 'field':11, 'type':'int' },
					'restartPid':{ 'field':12, 'type':'int' },
					'userName':{ 'field':13, 'type':'str' },
					'cpuLimit':{ 'field':14, 'type':'int' },
					'fsLimit':{ 'field':15, 'type':'int' },
					'dataSegLimit':{ 'field':16, 'type':'int' },
					'stackSegLimit':{ 'field':17, 'type':'int' },
					'coreFileSizeLimit':{ 'field':18, 'type':'int' },
					'memSizeLimit':{ 'field':19, 'type':'int' },
					'rlimit1':{ 'field':20, 'type':'int' },
					'rlimit2':{ 'field':21, 'type':'int' },
					'rlimit3':{ 'field':22, 'type':'int' },
					'runLimit':{ 'field':23, 'type':'int' },
					'rlimit4':{ 'field':24, 'type':'int' },
					'hostSpec':{ 'field':25, 'type':'str' },
					'hostFactor':{ 'field':26, 'type':'float' },
					'umask':{ 'field':27, 'type':'int' },
					'queue':{ 'field':28, 'type':'str' },
					'resReq':{ 'field':29, 'type':'str' },
					'submitHost':{ 'field':30, 'type':'str' },
					'cwd':{ 'field':31, 'type':'str' },
					'chkpntDir':{ 'field':32, 'type':'str' },
					'inFile':{ 'field':33, 'type':'str' },
					'outFile':{ 'field':34, 'type':'str' },
					'errFile':{ 'field':35, 'type':'str' },
					'subHomeDir':{ 'field':36, 'type':'str' },
					'jobFile':{ 'field':37, 'type':'str' },
					'numAskedHosts':{ 'field':38, 'type':'int' },
					'dependCond':{ 'field':39, 'type':'str' },
					'preExecCmd':{ 'field':40, 'type':'str' },
					'jobName':{ 'field':41, 'type':'str' },
					'command':{ 'field':42, 'type':'str' },
					'nxf':{ 'field':43, 'type':'int' },
					'xf':{ 'field':44, 'type':'str' },
					'projectName':{ 'field':45, 'type':'str' },
#					'niosPort':{ 'field':46, 'type':'int' },
					'maxNumProcessors':{ 'field':46, 'type':'int' },
					'schedHostType':{ 'field':47, 'type':'str' },
					'loginShell':{ 'field':48, 'type':'str' },
					'userGroup':{ 'field':49, 'type':'str' },
					'exceptList':{ 'field':50, 'type':'str' },
					'options2':{ 'field':52, 'type':'int' },
					'idx':{ 'field':53, 'type':'int' },
#					'inFileSpool':{ 'field':55, 'type':'str' },
#					'commandSpool':{ 'field':56, 'type':'str' },
#					'jobSpoolDir':{ 'field':57, 'type':'str' },
#					'userPriority':{ 'field':58, 'type':'int' },
#					'rsvId':{ 'field':59, 'type':'str' },
#					'sla':{ 'field':61, 'type':'str' },
#					'threadLimit':{ 'field':62, 'type':'int' },
#					'extsched':{ 'field':63, 'type':'str' },
#					'warningAction':{ 'field':63, 'type':'str' },
#					'warningTimePeriod':{ 'field':64, 'type':'int' },
#					'SLArunLimit':{ 'field':65, 'type':'int' },
#					'licenseProject':{ 'field':66, 'type':'str' },
#					'options3':{ 'field':67, 'type':'int' },
#					'app':{ 'field':68, 'type':'str' },
#					'postExecCmd':{ 'field':69, 'type':'str' },
#					'runtimeEstimation':{ 'field':70, 'type':'int' },
#					'requeueEValues':{ 'field':71, 'type':'str' },
#					'resizeNotifyCmd':{ 'field':72, 'type':'str' },
#					'jobDescription':{ 'field':73, 'type':'str' },
				}
			},
			'8.0.1':{
				'vfields':[
						{
						'tag':38,
						'fieldStart':39,
						'fieldName':"askedHosts",
						},
					],

				'fields':{
					'eventType':{ 'field':0, 'type':'str' },
					'versionNumber':{ 'field':1, 'type':'str' },
					'eventTime':{'field':2, 'type':'int'},
					'jobId':{ 'field':3, 'type':'int' },
					'userId':{ 'field':4, 'type':'int' },
					'options':{ 'field':5, 'type':'int' },
					'numProcessors':{ 'field':6, 'type':'int' },
					'submitTime':{ 'field':7, 'type':'int' },
					'beginTime':{ 'field':8, 'type':'int' },
					'termTime':{ 'field':9, 'type':'int' },
					'sigValue':{ 'field':10,'type':'int' },
					'chkpntPeriod':{ 'field':11, 'type':'int' },
					'restartPid':{ 'field':12, 'type':'int' },
					'userName':{ 'field':13, 'type':'str' },
					'cpuLimit':{ 'field':14, 'type':'int' },
					'fsLimit':{ 'field':15, 'type':'int' },
					'dataSegLimit':{ 'field':16, 'type':'int' },
					'stackSegLimit':{ 'field':17, 'type':'int' },
					'coreFileSizeLimit':{ 'field':18, 'type':'int' },
					'memSizeLimit':{ 'field':19, 'type':'int' },
					'rlimit1':{ 'field':20, 'type':'int' },
					'rlimit2':{ 'field':21, 'type':'int' },
					'rlimit3':{ 'field':22, 'type':'int' },
					'runLimit':{ 'field':23, 'type':'int' },
					'rlimit4':{ 'field':24, 'type':'int' },
					'hostSpec':{ 'field':25, 'type':'str' },
					'hostFactor':{ 'field':26, 'type':'float' },
					'umask':{ 'field':27, 'type':'int' },
					'queue':{ 'field':28, 'type':'str' },
					'resReq':{ 'field':29, 'type':'str' },
					'submitHost':{ 'field':30, 'type':'str' },
					'cwd':{ 'field':31, 'type':'str' },
					'chkpntDir':{ 'field':32, 'type':'str' },
					'inFile':{ 'field':33, 'type':'str' },
					'outFile':{ 'field':34, 'type':'str' },
					'errFile':{ 'field':35, 'type':'str' },
					'subHomeDir':{ 'field':36, 'type':'str' },
					'jobFile':{ 'field':37, 'type':'str' },
					'numAskedHosts':{ 'field':38, 'type':'int' },
					'dependCond':{ 'field':39, 'type':'str' },
					'preExecCmd':{ 'field':40, 'type':'str' },
					'jobName':{ 'field':41, 'type':'str' },
					'command':{ 'field':42, 'type':'str' },
					'nxf':{ 'field':43, 'type':'int' },
					'xf':{ 'field':44, 'type':'str' },
					'mailUser':{ 'field':44, 'type':'str' },
					'projectName':{ 'field':45, 'type':'str' },
#					'niosPort':{ 'field':46, 'type':'int' },
					'maxNumProcessors':{ 'field':46, 'type':'int' },
					'schedHostType':{ 'field':47, 'type':'str' },
					'loginShell':{ 'field':48, 'type':'str' },
					'timeEvent':{ 'field':49, 'type':'str' },
					'userGroup':{ 'field':50, 'type':'str' },
					'exceptList':{ 'field':51, 'type':'str' },
					'options2':{ 'field':52, 'type':'int' },
					'idx':{ 'field':53, 'type':'int' },
#					'inFileSpool':{ 'field':55, 'type':'str' },
#					'commandSpool':{ 'field':56, 'type':'str' },
#					'jobSpoolDir':{ 'field':57, 'type':'str' },
#					'userPriority':{ 'field':58, 'type':'int' },
#					'rsvId':{ 'field':59, 'type':'str' },
#					'sla':{ 'field':61, 'type':'str' },
#					'threadLimit':{ 'field':62, 'type':'int' },
#					'extsched':{ 'field':63, 'type':'str' },
#					'warningAction':{ 'field':63, 'type':'str' },
#					'warningTimePeriod':{ 'field':64, 'type':'int' },
#					'SLArunLimit':{ 'field':65, 'type':'int' },
#					'licenseProject':{ 'field':66, 'type':'str' },
#					'options3':{ 'field':67, 'type':'int' },
#					'app':{ 'field':68, 'type':'str' },
#					'postExecCmd':{ 'field':69, 'type':'str' },
#					'runtimeEstimation':{ 'field':70, 'type':'int' },
#					'requeueEValues':{ 'field':71, 'type':'str' },
#					'resizeNotifyCmd':{ 'field':72, 'type':'str' },
#					'jobDescription':{ 'field':73, 'type':'str' },
				}
			}	
		}
	}
class JobFinishEvent(object):
	def __init__(self,row):
		if row[0]!="JOB_FINISH":
			raise ValueError
		fields=FIELD_LOOKUP[row[0]][row[1]]
		for field in fields['vfields']:
			entries=[]
			numEntries=int(row[field['tag']])
			for i in xrange(numEntries):
				entries.append( row.pop(field['fieldStart']) )
			setattr(self, field['fieldName'], entries)
		for name in fields['fields'].iterkeys():
			id=fields['fields'][name]['field']
			cast=fields['fields'][name]['type']
			value=row[id]
			if cast=="str":
				value=str(value)
			elif cast=="int":
				value=int(value)
			elif cast=="float":
				value=float(value)
			setattr(self,name,value)
		self.endTime=self.eventTime
		self.termInfo=JobTermInfo(self.exitInfo)
		if self.startTime<1:
			# job never started
			# Possibly change to raise exception
			self.wallTime=0
			self.pendTime=self.endTime-self.submitTime
			self.startTime=self.endTime
		else:
			self.wallTime=self.endTime-self.startTime
			self.pendTime=self.startTime-self.submitTime
		if self.jStatus==32:
			self.jStatus="Exit"
		else:
			self.jStatus="Done"





class JobNewEvent(object):
	def __init__(self,row):
		if row[0]!="JOB_NEW":
			raise ValueError

		fields=FIELD_LOOKUP[row[0]][row[1]]
		for field in fields['vfields']:
			entries=[]
			try:
				numEntries=int(row[field['tag']])
			except ValueError:
				if row[1] in ['8.0.1','6.2']:
					row.pop(26)
					row.pop(26)
					numEntries=int(row[field['tag']])
			for i in xrange(numEntries):
				entries.append( row.pop(field['fieldStart']) )
			setattr(self, field['fieldName'], entries)
		if row[1]=='8.0.1':
			if len(row)==71:
				try:
					# Should be a string, so should fail
					int(row[45])
				except:
					try:
						# should be a string so should fail
						int(row[48])
					except:
						try:
							# should beints
							int(row[46])
							int(row[47])
							row.pop(46)
						except:
							pass

		for name in fields['fields'].iterkeys():
			id=fields['fields'][name]['field']
			cast=fields['fields'][name]['type']
			value=row[id]
			if cast=="str":
				value=str(value)
			elif cast=="int":
				value=int(value)
			elif cast=="float":
				value=float(value)
			setattr(self,name,value)
