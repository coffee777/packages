Name:               nginx
Epoch:              5
Version:            1.2.8
Release:            1%{?dist}
Summary:            High performance HTTP and reverse proxy server
License:            BSD
URL:                http://nginx.org/

Source0:            http://nginx.org/download/nginx-%{version}.tar.gz
Source1:            nginx.service
Source2:            nginx.logrotate
Source3:            nginx.conf
Source4:            mime.types
Source5:            gzip.conf
Source6:            default.conf
Source7:            https://github.com/simpl/ngx_devel_kit/archive/v0.2.18.tar.gz
Source8:            https://github.com/chaoslawful/lua-nginx-module/archive/v0.7.15.tar.gz
Source9:            https://github.com/FRiCKLE/ngx_postgres/archive/1.0rc2.tar.gz
Source10:           https://github.com/agentzh/rds-json-nginx-module/archive/v0.12rc10.tar.gz
Source11:           https://github.com/agentzh/echo-nginx-module/archive/v0.42.tar.gz

BuildRequires:      pcre-devel >= 8.20
BuildRequires:      zlib-devel
BuildRequires:      openssl-devel
BuildRequires:      libluajit-devel
BuildRequires:      GeoIP-devel
BuildRequires:      postgresql-devel

Requires:           logrotate
Requires(pre):      shadow-utils
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
Nginx [engine x] is a HTTP(S) server, HTTP(S) reverse proxy and IMAP/POP3
proxy server written by Igor Sysoev.


%prep
%setup -q -a7 -a8 -a9 -a10 -a11
sed -i 's/-Werror//g' auto/cc/gcc


