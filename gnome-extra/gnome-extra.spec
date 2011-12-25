Name:           gnome-extra
Version:        0.1
Release:        1%{?dist}
Summary:        Various GNOME desktop/application preference overrides
License:        GPLv3
URL:            https://bitbucket.org/craigbarnes/packages
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

#Requires:       

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
make install DESTDIR=%{buildroot} DIR=%{_datadir}/glib-2.0/schemas


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


%changelog

* Sat Dec 24 2011 Craig Barnes <cr@igbarn.es> - 0.1-1
- Initial package
