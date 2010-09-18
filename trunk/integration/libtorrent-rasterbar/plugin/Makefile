
CXX = g++
PKG_CONFIG_PATH = ${abspath ../../../core}:${abspath ../patches/libtorrent+bp2p}

export PKG_CONFIG_PATH

SRC = ${shell echo *.cc}

bp2p-libtorrent-plugin.a: $(SRC:.cc=.o)
	$(AR) cr $@ $+
	rm $+

%.o: %.cc
	$(CXX) `pkg-config --cflags libtorrent+bp2p libbp2p` -c $< -o $@
	
clean:
	rm -f bp2p-libtorrent-plugin.a $(SRC:.cc=.o)
