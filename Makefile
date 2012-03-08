PKG = jsmin nginx pngquant md2html luajit weighttp cgit discount fcgiwrap \
      httpd lua-json lua-cosmo lua-lgi tidy

# Null glob expansion is required for glob patterns used in install target
SHELL:=/bin/bash -O nullglob

help:
	@echo "Usage: make PACKAGE"
	@echo "Available packages: $(PKG)"
	@echo "Example: make nginx"
	@echo 'Use "make all" to build all available packages'

all: $(PKG)

$(PKG):
	spectool -S -C ~makerpm/rpmbuild/SOURCES -g $@/$@.spec
	cp -f $@/* ~makerpm/rpmbuild/SOURCES/
	cp -f $@/$@.spec ~makerpm/rpmbuild/SPECS/
	su -c 'cd ~/rpmbuild && rpmbuild -ba SPECS/$@.spec 1>/tmp/$@.build' makerpm
	sed -nr 's|^Wrote: (/.*\.rpm)|\1|p' /tmp/$@.build | \
	    while read line; do cp $$line ./; done

install: ~/Dropbox/Public/fedora-remix/16
	rm -f *-debuginfo-*.rpm
	cp -f *.src.rpm $</source/packages && cd $< && createrepo source
	cp -f *.{noarch,i686}.rpm $</i386/packages && cd $< && createrepo i386

test:
	rpmlint *.rpm

clean:
	rm -f *.rpm

.PHONY: help all install test clean $(PKG)
