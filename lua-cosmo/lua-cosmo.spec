Name:      lua-cosmo
Version:   10.04.06
Release:   1%{?dist}
Summary:   Safe templates for Lua
License:   MIT
URL:       http://cosmo.luaforge.net
Source0:   http://github.com/downloads/mascarenhas/cosmo/cosmo-%{version}.tar.gz
BuildArch: noarch
Requires:  lua-lpeg

%description
Cosmo is a "safe templates" engine. It allows you to fill nested templates,
providing many of the advantages of Turing-complete template engines,
without without the downside of allowing arbitrary code in the templates.


%prep
%setup -q -n cosmo-%{version}


%install
rm -rf %{buildroot}
install -d -m 755     %{buildroot}%{_datadir}/lua/5.1/cosmo
install -p -m 644 -t  %{buildroot}%{_datadir}/lua/5.1        src/cosmo.lua
install -p -m 644 -t  %{buildroot}%{_datadir}/lua/5.1/cosmo  src/cosmo/*.lua


%files
%doc README doc/cosmo.png doc/index.html samples/sample.lua
%dir %{_datadir}/lua/5.1/cosmo
%{_datadir}/lua/5.1/cosmo.lua
%{_datadir}/lua/5.1/cosmo/fill.lua
%{_datadir}/lua/5.1/cosmo/grammar.lua


%changelog

* Fri Mar 02 2012 Craig Barnes <cr@igbarn.es> - 10.04.06-1
- Initial package (manually translated from rockspec)
