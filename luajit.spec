Name:       luajit
Version:    2.0.2
Release:    2%{?dist}
Summary:    Just-In-Time Compiler for Lua
License:    MIT
URL:        http://luajit.org/
Source0:    http://luajit.org/download/LuaJIT-%{version}.tar.gz
Requires:   libluajit%{?_isa} = %{version}-%{release}

%description
LuaJIT implements the full set of language features defined by Lua 5.1.
The virtual machine is API- and ABI-compatible to the standard
Lua interpreter and can be deployed as a drop-in replacement.


%package -n libluajit
Summary: Library for LuaJIT
%description -n libluajit
%{summary}.


%package -n libluajit-static
Summary: Static library for LuaJIT
%description -n libluajit-static
%{summary}.


%package -n libluajit-devel
Summary: Development files for libluajit
Requires: libluajit%{?_isa} = %{version}-%{release}
%description -n libluajit-devel
%{summary}.


%prep
%setup -q -n LuaJIT-%{version}


%build
make amalg PREFIX=%{_prefix} TARGET_STRIP=@: \
           CFLAGS='%{optflags} -DLUAJIT_ENABLE_LUA52COMPAT'


%install
%make_install PREFIX=%{_prefix} INSTALL_LIB=%{buildroot}%{_libdir}
mv -T %{buildroot}%{_bindir}/luajit-%{version} %{buildroot}%{_bindir}/luajit
# Add binfmt_misc configuration to binfmt.d(5) directory
mkdir -p %{buildroot}%{_libdir}/binfmt.d
echo ':luajit:M::\x1b\x4c\x4a::%{_bindir}/luajit:' > \
      %{buildroot}%{_libdir}/binfmt.d/luajit.conf


%post -n libluajit -p /sbin/ldconfig
%postun -n libluajit -p /sbin/ldconfig


%files
%doc COPYRIGHT README doc/*
%{_bindir}/luajit
%{_mandir}/man1/luajit.1.gz
%{_libdir}/binfmt.d/luajit.conf


%files -n libluajit
%{_libdir}/libluajit-5.1.so.*
%{_datadir}/%{name}-%{version}/jit/*.lua
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/jit


%files -n libluajit-static
%{_libdir}/libluajit-5.1.a


%files -n libluajit-devel
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc
%{_includedir}/luajit-2.0/*.h*


%changelog

* Wed Jun 05 2013 Craig Barnes <cr@igbarn.es> - 2.0.2-2
- Specify libdir explicitly instead of relying on the Makefile default

* Mon Jun 03 2013 Craig Barnes <cr@igbarn.es> - 2.0.2-1
- Update to latest release
- Drop hotfix patch for previous release
- Disable "TARGET_STRIP" to keep debugging symbols intact

* Sat Mar 09 2013 Craig Barnes <cr@igbarn.es> - 2.0.1-1
- Update to latest release
- Add hotfix patch for latest release

* Sun Feb 03 2013 Craig Barnes <cr@igbarn.es> - 2.0.0-3
- Add binfmt_misc configuration to binfmt.d(5) directory

* Fri Jan 25 2013 Craig Barnes <cr@igbarn.es> - 2.0.0-2
- Use -DLUAJIT_ENABLE_LUA52COMPAT for build, not installation
- Remove smp_mflags from build section (not useful for amalg target)

* Tue Nov 13 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1
- Update to stable release
- Include doc directory in base package

* Wed Nov 07 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1.rc2
- Update to latest release candidate
- Drop hotfix patch
- Remove beta suffix from installation paths
- Add -DLUAJIT_ENABLE_LUA52COMPAT to XCFLAGS, to enable some Lua 5.2 features

* Fri Oct 26 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1.beta11
- Update to latest beta
- Add latest hotfix patch
- Split static library into separate libluajit-static package

* Thu May 10 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1.beta10
- Update to latest beta

* Thu Jan 05 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1.beta9
- Initial package
