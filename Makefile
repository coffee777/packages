PACKAGES = $(patsubst %.spec,%,$(wildcard *.spec))
BUILDLOG = /tmp/$@.build
FINDRPMS = `sed -nr 's|^Wrote: (/.*\.rpm)|\1|p' $(BUILDLOG)`

help:
	@echo 'Usage: make PACKAGE...'

all: $(PACKAGES)

$(PACKAGES):
	spectool -S -C ~makerpm/rpmbuild/SOURCES -g $@.spec
	test ! -d sources/$@ || cp -f sources/$@/* ~makerpm/rpmbuild/SOURCES/
	cp -f $@.spec ~makerpm/rpmbuild/SPECS/
	su -c 'cd ~/rpmbuild && rpmbuild -ba SPECS/$@.spec > $(BUILDLOG)' makerpm
	for rpm in $(FINDRPMS); do cp $$rpm .; done

install: ~/Dropbox/Public/fedora-remix/16
	rm -f *-debuginfo-*.rpm
	cp -f *.src.rpm $</source/packages && cd $< && createrepo source
	cp -f *.{noarch,i686}.rpm $</i386/packages && cd $< && createrepo i386

init: ~makerpm/rpmbuild

~makerpm/rpmbuild:
	yum -y install fedora-packager spin-kickstarts livecd-tools
	useradd --system --create-home makerpm
	passwd makerpm
	su -c rpmdev-setuptree makerpm

test:
	rpmlint *.rpm

clean:
	rm -f *.rpm


.PHONY: help all install init test clean $(PACKAGES)
