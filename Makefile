include /etc/os-release

ifndef VERSION_ID
  $(error Unable to determine version from /etc/os-release)
endif

all:
	@rm -f *-debuginfo-*.rpm
	@mv -f *.src.rpm $(VERSION_ID)/source/ || :
	@mv -f *.i[3456]86.rpm $(VERSION_ID)/i386/ || :
	@git rm -rf $(VERSION_ID)/{source,i386}/repodata || :
	@cd $(VERSION_ID)/source/ && createrepo .
	@cd $(VERSION_ID)/i386/ && createrepo .


.PHONY: all
