dir   = ~makerpm/rpmbuild
spec ?= nginx.spec

get  = $(shell grep -o '$(1)' $(spec) | sed "s|$(1)|\1|")
name = $(call get,Name: \+\(.*\)$)
ver  = $(call get,Version: \+\(.*\)$)
rel  = $(call get,Release: \+\([0-9]\).*$)
os   = fc$(strip $(shell grep -o " 1[0-9] " /etc/issue))
arch = $(shell arch)
src0 = $(shell echo $(call get,Source0: \+\(.*\)$) | sed "s|%{version}|$(ver)|")
srcN = $(call get,Source[1-9]: \+\(.*\)$)

$(name)-$(ver)-$(rel).$(os).$(arch).rpm: $(spec) $(srcN)
	cp $(spec) $(dir)/SPECS
	cp $(srcN) $(dir)/SOURCES
	cd $(dir)/SOURCES && wget $(src0)
	su -c 'cd $(dir) && rpmbuild -ba SPECS/$(spec)' makerpm
	cp $(dir)/RPMS/$(arch)/$@ $@

#TODO: The above recipe makes the assumption that Source0 is a HTTP URI
#      and everything else is a local, relative URI. It should be fixed such
#      that all sources are enumerated and fetched via whatever means relavent.
#      Remote source should *not* be included in the recipe's dependencies.

clean:
	rm -f *.rpm


.PHONY: clean
