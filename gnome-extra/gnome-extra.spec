Name:           gnome-extra
Version:        0.2
Release:        1%{?dist}
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


%postun
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/glib-2.0/schemas/*.gschema.override
%{_datadir}/gnome-shell/search_providers/google-ssl.xml


%changelog

* Tue Dec 27 2011 Craig Barnes <cr@igbarn.es> - 0.2-1
- Adjust install section to handle updated Makefile
- Adjust files section to include new gnome-shell search provider file
- Bump version

* Sat Dec 24 2011 Craig Barnes <cr@igbarn.es> - 0.1-1
- Initial package
