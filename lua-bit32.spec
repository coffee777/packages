Name:           lua-bit32
Version:        5.2.0.a1
Release:        1%{?dist}
Summary:        Lua 5.2 bit manipulation library
License:        MIT
URL:            http://smbolton.com/lua.html
Source0:        http://smbolton.com/lua/lbitlib-5.2.0-alpha-backport1.c

BuildRequires:  lua-devel >= 5.1
Requires:       lua >= 5.1

%description
bit32 is the native Lua 5.2 bit manipulation library, backported to Lua 5.1


%prep
cp %{SOURCE0} %{_builddir}/bit32.c


%build
gcc %{optflags} -fPIC -I%{_includedir} -c bit32.c -o bit32.o
gcc -shared -fPIC -o bit32.so -L%{_libdir} bit32.o


%install
install -Dpm0755 bit32.so %{buildroot}%{_libdir}/lua/5.1/bit32.so


%files
%{_libdir}/lua/5.1/bit32.so


%changelog

* Mon Mar 12 2012 Craig Barnes <cr@igbarn.es> - 5.2.0.a1-1
- Initial package
