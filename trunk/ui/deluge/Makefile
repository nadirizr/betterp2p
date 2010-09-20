
TESTING_LAB_PATCH = 1

default: patch-for-multiple-instances ;

unpack:
	tar xf ext/deluge-1.1.9.tar.gz

patch-for-multiple-instances: unpack
	grep -l 'if iface.NameHasOwner("org.deluge_torrent.Deluge")' `find deluge-1.1.9 -name "*.py"` > .patched.filelist || echo No files need patch.
	for fn in `cat .patched.filelist`; do sed -i 's/if iface.NameHasOwner("org.deluge_torrent.Deluge")/if 0 and iface.NameHasOwner("org.deluge_torrent.Deluge")/' $$fn; done

install:
	( cd deluge-1.1.9 && python setup.py install )
