%global         commit 35d2664135c5f62c123535eda4edb0e888d6452a
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           pngquant
Version:        1.8.1
Release:        1%{?dist}
Summary:        PNG quantization tool for reducing image file size
License:        BSD
URL:            http://pngquant.org/
Source0:        https://github.com/pornel/improved-pngquant/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildRequires:  libpng-devel zlib-devel

%description
pngquant converts 24/32-bit RGBA PNG images to 8-bit palette with
alpha channel preserved. Such images are compatible with all modern web
browsers and a compatibility setting is available to help transparency
degrade well in Internet Explorer 6. Quantized files are often 40-70
percent smaller than their 24/32-bit version. pngquant uses the
median cut algorithm.


%prep
%setup -qn improved-pngquant-%{commit}


%build
make %{?_smp_mflags} CFLAGSADD='%{optflags}'


%install
%make_install PREFIX=%{_prefix}
install -Dpm0644 pngquant.1 %{buildroot}%{_mandir}/man1/pngquant.1


%files
%doc README.md CHANGELOG COPYRIGHT
%{_bindir}/pngquant
%{_mandir}/man1/pngquant.1*


%changelog

* Thu Jan 10 2013 Craig Barnes <cr@igbarn.es> - 1.8.1-1
- Update to latest stable release
- Conform to Fedora packaging guidelines for GitHub
- Build with optflags
- Remove slash between buildroot and _mandir macros
- Use make_install macro
- Update to new project URL

* Thu May 03 2012 Craig Barnes <cr@igbarn.es> - 1.7.2-1
- Update to latest upstream version

* Sun Jan 15 2012 Craig Barnes <cr@igbarn.es> - 1.7.0-1
- Update to latest upstream version

* Mon Jan 09 2012 Craig Barnes <cr@igbarn.es> - 1.6.4-1
- Update to latest version
- Remove Makefile patch (merged upstream)
- Use prefix macro when installing (upstream changed the default prefix)

* Wed Dec 28 2011 Craig Barnes <cr@igbarn.es> - 1.6.2-1
- Initial package
