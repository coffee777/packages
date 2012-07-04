Name:           lua-manpages
Version:        5.1
Release:        1%{?dist}
Summary:        Manual pages for the Lua C API functions
License:        MIT
URL:            http://zevv.nl/play/code/luaman/
Source0:        http://zevv.nl/play/code/luaman/luaman-5.1.tgz
BuildArch:      noarch

%description
%{summary}.


%prep
%setup -q -n 5.1


%build
# Fix invalid macro
sed -i '51s|\\.)|)\\.|' man3/luaL_Buffer.3


%install
mkdir -p %{buildroot}%{_mandir}/man3
install -pm0644 man3/*.3 %{buildroot}%{_mandir}/man3


%files
%{_mandir}/man3/*.3*


%changelog

* Sun Jun 24 2012 Craig Barnes <cr@igbarn.es> - 5.1-1
- Initial package
