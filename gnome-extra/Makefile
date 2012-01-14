VERSION    = 0.3
SCHEMADIR ?= /usr/share/glib-2.0/schemas
SEARCHDIR ?= /usr/share/gnome-shell/search_providers

install:
	install -m 0755 -p -d $(DESTDIR)$(SCHEMADIR) $(DESTDIR)$(SEARCHDIR)
	install -m 0644 -p *.gschema.override $(DESTDIR)$(SCHEMADIR)
	install -m 0644 -p google-ssl.xml $(DESTDIR)$(SEARCHDIR)

update:
	glib-compile-schemas $(SCHEMADIR)

dist: *.gschema.override google-ssl.xml Makefile README
	tar -czf gnome-extra-$(VERSION).tar.gz $^

clean:
	rm -f *.tar.gz


.PHONY: install update dist clean
