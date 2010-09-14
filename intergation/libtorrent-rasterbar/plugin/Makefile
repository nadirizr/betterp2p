
PKG_CONFIG_PATH = $(PWD)/../../../core:$(PWD)/../patches/libtorrent+bp2p
CXX = g++

export PKG_CONFIG_PATH

SRC = ${shell echo *.cc}

bp2p-libtorrent-plugin.a: $(SRC:.cc=.o)
	$(AR) cq $@ $+
	rm $+

%.o: %.cc
	$(CXX) `pkg-config --cflags libtorrent+bp2p libbp2p` -c $< -o $@
	
