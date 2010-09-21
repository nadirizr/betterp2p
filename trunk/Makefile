
default:
	@echo
	@echo '  Type "make build-all" to build core library and plugin.'
	@echo '       "make install" to install BetterP2P.'
	@echo '       "make prerequisites" to install required packages.'
	@echo

BOOST_PACKAGES = system filesystem iostreams regex thread program-options python
DEV_PACKAGES = libssl liblog4cpp5
PYTHON_PACKAGES = setuptools
OTHER_PACKAGES = checkinstall
ALL_PACKAGES = ${foreach p,$(BOOST_PACKAGES),libboost-$p-dev} \
               ${foreach p,$(DEV_PACKAGES),$p-dev} \
               ${foreach p,$(PYTHON_PACKAGES),python-$p} \
               $(OTHER_PACKAGES)

prerequisites:
	sudo apt-get install $(ALL_PACKAGES)

build-all:
	$(MAKE) -C core
	$(MAKE) -C integration/libtorrent-rasterbar
	$(MAKE) -C ui/deluge

install:
	install -m755 core/build/lib/libbp2p.so /usr/local/lib/libbp2p.so
	$(MAKE) -C integration/libtorrent-rasterbar install
	ldconfig 2>/dev/null
	$(MAKE) -C ui/deluge install

deb:
	sudo checkinstall --backup=no --deldoc=yes --delspec=yes --deldesc=yes
	sudo chown $(USER) ./*.deb

# Notice:
# "import libtorrent" must work before trying to install Deluge.
# Otherwise Deluge's setup attempts to compile its own version of libtorrent.
