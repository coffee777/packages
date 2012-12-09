Name:           lua-date
Version:        0.0.1
Release:        1%{?dist}
Summary:        Serialized date parsing for Lua
License:        MIT
URL:            https://github.com/craigbarnes/lua-date
Source0:        %{url}/archive/master.tar.gz
BuildArch:      noarch
BuildRequires:  lua >= 5.1, lua-lpeg >= 0.8.1
Requires:       lua >= 5.1, lua-lpeg >= 0.8.1

%description
%{summary}.


%prep
%setup -q -n %{name}-master


%install
%make_install LUADIR=%{_datadir}/lua/5.1


%check
make test


%files
%{_datadir}/lua/5.1/rfc3339.lua


%changelog

* Sun Dec 09 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package
