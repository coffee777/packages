dir  = ~makerpm/rpmbuild
get  = $(shell grep -o '$(1)' nginx.spec | sed "s|$(1)|\1|")
name = $(call get,Name: \+\(.*\)$)
ver  = $(call get,Version: \+\(.*\)$)
rel  = $(call get,Release: \+\([0-9]\).*$)
os   = fc$(strip $(shell grep -o " 1[0-9] " /etc/issue))
arch = $(shell arch)
src0 = $(shell echo $(call get,Source0: \+\(.*\)$) | sed "s|%{version}|$(ver)|")

$(name)-$(ver)-$(rel).$(os).$(arch).rpm:
	cp nginx.spec $(dir)/SPECS
	cp nginx.{conf,service,logrotate} {mime,gzip}.types $(dir)/SOURCES
	cd $(dir)/SOURCES && wget $(src0)
	su -c 'cd $(dir) && rpmbuild -ba SPECS/nginx.spec' makerpm
	cp $(dir)/RPMS/$(arch)/$@ $@
