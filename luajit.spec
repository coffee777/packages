%define beta beta10

Name:       luajit
Version:    2.0.0
Release:    1.%{beta}%{?dist}
Summary:    Just-In-Time Compiler for Lua
License:    MIT
URL:        http://luajit.org/
Source0:    http://luajit.org/download/LuaJIT-%{version}-%{beta}.tar.gz
Requires:   libluajit%{?_isa} = %{version}-%{release}

%description
LuaJIT implements the full set of language features defined by Lua 5.1.
The virtual machine is API- and ABI-compatible to the standard
Lua interpreter and can be deployed as a drop-in replacement.


%package -n libluajit
Summary: Library for LuaJIT
%description -n libluajit
%{summary}


%package -n libluajit-devel
Summary: Development files for libluajit library
Requires: libluajit%{?_isa} = %{version}-%{release}
%description -n libluajit-devel
%{summary}


%prep
%setup -q -n LuaJIT-%{version}-%{beta}


%build
make amalg PREFIX=%{_prefix} CFLAGS="%{optflags}" %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
mv -T %{buildroot}%{_bindir}/luajit-%{version}-%{beta} %{buildroot}%{_bindir}/luajit


%post -n libluajit -p /sbin/ldconfig
%postun -n libluajit -p /sbin/ldconfig


%files
%doc COPYRIGHT README
%{_bindir}/luajit
%{_mandir}/man1/luajit.1.gz


%files -n libluajit
%{_libdir}/libluajit-5.1.so.*
%{_datadir}/%{name}-%{version}-%{beta}/jit/*.lua
%dir %{_datadir}/%{name}-%{version}-%{beta}
%dir %{_datadir}/%{name}-%{version}-%{beta}/jit


%files -n libluajit-devel
%{_libdir}/libluajit-5.1.a
%{_libdir}/libluajit-5.1.so
%{_libdir}/pkgconfig/luajit.pc
%{_includedir}/luajit-2.0/*.h*


%changelog

* Thu May 10 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1.beta10
- Update to latest beta

* Thu Jan 05 2012 Craig Barnes <cr@igbarn.es> - 2.0.0-1.beta9
- Initial package
