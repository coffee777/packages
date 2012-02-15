PREFIX  = /etc/privoxy
INSTALL = install -D -p -m 644

user.action: https.action facebook.action
	cat $^ > $@

install: user.action
	$(INSTALL) user.action $(DESTDIR)$(PREFIX)/user.action

clean:
	$(RM) user.action


.PHONY: install uninstall clean
