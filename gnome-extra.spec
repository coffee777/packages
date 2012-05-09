Name:           gnome-extra
Version:        0.0.1
Release:        1%{?dist}
Summary:        Various GNOME applications and preference overrides
License:        GPLv3
URL:            https://bitbucket.org/craigbarnes/packages
BuildArch:      noarch
Source0:        gnome-extra.gschema.override
Source1:        google-ssl.xml

Requires:       epiphany epiphany-extensions
Requires:       inkscape gimp blender
Requires:       gedit-plugins
Requires:       nautilus-open-terminal
Requires:       dconf-editor
Requires:       privoxy
Requires:       emerillon
Requires:       devhelp

%description
This is a meta-package for installing various GNOME applications
and preferences that are not included in Fedora by default.


%prep
cp %{SOURCE0} %{SOURCE1} %{_builddir}


%install
rm -rf %{buildroot}
install -Dpm644 %{SOURCE0} %{buildroot}%{_datadir}/glib-2.0/schemas/gnome-extra.gschema.override
install -Dpm644 %{SOURCE1} %{buildroot}%{_datadir}/gnome-shell/search_providers/google-ssl.xml


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
%{_datadir}/glib-2.0/schemas/gnome-extra.gschema.override
%{_datadir}/gnome-shell/search_providers/google-ssl.xml


%changelog

* Sun May 06 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package (based on previously deleted spec)
