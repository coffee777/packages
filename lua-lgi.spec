Name:           lua-lgi
Version:        0.6.1
Release:        1%{?dist}
Summary:        Dynamic Lua binding to GObject libraries using GObject-Introspection
License:        MIT
URL:            https://github.com/pavouk/lgi
Source0:        https://github.com/downloads/pavouk/lgi/lgi-%{version}.tar.gz
BuildRequires:  gobject-introspection-devel >= 1.30
BuildRequires:  lua-devel >= 5.1
Requires:       gobject-introspection >= 1.30
Requires:       lua >= 5.1

%description
LGI is gobject-introspection based dynamic Lua binding to GObject based
libraries. It allows using GObject-based libraries directly from Lua.

LGI is tested and compatible with standard Lua 5.1 and Lua 5.2 and recent
LuaJIT 2 betas. Compatibility with other Lua implementations is not tested
yet.


%prep
%setup -q -n lgi-%{version}


%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}


%files
%doc LICENSE README.md docs/*.md
%dir %{_libdir}/lua/5.1/lgi
%dir %{_datadir}/lua/5.1/lgi
%dir %{_datadir}/lua/5.1/lgi/override
%{_libdir}/lua/5.1/lgi/corelgilua51.so
%{_datadir}/lua/5.1/lgi.lua
%{_datadir}/lua/5.1/lgi/*.lua
%{_datadir}/lua/5.1/lgi/override/*.lua


%changelog

* Wed Jun 20 2012 Craig Barnes <cr@igbarn.es> - 0.6.1-1
- Update to latest release

* Sun Mar 04 2012 Craig Barnes <cr@igbarn.es> - 0.4-1
- Initial package
