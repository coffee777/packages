Name:           lua-json
Version:        1.3
Release:        1%{?dist}
Summary:        JSON parsing and encoding for Lua
License:        MIT
URL:            http://luaforge.net/projects/luajson/
Source0:        https://github.com/downloads/harningt/luajson/luajson-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua >= 5.1, lua-lpeg >= 0.8.1
BuildRequires:  lua-filesystem >= 1.4.1, lua-lunit >= 0.4
Requires:       lua >= 5.1, lua-lpeg >= 0.8.1

%description
LuaJSON is a JSON parser and encoder for Lua, using LPEG for speed and
flexibility.


%prep
%setup -q -n luajson-%{version}


%build


%install
rm -rf %{buildroot}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}


%check
make check-regression
make check-unit | tee testlog.txt
grep -q "0 failed, 0 errors" testlog.txt


%files
%doc README LICENSE docs/LuaJSON.txt docs/ReleaseNotes-%{version}.txt
%dir %{_datadir}/lua/5.1/json
%{_datadir}/lua/5.1/json.lua
%{_datadir}/lua/5.1/json/*


%changelog

* Thu Mar 08 2012 Craig Barnes <cr@igbarn.es> - 1.3-1
- Update to latest stable version
- Update source URL
- Update summary and description based on upstream's own description
- Add README to docs
- Make files section more specific and robust
- Remove ad-hoc build scriptlet and use the provided Makefile
- Remove pointless luadir and luapkgdir macros

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 10 2009 Michel Salim <salimma@fedoraproject.org> - 1.0-1
- Initial package
