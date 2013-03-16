ABIVER  = 5.2
CC      = gcc
CFLAGS  = -O2 -Wall -fPIC

OBJECTS = lapi.o lcode.o lctype.o ldebug.o ldo.o ldump.o lfunc.o lgc.o llex.o \
          lmem.o lobject.o lopcodes.o lparser.o lstate.o lstring.o ltable.o \
          ltm.o lundump.o lvm.o lzio.o lauxlib.o lbaselib.o lbitlib.o \
          lcorolib.o ldblib.o liolib.o lmathlib.o loslib.o lstrlib.o \
          ltablib.o loadlib.o linit.o

lua: lua.o liblua-$(ABIVER).so
	$(CC) $(CFLAGS) -DLUA_USE_LINUX -o $@ $< -L. -llua-5.2 -lreadline

liblua-$(ABIVER).so: $(OBJECTS)
	$(CC) -shared -Wl,-soname,$@ -lm -ldl -o $@ $^

check: lua
	@LD_LIBRARY_PATH=. ./lua -e 'print "it works!"'
