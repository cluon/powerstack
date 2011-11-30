%define beanstalkd_user      beanstalkd
%define beanstalkd_group     %{beanstalkd_user}
%define beanstalkd_home      %{_localstatedir}/lib/beanstalkd
%define beanstalkd_logdir    %{_localstatedir}/log/beanstalkd
%define beanstalkd_binlogdir %{beanstalkd_home}/binlog

Name:           beanstalkd
Version:        1.4.6
Release:        1
Summary:        A simple, fast work-queue service

Group:          System Environment/Daemons
License:        GPLv3+
URL:            http://xph.us/software/%{name}/
Source0:        http://xph.us/dist/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.init
Source2:        %{name}.sysconfig
Patch0:		beanstalkd-1.4.6-centos-4.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:   libevent-devel

Requires(pre):      %{_sbindir}/useradd
Requires(pre):      %{_sbindir}/groupadd
Requires(post):     chkconfig
Requires(preun):    chkconfig
Requires(preun):    initscripts
Requires(postun):   initscripts


%description
beanstalkd is a simple, fast work-queue service. Its interface is generic,
but was originally designed for reducing the latency of page views in
high-volume web applications by running most time-consuming tasks
asynchronously.


%prep
%setup -q

%if 0%{?rhel} == 4
%patch0 -p0
%endif

if [ ! -e configure ]; then
  sh autogen.sh
fi


%build
%configure --disable-rpath
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install-man1 DESTDIR=$RPM_BUILD_ROOT
make install-exec-am DESTDIR=$RPM_BUILD_ROOT
%{__install} -p -D -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%{__install} -d -m 0755 %{buildroot}%{beanstalkd_home}
%{__install} -d -m 0755 %{buildroot}%{beanstalkd_binlogdir}


%clean
rm -rf $RPM_BUILD_ROOT

%pre
%{_sbindir}/groupadd -f -r %{beanstalkd_group}
%{_sbindir}/useradd -r -m -c "beanstalkd user" -s /bin/false \
    -d %{beanstalkd_home} %{beanstalkd_user} 2>/dev/null || :

%post
/sbin/chkconfig --add %{name}

# make the binlog dir after installation, this is so SELinux does not complain
# about the init script creating the binlog directory
# Bug 558310
if [ -d %{beanstalkd_home} ]; then
    %{__install} -d %{beanstalkd_binlogdir} -m 0755 \
        -o %{beanstalkd_user} -g %{beanstalkd_user} \
        %{beanstalkd_binlogdir}
fi


%preun
if [ $1 = 0 ]; then
    /sbin/service %{name} stop >/dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi

%postun
if [ "$1" -ge "1" ]; then
    /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%doc README README-DEVELOPERS README-TESTS COPYING doc/protocol.txt
%{_initrddir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%ghost %attr(0755,%{beanstalkd_user},%{beanstalkd_group}) %dir %{beanstalkd_home}
%ghost %attr(0755,%{beanstalkd_user},%{beanstalkd_group}) %dir %{beanstalkd_binlogdir}


%changelog
* Thu Nov 24 2011 Santi Saez <santi@woop.es> - 1.4.6-1
- Upgrade to upstream beanstalkd 1.4.6 (EPEL-6 backport)
- beanstalkd-1.4.6-centos-4 patch added to allow build on RHEL-4

* Sat Oct 17 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4.2-1
- update to upstream 1.4.2

* Sun Oct 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.4-0
- update to upstream 1.4

* Sat Apr 11 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.3-1
- update to upstream 1.3

* Tue Feb 17 2009 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.2-1
- update to upstream 1.2
- remove man page source as it was incorporated upstream

* Sat Nov 22 2008 Jeremy Hinegardner <jeremy at hinegardner dot org> - 1.1-1
- initial spec creation
