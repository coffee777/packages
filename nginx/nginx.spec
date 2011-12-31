Name:               nginx
Version:            1.1.12
Release:            1%{?dist}
Summary:            High performance HTTP and reverse proxy server
License:            BSD
URL:                http://nginx.org/

Source0:            http://nginx.org/download/nginx-%{version}.tar.gz
Source1:            nginx.service
Source2:            nginx.logrotate
Source3:            nginx.conf
Source4:            mime.types
Source5:            gzip.types
Source6:            default.conf

BuildRequires:      pcre-devel,zlib-devel,openssl-devel
Requires:           pcre,openssl,logrotate
Requires(post):     systemd-units
Requires(preun):    systemd-units
Requires(postun):   systemd-units

%description
Nginx [engine x] is a HTTP(S) server, HTTP(S) reverse proxy and IMAP/POP3
proxy server written by Igor Sysoev.


%prep
%setup -q


%build
./configure \
    --user=nginx \
    --group=nginx \
    --prefix=%{_datadir}/nginx \
    --sbin-path=%{_sbindir}/nginx \
    --conf-path=%{_sysconfdir}/nginx/nginx.conf \
    --error-log-path=%{_localstatedir}/log/nginx/error.log \
    --http-log-path=%{_localstatedir}/log/nginx/access.log \
    --http-client-body-temp-path=%{_sharedstatedir}/nginx/body \
    --pid-path=/run/nginx.pid \
    --lock-path=%{_localstatedir}/lock/subsys/nginx \
    --with-http_ssl_module \
    --with-http_gzip_static_module \
    --with-file-aio \
    --with-ipv6 \
    --with-pcre-jit \
    --with-cc-opt="%{optflags} $(pcre-config --cflags)" \
    --without-http_access_module \
    --without-http_auth_basic_module \
    --without-http_autoindex_module \
    --without-http_browser_module \
    --without-http_charset_module \
    --without-http_empty_gif_module \
    --without-http_fastcgi_module \
    --without-http_geo_module \
    --without-http_limit_req_module \
    --without-http_limit_zone_module \
    --without-http_map_module \
    --without-http_memcached_module \
    --without-http_proxy_module \
    --without-http_scgi_module \
    --without-http_split_clients_module \
    --without-http_ssi_module \
    --without-http_upstream_ip_hash_module \
    --without-http_userid_module \
    --without-http_uwsgi_module
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
chmod 0755 %{buildroot}%{_sbindir}/nginx
rm %{buildroot}/%{_sysconfdir}/nginx/fastcgi.conf
rm %{buildroot}/%{_sysconfdir}/nginx/*.default
rm %{buildroot}/%{_sysconfdir}/nginx/{fastcgi,scgi,uwsgi}_params
rm %{buildroot}/%{_sysconfdir}/nginx/{win-utf,koi-utf,koi-win}
gzip -9 objs/nginx.8
install -p -D -m 0644 objs/nginx.8.gz %{buildroot}%{_mandir}/man8/nginx.8.gz
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/nginx.service
install -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/nginx
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/nginx/conf.d/default.conf
install -p -m 0644 %{SOURCE3} %{SOURCE4} %{SOURCE5} %{buildroot}%{_sysconfdir}/nginx/
install -p -d -m 0755 %{buildroot}%{_sharedstatedir}/nginx
install -p -d -m 0755 %{buildroot}%{_localstatedir}/log/nginx
install -p -d -m 0755 %{buildroot}%{_datadir}/nginx/html


%pre
if [ $1 -eq 1 ]; then
    useradd -s /bin/false -r -d %{_sharedstatedir}/nginx nginx &>/dev/null || :
fi

%post
if [ $1 -eq 1 ]; then
    /bin/systemctl daemon-reload &>/dev/null || :
fi

%preun
if [ $1 -eq 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable nginx.service &>/dev/null || :
    /bin/systemctl stop nginx.service &>/dev/null || :
fi

%postun
/bin/systemctl daemon-reload &>/dev/null || :
if [ $1 -ge 1 ]; then
    # Package upgrade, not removal
    /bin/systemctl try-restart nginx.service &>/dev/null || :
fi


%files
%doc LICENSE CHANGES README
%{_datadir}/nginx/
%{_sbindir}/nginx
%{_mandir}/man8/nginx.8.gz
%{_unitdir}/nginx.service
%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%dir %{_localstatedir}/log/nginx
%config(noreplace) %{_sysconfdir}/nginx/nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/mime.types
%config(noreplace) %{_sysconfdir}/nginx/gzip.types
%config(noreplace) %{_sysconfdir}/nginx/conf.d/default.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%attr(-,nginx,nginx) %dir %{_sharedstatedir}/nginx


%changelog

* Mon Dec 26 2011 Craig Barnes <cr@igbarn.es> - 1.1.12-1
- Update to latest development release
- Add configure flag for PCRE JIT support
- Clean up pointless overuse of macros
- Move "http-client-body-temp-path" location
- Remove pointless extras from pre-install useradd command

* Fri Dec 9 2011 Craig Barnes <cr@igbarn.es> - 1.0.10-1
- Update to latest stable release
- Pedantic column alignment for package metadata

* Fri Nov 4 2011 Craig Barnes <cr@igbarn.es> - 1.0.9-1
- Add custom configuration files
- Fix incorrect macro usage
- Update to latest stable release

* Fri Oct 21 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-4
- Remove pointless *.default configuration files
- Add standard systemd scriptlet snippets

* Fri Oct 21 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-3
- Remove all core modules that aren't necessary for serving static files
- Remove all configuration files relating to removed modules
- Remove optional GeoIP module and it's dependencies
- Remove optional stub status module
- Clean up files section to reflect changes

* Wed Oct 19 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-2
- Add systemd init configuration
- Add logrotate configuration

* Tue Oct 18 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-1
- Install manpage
- Remove pointless "provides webserver" directive
- Remove libxslt, libgd and Perl dependencies
- Remove unnecessary patches and extra sources
- Remove Perl module and all related hacks
- Remove most extra modules and some unnecessary core modules
- Remove configuration files for removed core modules
- Remove old style init config and related dependencies
- Remove unnecessary shadow-utils dependency
- Remove seemingly obsolete character set conversion script
- Remove custom macros
- Clean up files section
- Clean up grammar and formatting
- Truncate old changelog
- Remove unnecessary buildroot variable and clean section
- Update to latest stable release

* Fri Aug 26 2011 Keiran "Affix" Smith <fedora@affix.me> - 1.0.5-1
- Update to latest stable release
