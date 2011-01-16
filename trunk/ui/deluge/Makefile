
TESTING_LAB_PATCH = 1

default: patch-for-multiple-instances ;

unpack:
	tar xf ext/deluge-1.1.9.tar.gz

UNAME := $(shell uname -s)

# sed inplace with no backup for GNU sed
SED_INPLACE = sed -i
ifeq ($(UNAME),Darwin)
	# sed inplace for BSD sed
	SED_INPLACE = sed -i ""
endif

patch-for-multiple-instances: unpack
	grep -l 'if iface.NameHasOwner("org.deluge_torrent.Deluge")' `find deluge-1.1.9 -name "*.py"` > .patched.filelist || echo No files need patch.
	$(SED_INPLACE) '/if iface.NameHasOwner("org.deluge_torrent.Deluge")/ {; s/if iface/if False and iface/; }' `cat .patched.filelist`

install:
	( cd deluge-1.1.9 && python setup.py install )
