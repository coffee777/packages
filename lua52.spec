Name:           lua52
Version:        5.2.1
Release:        1%{?dist}
Summary:        Powerful, fast, lightweight, embeddable scripting language
License:        MIT
URL:            http://www.lua.org
Source0:        %{url}/ftp/lua-%{version}.tar.gz
Source1:        lua52.mk
BuildRequires:  readline-devel ncurses-devel

%description
Lua combines simple procedural syntax with powerful data description
constructs based on associative arrays and extensible semantics. Lua is
dynamically typed, runs by interpreting bytecode for a register-based
virtual machine, and has automatic memory management with incremental
garbage collection, making it ideal for configuration, scripting, and rapid
prototyping.


%prep
%setup -qn lua-%{version}


%build
cd src
cp %{SOURCE1} .
make %{?_smp_mflags} -f lua52.mk CFLAGS='%{optflags} -fPIC'


%install
install -Dpm0755 src/lua %{buildroot}%{_bindir}/lua52
install -Dpm0755 src/liblua-5.2.so %{buildroot}%{_libdir}/liblua-5.2.so
install -Dpm0644 doc/lua.1 %{buildroot}%{_mandir}/man1/lua52.1


%files
%doc doc/*
%{_bindir}/lua52
%{_libdir}/liblua-5.2.so
%{_mandir}/man1/lua52.1*


%changelog

* Tue Mar 05 2013 Craig Barnes <cr@igbarn.es> - 5.2.1-1
- Initial package
