PACKAGES = $(patsubst %.spec,%,$(wildcard *.spec))
RPMQFMT  = '$|/RPMS/%{arch}/%{name}-%{version}-%{release}.%{arch}.rpm '
SRPMQFMT = '$|/SRPMS/%{name}-%{version}-%{release}.src.rpm '
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
	spectool -A -g -C $|/SOURCES $@.spec
	test ! -d sources/$@ || cp -f sources/$@/* $|/SOURCES/
	cp -f $@.spec $|/SPECS/
	su -c 'cd $| && rpmbuild -ba SPECS/$@.spec' makerpm
	cp `rpmspec -q --qf $(RPMQFMT) $@.spec` .
	cp `rpmspec -q --srpm --qf $(SRPMQFMT) $@.spec` .

sassc: install-libsass
libparserutils: install-netsurf-buildsystem
libhubbub: install-libparserutils
lunamark: lua-bit32 lua-unicode lua-cosmo

# TODO: Only build/install if necessary, not unconditionally
install-%: % | ~makerpm/rpmbuild
	rpm --replacepkgs --replacefiles -Uvh `rpmspec -q --qf $(RPMQFMT) $*.spec`

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


.PHONY: help all init test clean $(PACKAGES)
