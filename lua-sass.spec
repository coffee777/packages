%global         gitcommit e9618a5
Name:           lua-sass
Version:        0.0.1
Release:        1%{?dist}
Summary:        Lua binding to libsass
License:        ISC
URL:            https://github.com/craigbarnes/lua-sass
Source0:        %{url}/tarball/%{gitcommit}

BuildRequires:  libsass-devel%{?_isa} >= 1
BuildRequires:  lua-devel%{?_isa} >= 5.1
Requires:       libsass%{?_isa} >= 1
Requires:       lua%{?_isa} >= 5.1

%description
%{summary}.


%prep
%setup -q -n craigbarnes-lua-sass-%{gitcommit}


%build
make %{?_smp_mflags}


%install
%make_install LIBDIR='%{_libdir}/lua/5.1' CFLAGS='%{optflags} -fPIC'


%check
make test


%files
%doc README.md
%{_libdir}/lua/5.1/sass.so


%changelog

* Fri Oct 19 2012 Craig Barnes <cr@igbarn.es> - 0.0.1-1
- Initial package
