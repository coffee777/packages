PKG = jsmin gnome-extra nginx pngquant md2html

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

# FIXME: this is a really hacky, lazy solution
install: ~/Dropbox/Public/fedora-remix/16
	cp -f *.src.rpm $</source/packages && cd $< && createrepo source
	-cp -f *.noarch.rpm $</i386/packages
	-cp -f *.i686.rpm $</i386/packages
	cd $< && createrepo i386

clean:
	rm -f *.rpm

.PHONY: help all install clean $(PKG)