Name:           lua-unicode
Version:        1.1
Release:        1%{?dist}
Summary:        Unicode support library for Lua
License:        MIT
URL:            http://luaforge.net/projects/sln/

Source0:        http://luaforge.net/frs/download.php/1693/slnunicode-%{version}.tar.bz2
Patch0:         lua-unicode-1.1.patch

BuildRequires:  lua-devel >= 5.1
Requires:       lua >= 5.1

%description
slnunicode is a Unicode support library for Lua, developed for the Selene
database project.


%prep
%setup -q -n slnunicode-%{version}
%patch0


%build
gcc %{optflags} -fPIC -I%{_includedir} -c slnunico.c -o ./slnunico.o
gcc %{optflags} -fPIC -I%{_includedir} -c slnudata.c -o ./slnudata.o
gcc -shared -o unicode.so -L%{_libdir} slnunico.o ./slnudata.o


%install
install -Dpm0755 unicode.so %{buildroot}%{_libdir}/lua/5.1/unicode.so


%files
%{_libdir}/lua/5.1/unicode.so


%changelog

* Mon Mar 12 2012 Craig Barnes <cr@igbarn.es> - 1.1-1
- Initial package
