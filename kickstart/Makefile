VERSION = 18
TITLE   = Fedora $(VERSION) Remix

REPOS   = /etc/yum.repos.d/google-chrome.repo \
          /etc/yum.repos.d/google-talkplugin.repo \
          /etc/yum.repos.d/rpmfusion-free.repo

help:
	@echo 'Usage:  make dev       Create live image from dev.ks'
	@echo '        make thai      Create live image from thai.ks'
	@echo '        make install   Install packages from dev.ks'

install: desktop.ks dev.ks | /etc/rpm/macros.lang $(REPOS)
	@yum -y install `sed -nr '/^%packages/,/^%end/s/^(\w[^ ]+)/\1/p' $^`

erase: desktop.ks dev.ks
	@yum erase `sed -nr '/^%packages/,/^%end/s/^-(\w[^ ]+)/\1/p' $^`

privoxy:
	@yum -y install privoxy
	@systemctl --quiet start  privoxy.service
	@systemctl --quiet enable privoxy.service

dev thai: | /usr/bin/livecd-creator /usr/share/spin-kickstarts/
	livecd-creator -c $@.ks -f F$(VERSION)-$@ --tmpdir=tmp --cache=cache \
	--releasever=$(VERSION) --title="$(TITLE)" --product="$(TITLE)"

/etc/rpm/macros.lang:
	@echo '%_install_langs en_GB:th_TH' > $@

/etc/yum.repos.d/rpmfusion-free.repo:
	@yum -y --nogpgcheck localinstall http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(VERSION).noarch.rpm

/etc/yum.repos.d/%.repo: %.repo
	@install -Dm0644 $< $@

/usr/bin/livecd-creator:
	@yum -y install livecd-tools

/usr/share/spin-kickstarts/:
	@yum -y install spin-kickstarts

check:
	@rpm -q --quiet pykickstart || yum -y install pykickstart
	@for K in *.ks; do echo $$K:; ksvalidator -iv F$(VERSION) $$K; done

clean:
	rm -rf *.iso tmp cache


.PHONY: help install erase privoxy dev thai check clean
