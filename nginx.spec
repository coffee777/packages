%define nginx_user      nginx
%define nginx_group     %{nginx_user}
%define nginx_home      %{_localstatedir}/lib/nginx
%define nginx_home_tmp  %{nginx_home}/tmp
%define nginx_logdir    %{_localstatedir}/log/nginx
%define nginx_confdir   %{_sysconfdir}/nginx
%define nginx_datadir   %{_datadir}/nginx
%define nginx_webroot   %{nginx_datadir}/html

Name:           nginx
Version:        1.0.8
Release:        1%{?dist}
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
Nginx [engine x] is an HTTP(S) server, HTTP(S) reverse proxy and IMAP/POP3
proxy server written by Igor Sysoev.


%prep
%setup -q


%build
export DESTDIR=%{buildroot}
./configure \
    --user=%{nginx_user} \
    --group=%{nginx_group} \
    --prefix=%{nginx_datadir} \
    --sbin-path=%{_sbindir}/%{name} \
    --conf-path=%{nginx_confdir}/%{name}.conf \
    --error-log-path=%{nginx_logdir}/error.log \
    --http-log-path=%{nginx_logdir}/access.log \
    --http-client-body-temp-path=%{nginx_home_tmp}/client_body \
    --http-proxy-temp-path=%{nginx_home_tmp}/proxy \
    --http-fastcgi-temp-path=%{nginx_home_tmp}/fastcgi \
    --http-uwsgi-temp-path=%{nginx_home_tmp}/uwsgi \
    --http-scgi-temp-path=%{nginx_home_tmp}/scgi \
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
rm %{buildroot}/%{nginx_confdir}/{win-utf,koi-utf,koi-win}
rm %{buildroot}/%{nginx_confdir}/{uwsgi_params,uwsgi_params.default}
chmod 0755 %{buildroot}%{_sbindir}/nginx
%{__install} -p -d -m 0755 %{buildroot}%{nginx_confdir}/conf.d
%{__install} -p -d -m 0755 %{buildroot}%{nginx_home_tmp}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_logdir}
%{__install} -p -d -m 0755 %{buildroot}%{nginx_webroot}

# convert to UTF-8 all files that give warnings.
for textfile in CHANGES; do
    mv $textfile $textfile.old
    iconv --from-code ISO8859-1 --to-code UTF-8 --output $textfile $textfile.old
    rm -f $textfile.old
done


%pre
if [ $1 == 1 ]; then
    %{_sbindir}/useradd -c "Nginx user" -s /bin/false -r -d %{nginx_home} %{nginx_user} 2>/dev/null || :
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
%{nginx_datadir}/
%{_sbindir}/%{name}
%dir %{nginx_confdir}
%dir %{nginx_confdir}/conf.d
%dir %{nginx_logdir}
%config(noreplace) %{nginx_confdir}/%{name}.conf
%config(noreplace) %{nginx_confdir}/%{name}.conf.default
%config(noreplace) %{nginx_confdir}/mime.types
%config(noreplace) %{nginx_confdir}/mime.types.default
%config(noreplace) %{nginx_confdir}/fastcgi.conf
%config(noreplace) %{nginx_confdir}/fastcgi.conf.default
%config(noreplace) %{nginx_confdir}/fastcgi_params
%config(noreplace) %{nginx_confdir}/fastcgi_params.default
%config(noreplace) %{nginx_confdir}/scgi_params
%config(noreplace) %{nginx_confdir}/scgi_params.default
%attr(-,%{nginx_user},%{nginx_group}) %dir %{nginx_home}
%attr(-,%{nginx_user},%{nginx_group}) %dir %{nginx_home_tmp}


%changelog

* Fri Aug 26 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-2
- Remove pointless "provides webserver" directive
- Remove libxslt and libgd dependencies
- Remove all remaining patches and extra sources
- Remove most of the extra modules
- Remove unnecessary core modules
- Remove configuration files for removed core modules
- Clean up files section
- Remove remaining Perl cruft

* Fri Aug 26 2011 Craig Barnes <cr@igbarn.es> - 1.0.8-1
- Truncate old changelog
- Remove pointless distro patches
- Remove Perl from modules and dependencies
- Fix comments and formatting
- Remove unnecessary buildroot variable and clean section
- Update to latest stable release

* Fri Aug 26 2011 Keiran "Affix" Smith <fedora@affix.me> - 1.0.5-1
- Update to latest stable release
