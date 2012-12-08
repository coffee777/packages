Name:           jshon
Version:        0.0.1
Release:        1%{?dist}
Summary:        A JSON parser designed for maximum convenience within the shell
License:        MIT
URL:            https://github.com/keenerd/jshon
Source0:        %{url}/archive/master.tar.gz
BuildRequires:  jansson-devel
Requires:       jansson


%description
%{summary}.


%prep
%setup -q -n %{name}-master


%build
gcc %{optflags} -ljansson -o %{name} %{name}.c


%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog

* Fri Dec 07 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package
