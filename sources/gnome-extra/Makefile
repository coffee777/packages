PREFIX = /usr
SCHEMADIR = $(PREFIX)/share/glib-2.0/schemas

apply: gnome-extra.gschema.override
	./apply.awk $<

install: gnome-extra.gschema.override
	install -Dpm0644 $< $(DESTDIR)$(SCHEMADIR)/$<
	glib-compile-schemas $(DESTDIR)$(SCHEMADIR)


.PHONY: apply install