%build
export LUAJIT_LIB=%{_libdir}
export LUAJIT_INC=%{_includedir}/luajit-2.0
./configure \
    --user=nginx \
    --group=nginx \
    --with-file-aio \
    --with-ipv6 \
    --with-pcre-jit \
    --prefix=%{_datadir}/nginx \
    --sbin-path=%{_sbindir}/nginx \
    --conf-path=%{_sysconfdir}/nginx/nginx.conf \
    --pid-path=/run/nginx.pid \
    --lock-path=%{_localstatedir}/lock/subsys/nginx \
    --error-log-path=%{_localstatedir}/log/nginx/error.log \
    --http-log-path=%{_localstatedir}/log/nginx/access.log \
    --http-client-body-temp-path=%{_sharedstatedir}/nginx/body \
    --http-proxy-temp-path=%{_sharedstatedir}/nginx/proxy \
    --http-fastcgi-temp-path=%{_sharedstatedir}/nginx/fastcgi \
    --http-scgi-temp-path=%{_sharedstatedir}/nginx/scgi \
    --http-uwsgi-temp-path=%{_sharedstatedir}/nginx/uwsgi \
    --with-cc-opt="%{optflags} $(pcre-config --cflags)" \
    --with-http_ssl_module \
    --with-http_gzip_static_module \
    --with-http_geoip_module \
    --without-http_charset_module \
    --add-module=ngx_devel_kit-0.2.18 \
    --add-module=lua-nginx-module-0.7.15 \
    --add-module=ngx_postgres-1.0rc2 \
    --add-module=rds-json-nginx-module-0.12rc10 \
    --add-module=echo-nginx-module-0.42
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
chmod 0755 %{buildroot}%{_sbindir}/nginx
rm %{buildroot}/%{_sysconfdir}/nginx/*.default
rm %{buildroot}/%{_sysconfdir}/nginx/{win-utf,koi-utf,koi-win}
install -Dpm0644 objs/nginx.8 %{buildroot}%{_mandir}/man8/nginx.8
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/nginx.service
install -Dpm0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/nginx
install -Dpm0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/nginx/nginx.conf
install -Dpm0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/nginx/mime.types
install -Dpm0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/nginx/gzip.conf
install -Dpm0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/nginx/conf.d/default.conf
install -dpm0755 %{buildroot}%{_sharedstatedir}/nginx
install -dpm0755 %{buildroot}%{_localstatedir}/log/nginx
install -dpm0755 %{buildroot}%{_datadir}/nginx/html


%pre
if [ $1 -eq 1 ]; then
    getent group nginx >/dev/null || groupadd -r nginx
    getent passwd nginx >/dev/null || useradd -r -d %{_sharedstatedir}/nginx \
        -g nginx -s /sbin/nologin -c "Nginx web server" nginx >/dev/null
    exit 0
fi

%post
%systemd_post nginx.service

%preun
%systemd_preun nginx.service

%postun
%systemd_postun_with_restart nginx.service


%files
%doc LICENSE CHANGES README
%{_datadir}/nginx/
%{_sbindir}/nginx
%{_mandir}/man8/nginx.8*
%{_unitdir}/nginx.service
%dir %{_sysconfdir}/nginx
%dir %{_sysconfdir}/nginx/conf.d
%dir %{_localstatedir}/log/nginx
%config(noreplace) %{_sysconfdir}/nginx/nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/fastcgi.conf
%config(noreplace) %{_sysconfdir}/nginx/*_params
%config(noreplace) %{_sysconfdir}/nginx/mime.types
%config(noreplace) %{_sysconfdir}/nginx/gzip.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/default.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/nginx
%attr(-,nginx,nginx) %dir %{_sharedstatedir}/nginx


%changelog

* Thu Apr 04 2013 Craig Barnes <cr@igbarn.es> - 5:1.2.8-1
- Update to latest stable release
- Update modules

* Sun Mar 17 2013 Craig Barnes <cr@igbarn.es> - 5:1.2.7-2
- Use systemd macro scriptlets

* Sat Mar 09 2013 Craig Barnes <cr@igbarn.es> - 5:1.2.7-1
- Update to latest stable release
- Fix overly specific libluajit version dependency

* Sat Jan 05 2013 Craig Barnes <cr@igbarn.es> - 5:1.2.6-1
- Update to latest stable release
- Update Lua module to v0.7.13

* Sat Jan 05 2013 Craig Barnes <cr@igbarn.es> - 5:1.2.5-2
- Clean up commands in install section

* Thu Nov 15 2012 Craig Barnes <cr@igbarn.es> - 5:1.2.5-1
- Update Nginx to latest stable release
- Update Lua module to 0.6.10
- Update PostgreSQL module to 1.0rc2
- Update RDS JSON module to 0.12rc10
- Update echo module to 0.41
- Update sources to use new GitHub archive links
- Use new "auto" value for "worker_processes" in nginx.conf
- Add shadow-utils as "Requires(pre)"
- Make pre scriptlet more robust

* Fri Jun 22 2012 Craig Barnes <cr@igbarn.es> - 5:1.2.1-1
- Use Epoch 5 to take precedence over Nginx builds in the Fedora repository
- Update Lua module to v0.5.2

* Fri Jun 22 2012 Craig Barnes <cr@igbarn.es> - 1.2.1-1
- Update to latest stable release
- Remove -Werror flag (turns warnings from "FORTIFY_SOURCE=2" into errors)
- Enable "pcre_jit" option in nginx.conf (requires pcre version 8.20 or above)

* Thu Apr 26 2012 Craig Barnes <cr@igbarn.es> - 1.2.0-1
- Update to latest stable release
- Update Lua module

* Thu Mar 01 2012 Craig Barnes <cr@igbarn.es> - 1.1.16-1
- Remove all "--without-*" flags except for "--without-http_charset_module"
- Update build, install and files sections to reflect full build
- Update to latest development release

* Mon Feb 20 2012 Craig Barnes <cr@igbarn.es> - 1.1.15-2
- Add postgres, rds-json and echo modules

* Fri Feb 17 2012 Craig Barnes <cr@igbarn.es> - 1.1.15-1
- Move all gzip directives from nginx.conf and gzip.types to gzip.conf
- Move "default_type" from nginx.conf to mime.types
- Remove "pid" from nginx.conf (the configure script sets the correct default)
- Remove "log_format" from nginx.conf (it was the same as the default anyway)
- Clean up and add comments to nginx.conf
- Remove "--without-http_upstream_ip_hash_module" from configure flags
- Update to latest development release

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.1.14-2
- Include some previously excluded core modules (FastCGI, autoindex etc.)

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.1.14-1
- Update to latest development release
- Update Lua module to v0.4.0
- Include FastCGI module again

* Sun Jan 29 2012 Craig Barnes <cr@igbarn.es> - 1.1.13-2
- Change /run references back to /var/run
- Re-order configure flags so that all module related flags are at the bottom
- Add remote-fs and nss-lookup to the "After" directive in nginx.service
  (taken from Fedora's latest httpd.spec)

* Sun Jan 22 2012 Craig Barnes <cr@igbarn.es> - 1.1.13-1
- Update to latest development release
- Add "Restart=on-abort" directive to systemd unit file
- Merge 3 hacky setup macros into 1

* Thu Jan 12 2012 Craig Barnes <cr@igbarn.es> - 1.1.12-3
- Add GeoIP module
- Set geoip_country to correct GeoIP database location in nginx.conf
- Fix RPM explicit-lib-dependency error by specifying libluajit arch/version

* Fri Jan 06 2012 Craig Barnes <cr@igbarn.es> - 1.1.12-2
- Add Lua module (using libluajit)

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
