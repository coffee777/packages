VERSION  = 17
TITLE    = Fedora $(VERSION) Remix
PACKAGES = `sed -nr '/^\%packages/,/%end/s/^(\w[A-Za-z0-9_-]+).*/\1/p' $<`
SCTL     = systemctl --quiet 2>/dev/null

thai: F$(VERSION)-Thai.iso
desktop: F$(VERSION)-desktop.iso

F$(VERSION)-%.iso: %.ks
	livecd-creator -c $< -f $(@:.iso=) --tmpdir=tmp --cache=cache \
		--releasever=$(VERSION) --title="$(TITLE)" --product="$(TITLE)"

install: desktop.ks | $(FUSIONREPO)
	@rpm -q --quiet $(PACKAGES) || yum -y install $(PACKAGES)
	@$(SCTL) is-enabled privoxy.service || $(SCTL) enable privoxy.service
	@$(SCTL) is-active  privoxy.service || $(SCTL) start  privoxy.service
	@echo "OK"

FUSIONREPO = /etc/yum.repos.d/rpmfusion-free.repo
FUSIONDL = http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm

$(FUSIONREPO):
	@yum -y --nogpgcheck install $(FUSIONDL)

check: *.ks
	@for KS in $^; do echo $$KS:; ksvalidator -iv F$(VERSION) $$KS; echo; done

clean:
	rm -rf *.iso tmp cache


.PHONY: install check clean
