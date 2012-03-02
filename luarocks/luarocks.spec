Name:           luarocks
Version:        2.0.8
Release:        1%{?dist}
Summary:        Package management system for Lua
Group:          Development/System
License:        MIT
URL:            http://luarocks.org/
Source0:        http://luarocks.org/releases/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  lua-devel >= 5.1
Requires:       lua >= 5.1
Requires:       wget
Requires:       zip

%description
LuaRocks manages the installation, removal and dependency resolution of
Lua "rock" packages. Rocks can be installed either system-wide or per-user.
This package also provides the admin tool for managing a LuaRocks repository.

Note: some packages may require that lua-devel is installed.


%prep
%setup -q -n %{name}-%{version}


%build
./configure \
    --prefix="%{_prefix}" \
    --sysconfdir="%{_sysconfdir}/%{name}/" \
    --with-lua="%{_prefix}" \
    --with-lua-include="%{_includedir}" \
    --with-lua-lib="%{_libdir}" \
    --with-downloader="wget" \
    --with-md5-checker="md5sum" \
    --force-config="%{_prefix}"
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%files
%doc COPYING
%{_bindir}/luarocks
%{_bindir}/luarocks-admin
%dir %{_datadir}/lua/5.1/luarocks
%{_datadir}/lua/5.1/luarocks/*
%dir %{_sysconfdir}/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/config.lua


%changelog

* Fri Mar 02 2012 Craig Barnes <cr@igbarn.es> - 2.0.8-1
- Initial package