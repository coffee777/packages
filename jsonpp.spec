Name:           jsonpp
Version:        1.1.0
Release:        1%{?dist}
Summary:        A fast command line JSON pretty printer
License:        MIT
URL:            https://github.com/jmhodges/jsonpp
Source0:        %{url}/archive/v%{version}.tar.gz
BuildRequires:  gcc-go
Requires:       libgo >= 4.7.2


%description
%{summary}.


%prep
%setup -q


%build
gccgo %{optflags} -o %{name} %{name}.go


%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%doc README.md LICENSE
%{_bindir}/%{name}


%changelog

* Fri Dec 07 2012 Craig Barnes <cr@igbarn.es> - 1.1.0-1
- Initial package
