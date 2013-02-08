PACKAGES = $(patsubst %.spec,%,$(wildcard *.spec))
BUILDLOG = /tmp/$@.build
FINDRPMS = `sed -nr 's|^Wrote: (/.*\.rpm)|\1|p' $(BUILDLOG)`
DEPSLIST = rpmspec -q --buildrequires $@.spec | cut -f1 -d' ' | cut -f1 -d'('
HAVEDEPS = test -z "`$(DEPSLIST)`" || $(DEPSLIST) | xargs rpm -q

# http://fedoraproject.org/wiki/Packaging:Guidelines#Exceptions_2
MINDEPS  = bash bzip2 coreutils cpio diffutils fedora-release findutils gawk \
           gcc gcc-c++ grep gzip info make patch redhat-rpm-config rpm-build \
           sed shadow-utils tar unzip util-linux which xz fedora-packager

help:
	@printf 'Usage: sudo make PACKAGE...\n\nPackages:\n'
	@echo $(sort $(PACKAGES)) | tr " " "\n" | column -x; echo

all: $(PACKAGES)

$(PACKAGES): | ~makerpm/rpmbuild
	$(HAVEDEPS) || yum-builddep -qy --noplugins $@.spec
	rm -f $|/SOURCES/master.tar.gz
	spectool -A -g -C $|/SOURCES $@.spec
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
	@test -w ~root || exit 1
	yum -y install $(MINDEPS)
	useradd --system --create-home --groups=mock makerpm || :
	su -c rpmdev-setuptree makerpm

test:
	rpmlint *.rpm

clean:
	rm -f *.rpm


.PHONY: help all install init test clean $(PACKAGES)
