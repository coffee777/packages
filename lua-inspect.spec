Name:           lua-inspect
Version:        1.1.1
Release:        1%{?dist}
Summary:        Human-readable representation of Lua tables
License:        BSD
URL:            https://github.com/kikito/inspect.lua
Source0:        %{url}/tarball/%{version}
BuildArch:      noarch
Requires:       lua

%description
Module for printing a human-readable representation of Lua tables.
The objective is to allow quick inspection of nested tables, not
serialization or compactness.


%prep
%setup -q -n kikito-inspect.lua-13ced72


%install
install -Dpm644 inspect.lua %{buildroot}%{_datadir}/lua/5.1/inspect.lua


%files
%doc README.textile BSD-LICENSE.txt
%{_datadir}/lua/5.1/inspect.lua


%changelog

* Sun May 13 2012 Craig Barnes <cr@igbarn.es> - 1.1.1-1
- Initial package
