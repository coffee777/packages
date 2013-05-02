Name:           netsurf-buildsystem
Version:        1.0
Release:        1%{?dist}
Summary:        NetSurf shared build system
License:        MIT
URL:            http://git.netsurf-browser.org/buildsystem.git/
Source0:        http://download.netsurf-browser.org/libs/releases/buildsystem-%{version}.tar.gz
BuildArch:      noarch

%description
%{summary}.


%prep
%setup -qn buildsystem-%{version}


%install
%make_install PREFIX=%{_prefix} BASE=%{buildroot}%{_datadir}/%{name}


%files
%doc COPYING README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/makefiles
%dir %{_datadir}/%{name}/testtools
%{_datadir}/%{name}/makefiles/*
%attr(0755, -, -) %{_datadir}/%{name}/testtools/testrunner.pl


%changelog

* Thu May 02 2013 Craig Barnes <cr@igbarn.es> - 1.0-1
- Initial package
