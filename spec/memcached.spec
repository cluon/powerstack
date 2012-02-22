%define username   memcached
%define groupname  memcached

Name:           memcached
Version:        1.4.13
Release:        1
Epoch:		0
Summary:        High Performance, Distributed Memory Object Cache

Group:          System Environment/Daemons
License:        BSD
URL:            http://www.memcached.org/
Source0:        http://memcached.googlecode.com/files/%{name}-%{version}.tar.gz

# custom init script
Source1:        memcached.sysv

# Fixes
#Patch0:		memcached-1.4.11-gcc-atomictest.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libevent-devel
BuildRequires:  perl(Test::More)

Requires: initscripts
Requires: libevent
Requires(pre):  shadow-utils
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service

# as of 3.5.5-4 selinux has memcache included
Obsoletes: memcached-selinux

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package devel
Summary:	Files needed for development using memcached protocol
Group:		Development/Libraries 
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Install memcached-devel if you are developing C/C++ applications that require access to the
memcached binary include files.

%prep
%setup -q
#%patch0 -p1 -b .gcc-atomictest

%build

# memcached 1.4.13 build fails on RHEL-5 + i386, ofender is march gcc flag => s/i386/i686
%ifarch %ix86
   %if 0%{?rhel} >= 4
      CFLAGS='-O2 -g -march=i686 -mtune=i686'
      export CFLAGS
   %endif
%endif

%configure

make %{?_smp_mflags}

%check
# remove failing test that doesn't work in build systems

# PowerStack: %check phase disabled again on 2012-02-22
#rm -f t/daemonize.t 
#rm -f t/binary.t
#make test

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"                                         
# remove memcached-debug
rm -f %{buildroot}/%{_bindir}/memcached-debug

# Perl script for monitoring memcached
install -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool

# Init script
install -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/memcached

# Default configs
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
cat <<EOF >%{buildroot}/%{_sysconfdir}/sysconfig/%{name}
PORT="11211"
USER="%{username}"
MAXCONN="1024"
CACHESIZE="64"
OPTIONS=""
EOF

# pid directory
mkdir -p %{buildroot}/%{_localstatedir}/run/memcached

%clean
rm -rf %{buildroot}


%pre
getent group %{groupname} >/dev/null || groupadd -r %{groupname}
getent passwd %{username} >/dev/null || \
useradd -r -g %{groupname} -d %{_localstatedir}/run/memcached \
    -s /sbin/nologin -c "Memcached daemon" %{username}
exit 0


%post
/sbin/chkconfig --add %{name}


%preun
if [ "$1" = 0 ] ; then
    /sbin/service %{name} stop > /dev/null 2>&1
    /sbin/chkconfig --del %{name}
fi
exit 0


