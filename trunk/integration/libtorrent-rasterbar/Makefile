
all:
	$(MAKE) -C patches libtorrent+bp2p
	$(MAKE) -C patches configure
	$(MAKE) -C plugin
	$(MAKE) -C patches configure # yes, again
	$(MAKE) -C patches build

clean:
	$(MAKE) -C plugin clean
	$(MAKE) -C patches clean

install:
	$(MAKE) -C patches install
