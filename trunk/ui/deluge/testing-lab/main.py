"""
Deluge Testing Lab

This script will run two instances of Deluge. Each instance comprises of a daemon
(deluged) and a user-interface.
Script will exit when all clients and daemons have been terminated, or when the user
presses Ctrl+C on the terminal - in which case all spawned processes are killed.
"""

import os
import shutil
from subprocess import Popen


class DelugeSpecimen(object):
	"""
	A single instance of Deluge.
	If a configuration does not exist in confdir, a fresh one is created using
	the default one stored in ./conf.
	"""

	def __init__(self, port):
		self.port = port
		self.confdir = os.path.expanduser("~/scratch/deluge/%s" % port)
		self.processes = []

	def __call__(self):
		self._prepare_conf()
		self._start_daemon()
		self._start_ui()
		return self

	def _prepare_conf(self):
		subdir = str(self.port)
		preconf = os.path.join(os.path.dirname(__file__), "conf", subdir)
		if os.path.isdir(preconf):
			for filename in os.listdir(preconf):
				sourceconf = os.path.join(preconf, filename)
				targetconf = os.path.join(self.confdir, filename)
				if os.path.isfile(sourceconf) and not os.path.exists(targetconf):
					if not os.path.isdir(os.path.dirname(targetconf)):
						os.makedirs(os.path.dirname(targetconf))
					shutil.copyfile(sourceconf, targetconf)

	def _start_daemon(self):
		cmdline = "deluged -d -c %(confdir)s -p %(port)d" % self.__dict__
		p = Popen(cmdline, shell=True)
		p.description = "deluged, %s" % self.port
		self.processes.append(p)

	def _start_ui(self):
		cmdline = "deluge -c %(confdir)s" % self.__dict__
		p = Popen(cmdline, shell=True)
		p.description = "deluge ui, %s" % self.port
		self.processes.append(p)


class ProcessSitter(object):
	"""
	Monitors a list of processes. Waits for processes to finish. If terminated,
	kills processes before exit.
	"""

	def __init__(self, processes=[]):
		self.processes = processes or []

	def __call__(self):
		try:
			self._monitor_processes()
		except KeyboardInterrupt:
			print '-' * 60
			self._killall()

	def _monitor_processes(self):
		while self.processes:
			self.processes = self._poll(self.processes)

	def _poll(self, processlist):
		for p in processlist:
			if p.poll() is not None:
				print "%d (%s) has exited" % (p.pid, p.description)
		return [p for p in processlist if p.returncode is None]

	def _killall(self):
		for p in self.processes:
			try:
				print "Kill %d (%s)" % (p.pid, p.description)
				p.kill()
			except:
				print "- warning: kill failed;"



if __name__ == '__main__':
	processes = []
	processes += DelugeSpecimen(55333)().processes
	processes += DelugeSpecimen(55444)().processes

	ProcessSitter(processes)()
