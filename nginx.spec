Name:           nginx
Version:        1.0.8
Release:        2%{?dist}
Summary:        Robust, high-performance HTTP and reverse proxy server
License:        BSD
URL:            http://nginx.org/
Source0:        http://nginx.org/download/nginx-%{version}.tar.gz

BuildRequires:      pcre-devel,zlib-devel,openssl-devel,GeoIP-devel
Requires:           pcre,openssl,GeoIP

# for /usr/sbin/useradd
Requires(pre):      shadow-utils
Requires(post):     chkconfig

# for /sbin/service
Requires(preun):    chkconfig, initscripts
Requires(postun):   initscripts

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
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -empty -exec rm -f {} \;
find %{buildroot} -type f -exec chmod 0644 {} \;
find %{buildroot} -type f -name '*.so' -exec chmod 0755 {} \;
rm %{buildroot}/%{_sysconfdir}/%{name}/{win-utf,koi-utf,koi-win}
rm %{buildroot}/%{_sysconfdir}/%{name}/{uwsgi_params,uwsgi_params.default}
chmod 0755 %{buildroot}%{_sbindir}/nginx
gzip -9 objs/%{name}.8
%{__install} -p -d -m 0755 %{buildroot}%{_mandir}/man8
%{__install} -p -m 0644 objs/%{name}.8.gz %{buildroot}%{_mandir}/man8
%{__install} -p -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/conf.d
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}/tmp
%{__install} -p -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}
%{__install} -p -d -m 0755 %{buildroot}%{_datadir}/%{name}/html

# convert to UTF-8 all files that give warnings.
for textfile in CHANGES; do
    mv $textfile $textfile.old
    iconv --from-code ISO8859-1 --to-code UTF-8 --output $textfile $textfile.old
    rm -f $textfile.old
done


%pre
if [ $1 == 1 ]; then
    %{_sbindir}/useradd -c "Nginx user" -s /bin/false -r -d %{_localstatedir}/lib/%{name} %{name} 2>/dev/null || :
fi

%post
if [ $1 == 1 ]; then
    /sbin/chkconfig --add %{name}
fi

%preun
if [ $1 = 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 == 2 ]; then
    /sbin/service %{name} upgrade || :
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

* Fri Aug 26 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-2
- Remove pointless "provides webserver" directive
- Remove libxslt and libgd dependencies
- Remove all remaining patches and extra sources
- Remove most of the extra modules
- Remove unnecessary core modules
- Remove configuration files for removed core modules
- Replace and remove custom macros
- Clean up files section
- Remove remaining Perl cruft
- Clean up grammar and formatting

* Fri Aug 26 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-1
- Truncate old changelog
- Remove pointless distro patches
- Remove Perl from modules and dependencies
- Fix comments and formatting
- Remove unnecessary buildroot variable and clean section
- Update to latest stable release

* Fri Aug 26 2011 Keiran "Affix" Smith <fedora@affix.me> - 1.0.5-1
- Update to latest stable release
