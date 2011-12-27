VER   = 0.1
DIR  ?= /usr/share/glib-2.0/schemas
FILES = org.gnome.desktop.gschema.override \
        org.gnome.empathy.gschema.override \
        org.gnome.epiphany.gschema.override \
        org.gnome.gedit.gschema.override \
        org.gnome.settings-daemon.peripherals.gschema.override \
        org.gnome.shell.gschema.override

install: $(FILES)
	install -m 0755 -p -d $(DESTDIR)$(DIR)
	install -m 0644 -p $^ $(DESTDIR)$(DIR)

update:
	glib-compile-schemas $(DIR)

dist: $(FILES) Makefile README
	tar -czf gnome-extra-$(VER).tar.gz $^

clean:
	rm -f *.tar.gz


.PHONY: install update dist clean
