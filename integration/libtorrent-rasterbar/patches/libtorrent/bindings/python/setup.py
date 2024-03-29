#!/usr/bin/env python

from distutils import sysconfig
from distutils.core import setup, Extension
import os
import platform
import sys

if 'boost_python' == '':
	print 'You need to pass --enable-python-binding to configure in order ',
	print 'to properly use this setup. There is no boost.python library configured now'
	sys.exit(1)

def parse_cmd(cmdline, prefix, keep_prefix = False):
	ret = []
	for token in cmdline.split():
		if token[:len(prefix)] == prefix:
			if keep_prefix:
				ret.append(token)
			else:
				ret.append(token[len(prefix):])
	return ret

def arch():
	if platform.system() != 'Darwin': return []
	import struct
	a = os.uname()[4]
	if a == 'Power Macintosh': a = 'ppc'
	if a == 'i386' and struct.calcsize("P") == 8: a = "x86_64" # XXX: BP2P
	return ['-arch', a]

if platform.system() == 'Windows':
# on windows, build using bjam and build an installer
	import shutil
	if os.system('bjam boost=source link=static geoip=static boost-link=static release msvc-7.1 optimization=space') != 0:
		print 'build failed'
		sys.exit(1)
	try: os.mkdir(r'build')
	except: pass
	try: os.mkdir(r'build\lib')
	except: pass
	try: os.mkdir(r'libtorrent')
	except: pass
	shutil.copyfile(r'bin\msvc-7.1\release\boost-source\geoip-static\link-static\optimization-space\threading-multi\libtorrent.pyd', r'.\build\lib\libtorrent.pyd')
	setup( name='python-libtorrent',
		version='0.14.4',
		author = 'Arvid Norberg',
		author_email='arvid@cs.umu.se',
		description = 'Python bindings for libtorrent-rasterbar',
		long_description = 'Python bindings for libtorrent-rasterbar',
		url = 'http://www.rasterbar.com/products/libtorrent/index.html',
		platforms = 'Windows',
		license = 'Boost Software License - Version 1.0 - August 17th, 2003',
		packages = ['libtorrent'],
	)
	sys.exit(0)

config_vars = sysconfig.get_config_vars()
if "CFLAGS" in config_vars and "-Wstrict-prototypes" in config_vars["CFLAGS"]:
	config_vars["CFLAGS"] = config_vars["CFLAGS"].replace("-Wstrict-prototypes", " ")
if "OPT" in config_vars and "-Wstrict-prototypes" in config_vars["OPT"]:
	config_vars["OPT"] = config_vars["OPT"].replace("-Wstrict-prototypes", " ")

source_list = os.listdir(os.path.join(os.path.dirname(__file__), "src"))
source_list = [os.path.join("src", s) for s in source_list if s.endswith(".cpp")]

extra_cmd = '-DTORRENT_USE_OPENSSL -DTORRENT_LINKING_SHARED   -pthread -I/opt/local/include -lz  -lboost_filesystem-mt -lboost_thread-mt  -lssl -lcrypto -lboost_system-mt -L/usr/lib -I/usr/include/openssl -DHAVE_SSL'

setup( name='python-libtorrent',
	version='0.14.4',
	author = 'Arvid Norberg',
	author_email='arvid@cs.umu.se',
	description = 'Python bindings for libtorrent-rasterbar',
	long_description = 'Python bindings for libtorrent-rasterbar',
	url = 'http://www.rasterbar.com/products/libtorrent/index.html',
	platforms = 'any',
	license = 'Boost Software License - Version 1.0 - August 17th, 2003',
	ext_modules = [Extension('libtorrent',
		sources = source_list,
		language='c++',
		include_dirs = ['../../include','../../include/libtorrent'] + parse_cmd(extra_cmd, '-I'),
		library_dirs = ['../../src/.libs'] + parse_cmd(extra_cmd, '-L'),
		extra_link_args = '-L/Users/corwin/dev/betterp2p/core/build/lib -lbp2p   /Users/corwin/dev/betterp2p/integration/libtorrent-rasterbar/patches/../plugin/bp2p-libtorrent-plugin.a -L/opt/local/lib'.split() + arch(),
		extra_compile_args = parse_cmd(extra_cmd, '-D', True) + arch() + ['-DBOOST_MULTI_INDEX_DISABLE_SERIALIZATION'],
		libraries = ['torrent-rasterbar','boost_python'] + parse_cmd(extra_cmd, '-l'))],
)
