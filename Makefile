
default:
	echo 'Type "make install" to install BetterP2P.'

install:
	install -m755 core/build/lib/libbp2p.so /usr/local/lib/libbp2p.so
