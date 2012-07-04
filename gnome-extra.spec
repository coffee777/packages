Name:           gnome-extra
Version:        0.0.3
Release:        1%{?dist}
Summary:        GNOME preference overrides
License:        GPLv3
URL:            https://bitbucket.org/craigbarnes/packages
BuildArch:      noarch
Source0:        gnome-extra.gschema.override
Source1:        google-ssl.xml

%description
Custom GNOME preference overrides and Open Search providers.


%prep
cp %{SOURCE0} %{SOURCE1} %{_builddir}


%install
install -Dpm644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/gnome-extra.gschema.override
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/gnome-shell/open-search-providers/google-ssl.xml


%postun
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files
%{_datadir}/glib-2.0/schemas/gnome-extra.gschema.override
%{_datadir}/gnome-shell/open-search-providers/google-ssl.xml


%changelog

* Fri Jun 15 2012 Craig Barnes <cr@igbarn.es> - 0.0.3-1
- Disable Google autocomplete in search provider URLs

* Wed May 30 2012 Craig Barnes <cr@igbarn.es> - 0.0.2-1
- Update install location (search_providers -> open-search-providers)

* Sun May 06 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package (based on previously deleted spec)
