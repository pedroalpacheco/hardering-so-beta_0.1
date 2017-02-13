# -*- coding: utf-8 -*-
#Call
#PedroALPacheco - pedro.pacheco.a@gmail.com / papacheco@furb.br - 06/02/2017
#!/usr/bin/python

import time
import os
import sys
import modules
from modules import *


try:
	#See root
	verify_user.see_root()

	def update_progress_bar():
		print '\b>',
		sys.stdout.flush()

	print 'Starting [',
	sys.stdout.flush()


	#See files
	verify_files.see_file()


	#1-Detect OS
	check_OS.so()
	update_progress_bar()

	#1-A)-Task check ports OS
	check_ports.verifport()
	update_progress_bar()

	#2-Task check cronta user
	check_cron.cronusuarios()
	update_progress_bar()

	#3-Task check files our pastes no user
	check_filenouser.nouser()
	update_progress_bar()

	#4-Task check files writing
	check_filew.arquivosescrita()
	update_progress_bar()

	#5-Check history for user
	check_history.historicouser()
	update_progress_bar()

	#6-Check info for user
	check_infouser.informacoesuser()
	update_progress_bar()

	#7-Check inizialization to OS
	check_init.inicializacao()
	update_progress_bar()

	#8-Check if ipv6 enable
	check_ipv6.veripv6()
	update_progress_bar()

	#9-Check packages
	check_packages.pacotes()
	update_progress_bar()

	#10-Check confs the ssh
	check_ssh.infossh()
	update_progress_bar()

	#11-Check if user shell
	check_usershell.shelluser()
	update_progress_bar()

	#12-Check if user uid root
	check_useruidroot.useruid()
	update_progress_bar()

	#13-Send mail
	send_mail.mail()
	update_progress_bar()

	#Add as many tasks as you need.

	print '] Done!'

except KeyboardInterrupt:
	print('\nSistema cancelado!')
	sys.exit(0)
