PKG = jsmin gnome-extra nginx pngquant

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

clean:
	rm -f *.rpm

.PHONY: help all clean $(PKG)
