Name:           pngquant
Version:        1.6.2
Release:        1%{?dist}
Summary:        PNG quantization tool for reducing image file size
License:        BSD
URL:            http://pornel.net/pngquant

Source0:        https://github.com/pornel/improved-pngquant/tarball/%{version}
Patch1:         pngquant-buildroot-install.patch

BuildRequires:  libpng-devel%{?_isa} >= 1.2.46-1
BuildRequires:  zlib-devel%{?_isa} >= 1.2.5-5
Requires:       libpng%{?_isa} >= 1.2.46-1
Requires:       zlib%{?isa} >= 1.2.5-5

%description
pngquant converts 24/32-bit RGBA PNG images to 8-bit palette with
alpha channel preserved. Such images are compatible with all modern web
browsers and a compatibility setting is available to help transparency
degrade well in Internet Explorer 6. Quantized files are often 40-70
percent smaller than their 24/32-bit version. pngquant uses the
median cut algorithm.


%prep
%setup -q -n pornel-improved-pngquant-f35a1de
%patch1

%build
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -m 0644 -p -D pngquant.1 %{buildroot}/%{_mandir}/man1/pngquant.1


%files
%doc README.md CHANGELOG COPYRIGHT
%{_bindir}/pngquant
%{_mandir}/man1/pngquant.1.gz


%changelog

* Wed Dec 28 2011 Craig Barnes <cr@igbarn.es> - 1.6.2-1
- Initial package
