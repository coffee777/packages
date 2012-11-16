VERSION  = 17
TITLE    = Fedora $(VERSION) Remix

PREREQS  = spin-kickstarts pykickstart
PACKAGES = `ksflatten dev.ks | sed -nr '/^%packages/,/^%end/s/^(\w[^ ]+)/\1/p'`
FUSN     = rpmfusion-free-release
URL      = http://download1.rpmfusion.org/free/fedora/$(FUSN)-stable.noarch.rpm
MACROS   = /etc/rpm/macros.lang
SCTL     = systemctl --quiet 2>/dev/null

help:
	@echo 'Usage:  make dev       Create live image from dev.ks'
	@echo '        make thai      Create live image from thai.ks'
	@echo '        make install   Install packages from dev.ks'

install:
	@test -f $(MACROS) || echo '%_install_langs en_GB:th_TH' > $(MACROS)
	@rpm -q --quiet $(PREREQS) || yum -y install $(PREREQS)
	@rpm -q --quiet $(FUSN) || yum -y --nogpgcheck install $(URL)
	@rpm -q --quiet $(PACKAGES) || yum -y install $(PACKAGES)
	@$(SCTL) is-enabled privoxy.service || $(SCTL) enable privoxy.service
	@$(SCTL) is-active  privoxy.service || $(SCTL) start  privoxy.service
	@echo "OK"

dev thai: | /usr/bin/livecd-creator
	livecd-creator -c $@.ks -f F$(VERSION)-$@ --tmpdir=tmp --cache=cache \
	--releasever=$(VERSION) --title="$(TITLE)" --product="$(TITLE)"

/usr/bin/livecd-creator:
	rpm -q --quiet livecd-tools || yum -y install livecd-tools

check:
	@for K in *.ks; do echo $$K:; ksvalidator -iv F$(VERSION) $$K; done

clean:
	rm -rf *.iso tmp cache


.PHONY: help install dev thai check clean