%postun
# DISABLED by PowerStack! **never** restart memcached service on RPM upgrade!!
#if [ "$1" -ge 1 ]; then
#    /sbin/service %{name} condrestart > /dev/null 2>&1
#fi
exit 0


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README doc/CONTRIBUTORS doc/*.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%dir %attr(755,%{username},%{groupname}) %{_localstatedir}/run/memcached
%{_bindir}/memcached-tool
%{_bindir}/memcached
%{_mandir}/man1/memcached.1*
%{_initrddir}/memcached


%files devel
%defattr(-,root,root,0755)
%{_includedir}/memcached/*

%changelog
* Tue Feb 21 2012 Santi Saez <santi@woop.es> - 1.4.13-1
- Upgrade to upstream memcached 1.4.13 (http://goo.gl/RkXLQ)
- Fix small number of bugs building on different platforms and old GCC versions
- memcached-1.4.11-gcc-atomictest removed, .12 adds properly detect GCC atomics
- make test enabled again
- RPM build fails on RHEL-5 + i386, ofender is-march gcc flag, fixed with a %if

* Tue Jan 17 2012 Santi Saez <santi@woop.es> - 1.4.11-1
- Upgrade to upstream memcached 1.4.11
- Fix race conditions and crashes introduced in previos version (goo.gl/0IQbe)
- Adds the ability to rebalance and reassign SLAB memory
- memcached-1.4.11-gcc-atomictest patch added for RHEL-{4,5} (goo.gl/bFdPI)

* Wed Nov 23 2011 Santi Saez <santi@woop.es> - 1.4.10-1
- Upgrade to upstream memcached 1.4.10
- %check phase disabled because of testapp:start_server() assertion random crash

* Thu Nov  3 2011 Santi Saez <santi@woop.es> - 1.4.9-1
- Upgrade to upstream memcached 1.4.9
- Disable memcached service restart on RPM upgrade

* Tue May 24 2011 Santi Saez <santi@woop.es> - 1.4.5-1
- Backport from EPEL-5

* Sun Apr  4 2010 Paul Lindner <lindner@inuus.com> - 0:1.4.5-1
- Upgrade to upstream memcached-1.4.5 (http://code.google.com/p/memcached/wiki/ReleaseNotes145)

* Wed Jan 20 2010 Paul Lindner <lindner@inuus.com> - 0:1.4.4-2
- Remove SELinux policies fixes Bugzilla 557073

* Sat Nov 28 2009 Paul Lindner <lindner@inuus.com> - 0:1.4.4-1
- Upgraded to upstream memcached-1.4.4 (http://code.google.com/p/memcached/wiki/ReleaseNotes144)
- Add explicit Epoch to fix issue with broken devel dependencies (resolves 542001)

* Thu Nov 12 2009 Paul Lindner <lindner@inuus.com> - 1.4.3-1
- Add explicit require on memcached for memcached-devel (resolves 537046)
- enable-threads option no longer needed
- Update web site address

* Wed Nov 11 2009 Paul Lindner <lindner@inuus.com> - 1.4.3-1
- Upgrade to memcached-1.4.3

* Mon Oct 12 2009 Paul Lindner <lindner@inuus.com> - 1.4.2-1
- Upgrade to memcached-1.4.2
- Addresses CVE-2009-2415

* Sat Aug 29 2009 Paul Lindner <lindner@inuus.com> - 1.4.1-1
- Upgrade to 1.4.1 
- http://code.google.com/p/memcached/wiki/ReleaseNotes141

* Wed Apr 29 2009 Paul Lindner <lindner@inuus.com> - 1.2.8-1
- Upgrade to memcached-1.2.8
- Addresses CVE-2009-1255

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Paul Lindner <lindner@inuus.com> - 1.2.6-1
- Upgrade to memcached-1.2.6

* Tue Mar  4 2008 Paul Lindner <lindner@inuus.com> - 1.2.5-1
- Upgrade to memcached-1.2.5

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-4
- Autorebuild for GCC 4.3

* Sun Jan 27 2008 Paul Lindner <lindner@inuus.com> - 1.2.4-3
- Adjust libevent dependencies

* Sat Dec 22 2007 Paul Lindner <lindner@inuus.com> - 1.2.4-2
- Upgrade to memcached-1.2.4

* Fri Sep 07 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.2.3-8
- Add selinux policies
- Create our own system user

* Mon Aug  6 2007 Paul Lindner <lindner@inuus.com> - 1.2.3-7
- Fix problem with -P and -d flag combo on x86_64
- Fix init script for FC-6

* Fri Jul 13 2007 Paul Lindner <lindner@inuus.com> - 1.2.3-4
- Remove test that fails in fedora build system on ppc64

* Sat Jul  7 2007 root <lindner@inuus.com> - 1.2.3-2
- Upgrade to 1.2.3 upstream
- Adjust make install to preserve man page timestamp
- Conform with LSB init scripts standards, add force-reload

* Wed Jul  4 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-5
- Use /var/run/memcached/ directory to hold PID file

* Sat May 12 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-4
- Remove tabs from spec file, rpmlint reports no more errors

* Thu May 10 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-3
- Enable build-time regression tests
- add dependency on initscripts
- remove memcached-debug (not needed in dist)
- above suggestions from Bernard Johnson

* Mon May  7 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-2
- Tidyness improvements suggested by Ruben Kerkhof in bugzilla #238994

* Fri May  4 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-1
- Initial spec file created via rpmdev-newspec
