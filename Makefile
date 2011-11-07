re1 = Version: \+\(.*\)$
ver = $(shell grep -o '$(re1)' nginx.spec | sed "s|$(re1)|\1|")
re2 = Source0: \+\(.*\)$
url = $(shell grep -o '$(re2)' nginx.spec | sed "s|$(re2)|\1|")
sc0 = $(shell echo $(url) | sed "s|%{version}|$(ver)|")

dist:
	cp nginx.spec ~makerpm/rpmbuild/SPECS
	cp nginx.{conf,service,logrotate} {mime,gzip}.types ~makerpm/rpmbuild/SOURCES
	cd ~makerpm/rpmbuild/SOURCES && wget $(sc0)
	su -c 'cd ~/rpmbuild && rpmbuild -ba SPECS/nginx.spec' makerpm
	cp ~makerpm/rpmbuild/RPMS/i686/nginx-$(ver)-1.fc16.i686.rpm ./
