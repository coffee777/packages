PACKAGES = $(patsubst %.spec,%,$(wildcard *.spec))
BUILDLOG = /tmp/$@.build
FINDRPMS = `sed -nr 's|^Wrote: (/.*\.rpm)|\1|p' $(BUILDLOG)`

help:
	@printf 'Usage: sudo make PACKAGE...\n\nPackages:\n'
	@echo $(sort $(PACKAGES)) | tr " " "\n" | column -x; echo

all: $(PACKAGES)

$(PACKAGES): | ~makerpm/rpmbuild
	yum-builddep -qyC --noplugins $@.spec
	spectool -S -C $|/SOURCES -g $@.spec
	test ! -d sources/$@ || cp -f sources/$@/* $|/SOURCES/
	cp -f $@.spec $|/SPECS/
	su -c 'cd $| && rpmbuild -ba SPECS/$@.spec > $(BUILDLOG)' makerpm
	for rpm in $(FINDRPMS); do cp $$rpm .; done

install: ~/Dropbox/Public/fedora-remix/16
	rm -f *-debuginfo-*.rpm
	cp -f *.src.rpm $</source/packages && cd $< && createrepo source
	cp -f *.{noarch,i686}.rpm $</i386/packages && cd $< && createrepo i386

init: ~makerpm/rpmbuild

~makerpm/rpmbuild:
	rpm -q fedora-packager || yum -y install fedora-packager
	useradd --system --create-home makerpm
	su -c rpmdev-setuptree makerpm

test:
	rpmlint *.rpm

clean:
	rm -f *.rpm


.PHONY: help all install init test clean $(PACKAGES)
