Name:           nginx
Version:        1.0.8
Release:        3%{?dist}
Summary:        High performance HTTP and reverse proxy server
License:        BSD
URL:            http://nginx.org/

Source0:        http://nginx.org/download/nginx-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.logrotate

BuildRequires:  pcre-devel,zlib-devel,openssl-devel
Requires:       pcre,openssl,logrotate

%description
Nginx [engine x] is a HTTP(S) server, HTTP(S) reverse proxy and IMAP/POP3
proxy server written by Igor Sysoev.


%prep
%setup -q


%build
./configure \
    --user=%{name} \
    --group=%{name} \
    --prefix=%{_datadir}/%{name} \
    --sbin-path=%{_sbindir}/%{name} \
    --conf-path=%{_sysconfdir}/%{name}/%{name}.conf \
    --error-log-path=%{_localstatedir}/log/%{name}/error.log \
    --http-log-path=%{_localstatedir}/log/%{name}/access.log \
    --http-client-body-temp-path=%{_localstatedir}/lib/%{name}/tmp/client_body \
    --pid-path=/run/%{name}.pid \
    --lock-path=%{_localstatedir}/lock/subsys/%{name} \
    --with-http_ssl_module \
    --with-http_gzip_static_module \
    --with-file-aio \
    --with-ipv6 \
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
rm %{buildroot}/%{_sysconfdir}/%{name}/fastcgi.conf
rm %{buildroot}/%{_sysconfdir}/%{name}/*.default
rm %{buildroot}/%{_sysconfdir}/%{name}/{fastcgi,scgi,uwsgi}_params
rm %{buildroot}/%{_sysconfdir}/%{name}/{win-utf,koi-utf,koi-win}
gzip -9 objs/%{name}.8
%{__install} -p -D -m 0644 objs/%{name}.8.gz %{buildroot}%{_mandir}/man8/%{name}.8.gz
%{__install} -p -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -p -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/conf.d
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -p -d -m 0755 %{buildroot}%{_datadir}/%{name}/html


%pre
if [ $1 == 1 ]; then
    %{_sbindir}/useradd -c "Nginx user" -s /bin/false -r -d %{_localstatedir}/lib/%{name} %{name} 2>/dev/null || :
fi


%files
%defattr(-,root,root,-)
%doc LICENSE CHANGES README
%{_datadir}/%{name}/
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.gz
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%dir %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/mime.types
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(-,%{name},%{name}) %dir %{_localstatedir}/lib/%{name}
%attr(-,%{name},%{name}) %dir %{_localstatedir}/lib/%{name}/tmp


%changelog

* Fri Oct 21 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-4
- Remove pointless *.default configuration files

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
