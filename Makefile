include /etc/os-release

all:
	@rm -f *-debuginfo-*.rpm
	@mv -f *.src.rpm $(VERSION_ID)/source/ || :
	@mv -f *.i[3456]86.rpm $(VERSION_ID)/i386/ || :
	@git rm -rf $(VERSION_ID)/{source,i386}/repodata || :
	@cd $(VERSION_ID)/source/ && createrepo .
	@cd $(VERSION_ID)/i386/ && createrepo .
	@git add $(VERSION_ID)/{source,i386}/repodata


ifndef VERSION_ID
  $(error Unable to determine version from /etc/os-release)
endif

ifeq ($(shell test -z '$(wildcard *.rpm)' && echo 1),1)
  $(error No RPMs)
endif

.PHONY: all
