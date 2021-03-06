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

import sys
import traceback
import csv
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from lavaFlow.accounting import *
from lavaFlow.models import *

# Global cluster
c=None
# User object cache
users={}
# Host object cache
hosts={}
# Queue Object Cache
queues={}

class Command(BaseCommand):
	option_list=BaseCommand.option_list + (
		make_option("-f", "--file", dest="filename",help="Read from lsb accounting FILE", metavar="FILE"),
		make_option("-c", "--cluster", dest="cluster",help="Cluster name", metavar="CLUSTER"),
	)
	def handle(self, *args, **options):
		if not options['cluster']:
			print "No cluster specified."
			sys.exit(253)
		if not options['filename']:
			print "No filename specified."
			sys.exit(253)
		try:
			acctf=open(options['filename'],'rb')
		except IOError as e:
			print 'File cannot be opened.'
			sys.exit(254)
		rowNum=0
		skipped=0
		f=csv.reader(acctf, delimiter=' ', quotechar='"')
		(c, created)=Cluster.objects.get_or_create(name=options['cluster'])
		for row in f:
			try:
				if row[0]=="JOB_FINISH":
					job_finish(c,row)
					rowNum+=1
					if rowNum % 100==0:
						print "Row: %s" %rowNum
			except KeyboardInterrupt:
				raise
			except:
				traceback.print_exc()
				print row

def job_finish(c,row):
	job=JobFinishEvent(row)
	# Find or create the user
	try:
		user=users[job.userName]
	except:
		(user,created)=User.objects.get_or_create(userName=job.userName)
		users[job.userName]=user

	# find or create the submit host
	try:
		submitHost=hosts[job.submitHost]
	except:
		(submitHost,created)=Host.objects.get_or_create(hostName=job.submitHost)
		hosts[job.submitHost]=submitHost

	# find or create the job, don't cache it.
	jobData={
		'jobId':job.jobId,
		'user':user,
		'submitHost':submitHost,
		'submitTime':job.submitTime,
		'cluster':c,
	}
	(j, created)=Job.objects.get_or_create(jobId=job.jobId, cluster=c, user=user,submitTime=job.submitTime, defaults=jobData)

	# Find or create the element in the project
	elementData={
		'elementId':job.idx,
	}
	(e, created)=j.elements.get_or_create(elementId=job.idx, defaults=elementData)

	# find or create the queue
	try:
		q=queues[job.queue]
	except:
		(q, created)=Queue.objects.get_or_create(name=job.queue)
		queues[job.queue]=q

	# create the run if needed
	runData={
		'element':e,
		'numProcessors':job.numProcessors,
		'startTime':job.startTime,
		'endTime':job.endTime,
		'wallTime':job.wallTime,
		'cpuTime':job.wallTime*job.numProcessors,
		'pendTime':job.pendTime,
		'queue':q,
	}

	(r,created)=Run.objects.get_or_create(element=e,startTime=job.startTime, defaults=runData)
	if created:
		# Add the projects to the run
		(p, created)=Project.objects.get_or_create(name=job.projectName, cluster=c)
		r.projects.add(p)
		for host in job.execHosts:
			cores=1
			if "*" in host:
				cores,star,host=host.partition("*")
			try:
				h=hosts[host]
			except:
				(h,created)=Host.objects.get_or_create(hostName=host)
				hosts[host]=h
			r.executions.create(host=h, run=r, numProcessors=cores)
		rf=RunFinishInfo()
		rf.run=r
		rf.options=job.options
		rf.numProcessors=job.numProcessors
		rf.beginTime=job.beginTime
		rf.termTime=job.termTime
		rf.userName=job.userName
		rf.resReq=job.resReq
		rf.dependCond=job.dependCond
		rf.preExecCmd=job.preExecCmd
		rf.cwd=job.cwd
		rf.inFile=job.inFile
		rf.outFile=job.outFile
		rf.errFile=job.errFile
		rf.jobFile=job.jobFile
		(js, created)=JobStatus.objects.get_or_create(jStatus=job.jStatus)
		rf.jStatus=js
		rf.hostFactor=job.hostFactor
		rf.jobName=job.jobName
		rf.command=job.command
		rf.utime=job.utime
		rf.stime=job.stime
		rf.maxrss=job.maxrss
		rf.ixrss=job.ixrss
		rf.ismrss=job.ismrss
		rf.idrss = job.idrss
		rf.isrss = job.isrss
		rf.minflt = job.minflt
		rf.majflt = job.majflt
		rf.nswap = job.nswap
		rf.inblock = job.inblock
		rf.oublock = job.oublock
		rf.ioch = job.ioch
		rf.msgsnd = job.msgsnd
		rf.msgrcv = job.msgrcv
		rf.nsignals = job.nsignals
		rf.nvcsw = job.nvcsw
		rf.nivcsw = job.nivcsw
		rf.exutime = job.exutime
		rf.mailUser = job.mailUser
		rf.projectName = job.projectName
		rf.exitStatus = job.exitStatus
		rf.maxNumProcessors= job.maxNumProcessors
		if len(job.loginShell)<RunFinishInfo._meta.get_field('loginShell').max_length:
			rf.loginShell = job.loginShell
		else:
			rf.loginShell="TRUNCATED"
		rf.timeEvent = job.timeEvent
		rf.idx = job.idx
		rf.maxRMem = job.maxRMem
		rf.maxRSwap = job.maxRSwap
		rf.inFileSpool = job.inFileSpool
		rf.commandSpool = job.commandSpool
		rf.rsvId = job.rsvId
		rf.sla = job.sla
		rf.exceptMask = job.exceptMask
		rf.additionalInfo = job.additionalInfo
		er=job.termInfo.name
		if er=="TERM_UNKNOWN":
			er="%s_%s" % (rf.jStatus.jStatus,rf.exitStatus) 
		(ei,created)=ExitReason.objects.get_or_create(name=er, defaults={'description':job.termInfo.description,'value':job.termInfo.number})
		rf.exitInfo = ei
		rf.warningTimePeriod = job.warningTimePeriod
		rf.warningAction = job.warningAction
		rf.save()
		for host in job.askedHosts:
			cores=1
			try:
				h=hosts[host]
			except:
				(h,created)=Host.objects.get_or_create(hostName=host)
				hosts[host]=h
			rf.askedHosts.add(h)

