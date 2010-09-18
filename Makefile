
default:
	@echo
	@echo '  Type "make build-all" to build core library and plugin.'
	@echo '       "make install" to install BetterP2P.'
	@echo

build-all:
	$(MAKE) -C core
	$(MAKE) -C integration/libtorrent-rasterbar

install:
	install -m755 core/build/lib/libbp2p.so /usr/local/lib/libbp2p.so
	$(MAKE) -C integration/libtorrent-rasterbar install
