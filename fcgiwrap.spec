%global         gitcommit 1328862
Name:           fcgiwrap
Version:        1.0.3
Release:        1.git%{gitcommit}%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
License:        MIT
URL:            http://nginx.localdomain.pl/

Source0:        https://github.com/gnosek/fcgiwrap/tarball/%{gitcommit}
Source1:        fcgiwrap.service

BuildRequires:      autoconf
BuildRequires:      fcgi-devel
Requires:           spawn-fcgi
Requires(post):     systemd-units
Requires(preun):    systemd-units
Requires(postun):   systemd-units

%description
fcgiwrap is a simple server for running CGI applications over FastCGI.
It hopes to provide clean CGI support to Nginx (and other web servers
that may need it).


%prep
%setup -q -n gnosek-fcgiwrap-%{gitcommit}


%build
autoreconf -i
%configure
# Bug: prefix erroneously added to absolute sbindir resulting in /usr/usr/sbin
sed -i '1,2s|/usr/usr|/usr|g' Makefile
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/fcgiwrap.service


%post
if [ $1 -eq 1 ]; then
    /bin/systemctl daemon-reload &>/dev/null || :
fi


%preun
if [ $1 -eq 0 ]; then
    /bin/systemctl --no-reload disable fcgiwrap.service &>/dev/null || :
    /bin/systemctl stop fcgiwrap.service &>/dev/null || :
fi


%postun
/bin/systemctl daemon-reload &>/dev/null || :
if [ $1 -ge 1 ]; then
    /bin/systemctl try-restart fcgiwrap.service &>/dev/null || :
fi


%files
%doc README.rst
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*
%{_unitdir}/fcgiwrap.service


%changelog

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.0.3-1.git1328862
- Initial package
