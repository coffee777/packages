Name:           gnome-extra
Version:        0.0.1
Release:        1%{?dist}
Summary:        Various GNOME applications and preference overrides
License:        GPLv3
URL:            https://bitbucket.org/craigbarnes/packages
BuildArch:      noarch
Source0:        gnome-extra.gschema.override
Source1:        google-ssl.xml

%description
This is a meta-package for installing various GNOME applications
and preferences that are not included in Fedora by default.


%prep
cp %{SOURCE0} %{SOURCE1} %{_builddir}


%install
rm -rf %{buildroot}
install -Dpm644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/gnome-extra.gschema.override
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/gnome-shell/search_providers/google-ssl.xml


%postun
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%{_datadir}/glib-2.0/schemas/gnome-extra.gschema.override
%{_datadir}/gnome-shell/search_providers/google-ssl.xml


%changelog

* Sun May 06 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package (based on previously deleted spec)
