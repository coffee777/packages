VERSION  = 17
TITLE    = Fedora $(VERSION) Remix

PACKAGES = $(shell sed -nr '/^%packages/,/^%end/s/^(\w[^ ]+)/\1/p' desktop.ks)
FUSN     = rpmfusion-free-release
URL      = http://download1.rpmfusion.org/free/fedora/$(FUSN)-stable.noarch.rpm
MACROS   = /etc/rpm/macros.lang
SCTL     = systemctl --quiet 2>/dev/null

install:
	@test -f $(MACROS) || echo '%_install_langs en_GB:th_TH' > $(MACROS)
	@rpm -q --quiet $(FUSN) || yum -y --nogpgcheck install $(URL)
	@rpm -q --quiet $(PACKAGES) || yum -y install $(PACKAGES)
	@$(SCTL) is-enabled privoxy.service || $(SCTL) enable privoxy.service
	@$(SCTL) is-active  privoxy.service || $(SCTL) start  privoxy.service
	@echo "OK"

desktop thai:
	livecd-creator -c $@.ks -f F$(VERSION)-$@ --tmpdir=tmp --cache=cache \
	--releasever=$(VERSION) --title="$(TITLE)" --product="$(TITLE)"

check: *.ks
	@for KS in $^; do echo $$KS:; ksvalidator -iv F$(VERSION) $$KS; echo; done

clean:
	rm -rf *.iso tmp cache


.PHONY: install check clean
