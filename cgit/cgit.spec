%global make_cgit \
export CFLAGS="%{optflags}" \
make V=1 %{?_smp_mflags} \\\
    DESTDIR=%{buildroot} \\\
    INSTALL="install -p"  \\\
    CACHE_ROOT=%{_localstatedir}/cache/cgit \\\
    CGIT_SCRIPT_PATH=%{_localstatedir}/www/cgi-bin \\\
    CGIT_SCRIPT_NAME=cgit \\\
    CGIT_DATA_PATH=%{_datadir}/cgit \\\
    docdir=%{docdir} \\\
    filterdir=%{_libexecdir}/cgit/filters

Name:           cgit
Version:        0.9.0.2
Release:        1%{?dist}
Summary:        Fast web interface for git
Group:          Development/Tools
License:        GPLv2
URL:            http://hjemli.net/git/cgit/

Source0:        http://hjemli.net/git/cgit/snapshot/cgit-%{version}.tar.bz2
Source1:        http://hjemli.net/git/git/snapshot/git-1.7.4.tar.bz2
Source2:        cgitrc
Source3:        cgit.nginx
Patch0:         0001-Fix-potential-XSS-vulnerability-in-rename-hint.patch

Requires:       nginx
Requires:       spawn-fcgi
Requires:       fcgiwrap

BuildRequires:  asciidoc
BuildRequires:  libcurl-devel
BuildRequires:  openssl-devel

%description
Cgit is a fast web interface for git.  It uses caching to increase performance.


%prep
%setup -q -a 1
%patch0 -p1

# Set up the git dir
rm -rf git
mv git-1.7.4 git
sed -i 's/^\(CFLAGS = \).*/\1%{optflags}/' git/Makefile


%build
%{make_cgit}

# Something in the a2x chain doesn't like running in parallel
%{make_cgit} -j1 doc-man doc-html


%install
rm -rf %{buildroot}
%{make_cgit} install install-man
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/cgitrc
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/nginx/conf.d/cgit.conf
install -d -m0755 %{buildroot}%{_localstatedir}/cache/cgit


%files
%doc COPYING README *.html
%config(noreplace) %{_sysconfdir}/cgitrc
%config(noreplace) %{_sysconfdir}/nginx/conf.d/cgit.conf
%dir %attr(-,nginx,root) %{_localstatedir}/cache/cgit
%{_datadir}/cgit
%{_libexecdir}/cgit/filters
%{_localstatedir}/www/cgi-bin/cgit
%{_mandir}/man5/cgitrc.5*


%changelog

* Thu Jan 12 2012 Craig Barnes <cr@igbarn.es> - 0.9.0.2-1
- Import from Fedora default packages
- Make files selection more explicit
- Remove legacy support (buildroot/clean, defattr, conditionals etc.)
- Remove unnecessary global macros
- Remove README.SELinux
- Remove Apache configuration
- Add Nginx configuration
- Change git source to hjemli.net -- kernel.org tarballs are all messed up
