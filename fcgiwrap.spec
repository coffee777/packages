%global         gitcommit 1328862
Name:           fcgiwrap
Version:        1.0.3
Release:        2.git%{gitcommit}%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
License:        MIT
URL:            http://nginx.localdomain.pl/

Source0:        https://github.com/gnosek/fcgiwrap/tarball/%{gitcommit}
Source1:        fcgiwrap.service

BuildRequires:      autoconf
BuildRequires:      fcgi-devel
Requires:           spawn-fcgi
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

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
make install DESTDIR=%{buildroot}
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/fcgiwrap.service


%post
%systemd_post fcgiwrap.service

%preun
%systemd_preun fcgiwrap.service

%postun
%systemd_postun_with_restart fcgiwrap.service


%files
%doc README.rst
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*
%{_unitdir}/fcgiwrap.service


%changelog

* Sun Mar 17 2013 Craig Barnes <cr@igbarn.es> - 1.0.3-2.git1328862
- Use systemd macro scriptlets

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.0.3-1.git1328862
- Initial package
