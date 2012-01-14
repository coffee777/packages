Name:           gnome-extra
Version:        0.3
Release:        2%{?dist}
Summary:        Various GNOME desktop/application preference overrides
License:        GPLv3
URL:            https://bitbucket.org/craigbarnes/packages
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

Requires:       epiphany epiphany-extensions
Requires:       inkscape
Requires:       gedit-plugins
Requires:       nautilus-open-terminal
Requires:       dconf-editor
Requires:       privoxy

Obsoletes:      gnome-games
Obsoletes:      aisleriot
Obsoletes:      sound-juicer
Obsoletes:      PackageKit-command-not-found
Obsoletes:      gnome-mplayer

%description
Many GNOME applications allow GSettings to centrally manage and store their
configuration settings. The default configuration of most applications
is typically minimalist and it is generally left to the user to further
configure things themself manually.

This package is a set of opinionated but tasteful default settings for
a number of the most useful and commonly used GNOME applications. It also
acts as a "meta-package" for installing a number of very useful applications
that are usually not included as part of a LiveCD installation.


%prep
%setup -q -c %{name}-%{version}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} \
             SCHEMADIR=%{_datadir}/glib-2.0/schemas \
             SEARCHDIR=%{_datadir}/gnome-shell/search_providers


%post
if [ $1 -eq 1 ]; then
    # F16 ships an old SysV init script for Privoxy and systemctl interface
    # just gives an error. Use chkconfig for now and change when privoxy
    # is shipped with native systemd unit file (F17?)
    /sbin/chkconfig privoxy on &>/dev/null || :
    /sbin/service privoxy start &>/dev/null || :
fi


%postun
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%doc README
%{_datadir}/glib-2.0/schemas/*.gschema.override
%{_datadir}/gnome-shell/search_providers/google-ssl.xml


%changelog

* Sat Jan 14 2012 Craig Barnes <cr@igbarn.es> - 0.3-2
- Silence post-install script output

* Sat Jan 14 2012 Craig Barnes <cr@igbarn.es> - 0.3-1
- Add Privoxy to dependencies
- Add gschema override to set Privoxy as http and https proxy

* Tue Dec 27 2011 Craig Barnes <cr@igbarn.es> - 0.2-1
- Adjust install section to handle updated Makefile
- Adjust files section to include new gnome-shell search provider file
- Bump version

* Sat Dec 24 2011 Craig Barnes <cr@igbarn.es> - 0.1-1
- Initial package
