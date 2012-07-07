FUSIONDL = http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm
PACKAGES = `sed -nr '/^\%packages/,/%end/s/^(\w[A-Za-z0-9_-]+).*/\1/p' $<`
EXCLUDED = `sed -nr '/^\%packages/,/%end/s/^-([A-Za-z0-9_-]+).*/\1/p' $<`
RPMQ     = rpm -q --quiet
SCTL     = systemctl --quiet 2>/dev/null

install: desktop.ks
	@! $(RPMQ) $(EXCLUDED) || yum -y remove $(EXCLUDED)
	@$(RPMQ) rpmfusion-free-release || yum -y --nogpgcheck install $(FUSIONDL)
	@$(RPMQ) $(PACKAGES) || yum -y install $(PACKAGES)
	@$(SCTL) is-enabled privoxy.service || $(SCTL) enable privoxy.service
	@$(SCTL) is-active  privoxy.service || $(SCTL) start  privoxy.service
	@echo "OK"


.PHONY: install
