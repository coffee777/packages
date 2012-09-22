VERSION  = 17
TITLE    = Fedora $(VERSION) Remix
PACKAGES = `sed -nr '/^\%packages/,/%end/s/^(\w[A-Za-z0-9_-]+).*/\1/p' $<`
SCTL     = systemctl --quiet 2>/dev/null

desktop thai:
	livecd-creator -c $@.ks -f F$(VERSION)-$@ --tmpdir=tmp --cache=cache \
	--releasever=$(VERSION) --title="$(TITLE)" --product="$(TITLE)"

install: desktop.ks | /etc/rpm/macros.lang /etc/yum.repos.d/rpmfusion-free.repo
	@rpm -q --quiet $(PACKAGES) || yum -y install $(PACKAGES)
	@$(SCTL) is-enabled privoxy.service || $(SCTL) enable privoxy.service
	@$(SCTL) is-active  privoxy.service || $(SCTL) start  privoxy.service
	@echo "OK"

/etc/rpm/macros.lang:
	@echo '%_install_langs en_GB:th_TH' > $@

/etc/yum.repos.d/rpmfusion-free.repo:
	@yum -y --nogpgcheck install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm

check: *.ks
	@for KS in $^; do echo $$KS:; ksvalidator -iv F$(VERSION) $$KS; echo; done

clean:
	rm -rf *.iso tmp cache


.PHONY: install check clean
