VER := $(shell sed -nr "s/^Version:[[:space:]]*([0-9.]+).*/\1/p" nginx.spec)
REL := $(shell sed -nr "s/^Release:[[:space:]]*([0-9]+).*/\1/p" nginx.spec)
SRC := $(shell sed -nr "s/^Source0?:[[:space:]]*(.*)/\1/p" nginx.spec)
SRC := $(subst %{version},$(VER),$(SRC))
ARCH = $(shell arch)

TARBALL = ~makerpm/rpmbuild/SOURCES/$(notdir $(SRC))

FILES = nginx.conf default.conf gzip.types mime.types \
        nginx.logrotate nginx.service

package: $(FILES) $(TARBALL) nginx.spec
	cp -f $(FILES) ~makerpm/rpmbuild/SOURCES/
	cp -f nginx.spec ~makerpm/rpmbuild/SPECS/
	su -c 'cd ~/rpmbuild && rpmbuild -ba SPECS/nginx.spec' makerpm
	cp -f ~makerpm/rpmbuild/RPMS/$(ARCH)/nginx-$(VER)-$(REL).*.$(ARCH).rpm ./

$(TARBALL):
	cd ~makerpm/rpmbuild/SOURCES/ && wget $(SRC)

test: nginx.spec
	rpmlint $^

clean:
	rm -f *.rpm


.PHONY: package test clean
