Name:           nginx
Version:        1.0.8
Release:        1%{?dist}
Summary:        Robust, high-performance HTTP and reverse proxy server
License:        BSD
URL:            http://nginx.org/
Source0:        http://nginx.org/download/nginx-%{version}.tar.gz

BuildRequires:      pcre-devel,zlib-devel,openssl-devel,GeoIP-devel
Requires:           pcre,openssl,GeoIP

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
    --http-proxy-temp-path=%{_localstatedir}/lib/%{name}/tmp/proxy \
    --http-fastcgi-temp-path=%{_localstatedir}/lib/%{name}/tmp/fastcgi \
    --http-scgi-temp-path=%{_localstatedir}/lib/%{name}/tmp/scgi \
    --pid-path=%{_localstatedir}/run/%{name}.pid \
    --lock-path=%{_localstatedir}/lock/subsys/%{name} \
    --with-http_ssl_module \
    --with-http_gzip_static_module \
    --with-http_stub_status_module \
    --with-http_geoip_module \
    --with-file-aio \
    --with-ipv6 \
    --with-cc-opt="%{optflags} $(pcre-config --cflags)" \
    --without-http_auth_basic_module \
    --without-http_charset_module \
    --without-http_map_module \
    --without-http_memcached_module \
    --without-http_split_clients_module \
    --without-http_ssi_module \
    --without-http_userid_module \
    --without-http_uwsgi_module
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
chmod 0755 %{buildroot}%{_sbindir}/nginx
rm %{buildroot}/%{_sysconfdir}/%{name}/{win-utf,koi-utf,koi-win}
rm %{buildroot}/%{_sysconfdir}/%{name}/{uwsgi_params,uwsgi_params.default}
gzip -9 objs/%{name}.8
%{__install} -p -d -m 0755 %{buildroot}%{_mandir}/man8
%{__install} -p -m 0644 objs/%{name}.8.gz %{buildroot}%{_mandir}/man8
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
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/conf.d
%dir %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf.default
%config(noreplace) %{_sysconfdir}/%{name}/mime.types
%config(noreplace) %{_sysconfdir}/%{name}/mime.types.default
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi.conf
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi.conf.default
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi_params
%config(noreplace) %{_sysconfdir}/%{name}/fastcgi_params.default
%config(noreplace) %{_sysconfdir}/%{name}/scgi_params
%config(noreplace) %{_sysconfdir}/%{name}/scgi_params.default
%attr(-,%{name},%{name}) %dir %{_localstatedir}/lib/%{name}
%attr(-,%{name},%{name}) %dir %{_localstatedir}/lib/%{name}/tmp


%changelog

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
