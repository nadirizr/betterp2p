
PWD := ${shell pwd}
SYS_LD_LIBRARY_PATH := $(LD_LIBRARY_PATH)
SYS_DYLD_LIBRARY_PATH := $(DYLD_LIBRARY_PATH)
SYS_PKG_CONFIG_PATH := $(PKG_CONFIG_PATH)

PKG_CONFIG_PATH = ${abspath ../../../core}:$(SYS_PKG_CONFIG_PATH)

export PKG_CONFIG_PATH

spc = $e $e
LDFLAGS = ${shell PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) pkg-config --libs libbp2p}
LDFLAGS += ${wildcard $(PWD)/../plugin/*.a}
CXXFLAGS = -I$(PWD)/..
LD_LIBRARY_PATH = ${subst $(spc),:,${strip ${patsubst -L%,%,${filter -L%,$(LDFLAGS)}} $(SYS_LD_LIBRARY_PATH)}}
DYLD_LIBRARY_PATH = ${subst $(spc),:,${strip ${patsubst -L%,%,${filter -L%,$(LDFLAGS)}} $(SYS_DYLD_LIBRARY_PATH)}}

.PHONY: libtorrent
libtorrent:
	( cd libtorrent+bp2p && grep -l -r 'XXX: BP2P' . ) | grep -v \.svn | tee .patched.filelist
	for fn in `cat .patched.filelist`; do echo $$fn; mkdir -p `dirname libtorrent/$$fn`; cp libtorrent+bp2p/$$fn libtorrent/$$fn; done
	
libtorrent-rasterbar-0.14.4:
	tar xf ext/libtorrent-rasterbar-0.14.4.tar.gz

libtorrent+bp2p: libtorrent-rasterbar-0.14.4
	mv libtorrent-rasterbar-0.14.4 $@
	( cd libtorrent ; tar cf - . ) | ( cd $@ ; tar xvf - )

configure:
	( cd libtorrent+bp2p ; LD_LIBRARY_PATH='$(LD_LIBRARY_PATH)' DYLD_LIBRARY_PATH='$(DYLD_LIBRARY_PATH)' LDFLAGS='$(LDFLAGS)' CXXFLAGS='$(CXXFLAGS)' ./configure --enable-python-binding )
	# Create libtorrent+bp2p.pc
	awk '/^prefix=/ { $$0= "prefix=$(PWD)/libtorrent+bp2p" } { print }' libtorrent+bp2p/libtorrent-rasterbar.pc > libtorrent+bp2p/libtorrent+bp2p.pc

build:
	make -C libtorrent+bp2p

install:
	make -C libtorrent+bp2p install

clean:
	rm -rf libtorrent-rasterbar-0.14.4 libtorrent+bp2p
