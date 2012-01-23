Name:           discount
Version:        2.1.3
Release:        1%{?dist}
Summary:        A command-line utility for converting Markdown files into HTML
License:        BSD
URL:            http://www.pell.portland.or.us/~orc/Code/%{name}

Source0:        %{url}/%{name}-%{version}.tar.bz2
Patch0:         discount-ldconfig.patch

Requires:       libmarkdown%{?_isa} = %{version}-%{release}
BuildRequires:  autoconf

%description
DISCOUNT is an implementation of John Gruber's Markdown language in C.
It includes all of the original Markdown features, along with a few
extensions, and passes the Markdown test suite.


%package -n libmarkdown
Summary: A fast implementation of the Markdown language in C

%description -n libmarkdown
libmarkdown is the library portion of discount, a fast Markdown language
implementation, written in C.


%package -n libmarkdown-devel
Summary: Development headers for the libmarkdown library
Requires: libmarkdown%{?_isa} = %{version}-%{release}

%description -n libmarkdown-devel
This package contains development headers and developer-oriented man pages for
libmarkdown.


%prep
%setup -q
%patch0


%build
./configure.sh \
    --shared \
    --prefix=%{_prefix} \
    --execdir=%{_bindir} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install.everything DESTDIR=%{buildroot}
# Rename markdown binary (clashes with python-markdown)
mv %{buildroot}%{_bindir}/markdown %{buildroot}%{_bindir}/discount
# Rename sample programs (names are too generic)
mv %{buildroot}%{_bindir}/makepage %{buildroot}%{_bindir}/discount-makepage
mv %{buildroot}%{_bindir}/mkd2html %{buildroot}%{_bindir}/discount-mkd2html
mv %{buildroot}%{_bindir}/theme %{buildroot}%{_bindir}/discount-theme
# Rename man1 pages to match their renamed binaries
mv %{buildroot}%{_mandir}/man1/markdown.1 \
   %{buildroot}%{_mandir}/man1/discount.1
mv %{buildroot}%{_mandir}/man1/makepage.1 \
   %{buildroot}%{_mandir}/man1/discount-makepage.1
mv %{buildroot}%{_mandir}/man1/mkd2html.1 \
   %{buildroot}%{_mandir}/man1/discount-mkd2html.1
mv %{buildroot}%{_mandir}/man1/theme.1 \
   %{buildroot}%{_mandir}/man1/discount-theme.1
# Note: Other man pages (including markdown.3 and markdown.7) aren't renamed,
# since python-markdown doesn't ship with any man pages anyway and these pages
# correspond to the libmarkdown library (3) and the markdown format (7)


%post -n libmarkdown -p /sbin/ldconfig
%postun -n libmarkdown -p /sbin/ldconfig


%check
make test


%files
%doc README COPYRIGHT CREDITS
%{_bindir}/discount
%{_bindir}/discount-makepage
%{_bindir}/discount-mkd2html
%{_bindir}/discount-theme
%{_mandir}/man1/discount*.1*
%{_mandir}/man7/*.7*


%files -n libmarkdown
%doc README COPYRIGHT CREDITS
%{_libdir}/libmarkdown.so.*


%files -n libmarkdown-devel
%{_libdir}/libmarkdown.so
%{_includedir}/*
%{_mandir}/man3/*.3*


%changelog

* Sun Jan 22 2012 Craig Barnes <cr@igbarn.es> - 2.1.3-1
- Rename "markdown" binary to "discount" (clashed with python-markdown)
- Prefix all other binaries with "discount-" (names were too generic)
- Rename man1 pages to match their renamed binaries
- Amend patterns in files section to match renamed binaries and man1 pages
- Remove unnecessary, duplicate paragraph from libmarkdown-devel description
- Remove unnecessary "defattr" macros (default behaviour since RPM 4.4)
- Minor formatting clean-ups
- Update to latest upstream release
- Re-generate patch to reflect upstream changes

* Mon Dec 12 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-4
- Split configure script flags across multiple lines for readability
- Add previously missing "--execdir" flag to configure script
- Use make install.everything target instead of specifying 3 separate targets

* Sun Oct 16 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-3
- Get sources from author's website instead of GitHub

* Sat Oct 01 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-2
- Remove unnecessary post/postun sections for base package
- Make base package explicitly depend on libmarkdown

* Wed Sep 28 2011 Craig Barnes <cr@igbarn.es> - 2.1.2-1
- New upstream version
- Add sample programs to the installation

* Mon Sep 26 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-5
- Move man3 pages from libmarkdown to libmarkdown-devel
- Add license document and other basic documentation to libmarkdown

* Sun Sep 25 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-4
- Make libmarkdown-devel explicitly depend on libmarkdown
- Remove unnecessary clean section
- Make pattern matching in file selections more specific
- Move unversioned shared library to libmarkdown-devel package
- Add post and postun sections for running ldconfig
- Add patch to prevent bundled script from running ldconfig itself

* Sun Sep 25 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-3
- Use seperate "libmarkdown" package for shared library
- Move development headers from discount-devel to libmarkdown-devel
- Add clean directive
- Add check directive for running the bundled test suite

* Thu Sep 22 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-2
- Packaged man pages
- Split development files into separate -devel package
- Fixed various rpmlint warnings

* Thu Sep 22 2011 Craig Barnes <cr@igbarn.es> - 2.1.1.3-1
- Initial package.

