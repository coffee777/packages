Name:           weighttp
Version:        0.3
Release:        1%{?dist}
Summary:        Lightweight and small benchmarking tool for webservers
License:        MIT
URL:            http://redmine.lighttpd.net/projects/weighttp/wiki
Source0:        http://cgit.lighttpd.net/weighttp/snapshot/weighttp-1bdbe4003c8d7d61568ed45548fccf354ab19018.tar.gz
BuildRequires:  libev-devel python

%description
weighttp (pronounced weighty) is a lightweight and small
benchmarking tool for webservers. It was designed to be very fast and
easy to use and only supports a tiny fraction of the HTTP protocol in
order to be lean and simple. weighttp supports multithreading to make
good use of modern CPUs with multiple cores as well as asynchronous i/o
for concurrent requests within a single thread.


%prep
%setup -q -n %{name}-1bdbe4003c8d7d61568ed45548fccf354ab19018


%build
# TODO: waf only looks for ev.h in /usr/include but Fedora has it
# in /usr/include/libev
# ---
# Why do these moron hipsters insist on using broken build systems built
# by other moron hipsters, just to build a few hundred lines of C?!
# --
# Temporary fix was to symlink it until I can figure out how to
# patch or configure this nasty build system
./waf configure --prefix=%{_prefix}
./waf build


%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot}


%files
%doc COPYING README TODO
%{_bindir}/weighttp


%changelog

* Fri Jan 06 2012 Craig Barnes <cr@igbarn.es> - 0.3-1
- Initial package
