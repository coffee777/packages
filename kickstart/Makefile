FUSIONDL = http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm
PACKAGES = `sed -nr '/^\%packages/,/%end/s/^(\w[A-Za-z0-9_-]+).*/\1/p' $<`
EXCLUDED = `sed -nr '/^\%packages/,/%end/s/^-([A-Za-z0-9_-]+).*/\1/p' $<`

install: desktop.ks
	@-yum -y --nogpgcheck install $(FUSIONDL)
	@yum -y remove  $(EXCLUDED)
	@yum -y install $(PACKAGES)
	@systemctl is-enabled privoxy.service || systemctl enable privoxy.service
	@systemctl is-active  privoxy.service || systemctl start  privoxy.service


.PHONY: install
