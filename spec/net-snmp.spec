%{!?tcp_wrappers:%define tcp_wrappers 1}
%{!?lm_sensors:%define lm_sensors 1}

Summary: A collection of SNMP protocol tools and libraries.
Name: net-snmp
Version: 5.3.4
Release: 1
License: BSDish
Group: System Environment/Daemons
URL: http://www.net-snmp.org
Source0: ftp://net-snmp.sourceforge.net/net-snmp-%{version}.tar.gz
Source1: net-snmp.redhat.conf
Source2: net-snmpd.init
Source3: net-snmptrapd.init
Source4: net-snmpd.logrotate
Source5: ucd5820stat
Patch1: ucd-snmp-4.2.4.pre3-mnttab.patch
Patch2: net-snmp-5.0.6-syslog.patch
Patch3: net-snmp-5.0.6-compat.patch
Patch4: net-snmp-5.0.6-libtool.patch
Patch5: net-snmp-5.0.8-ipv6-sock-close.patch
Patch6: net-snmp-5.0.8-readonly.patch
Patch7: net-snmp-5.1.2-libwrap.patch
Patch9: net-snmp-5.1-xs-label-iid.patch
Patch10: net-snmp-5.1-async-getnext.patch
Patch11: net-snmp-5.1.1-hr_storage-mbuf-v2.patch
Patch12: net-snmp-5.1.1-pie.patch
Patch13: net-snmp-5.1.2-bsdcompat.patch
Patch14: net-snmp-5.1-64bit-replace.patch
Patch15: net-snmp-5.1.1-ipAdEntIfIndex.patch
Patch16: net-snmp-5.1.1-quiet-memshared.patch
Patch17: net-snmp-5.0.9-smux-stack-var.patch
Patch18: net-snmp-5.1.2.rc1-agentx-little64.patch
Patch19: net-snmp-5.1.2-lelf.patch
Patch20: net-snmp-5.0.9-HUP_doublefree.patch
Patch21: net-snmp-5.1.2-int-sizes.patch
Patch23: net-snmp-5.1.2-file_offset.patch
Patch24: net-snmp-5.1.2-64bit_iface.patch
Patch25: net-snmp-5.1.2-hrSW_segfault.patch
Patch26: net-snmp-5.1.2-lmSensors.patch
Patch27: net-snmp-5.1.2-setcache.patch
Patch28: net-snmp-5.1.2-ethtool.patch
Patch29: net-snmp-5.1.2-clear_callback3.patch
Patch30: net-snmp-5.1.2-free_session.patch
Patch31: net-snmp-5.1-mktemp.diff
Patch32: net-snmp-5.1.2-tcp_dos.patch

Patch34: net-snmp-5.1.2-agentx-set-leak.patch
Patch35: net-snmp-5.1.2-64bit-interfaces.patch
Patch36: net-snmp-5.1.2-ip2mac.patch

Patch37: net-snmp-5.1.2-hr_storage.patch
Patch38: net-snmp-5.1.2-libwrap-only-socket.patch
Patch39: net-snmp-5.1.2-agent.patch
Patch40: net-snmp-5.1.2-override_bulk2.patch
Patch41: net-snmp-5.1.2-snmp_vlog_varargs_retraversal.patch
Patch42: net-snmp-5.1.2-counter32.patch
Patch43: net-snmp-5.1.2-snmptrapd-memory-leak.patch
Patch44: net-snmp-5.1.2-agentx_crash.patch
Patch45: net-snmp-5.1.2-hr_proc.patch

Patch46: net-snmp-5.1.2-outstanding_requests.patch
Patch47: net-snmp-5.1.2-log.patch
Patch48: net-snmp-5.1.2-snmptrapd-memory-leak1.patch
Patch49: net-snmp-5.1.2-libwrap3.patch

Patch50: net-snmp-5.1.2-api_leaks.patch
Patch51: net-snmp-5.1.2-order.patch
Patch52: net-snmp-5.1.2-negative.patch
Patch53: net-snmp-5.1.2-trap_acks.patch
Patch54: net-snmp-5.1.2-faster-log.patch
Patch55: net-snmp-5.1.2-man-config.patch
Patch56: net-snmp-5.1.2-man-snmpusm.patch
Patch57: net-snmp-5.1.2-port.patch
Patch58: net-snmp-5.1.2-ssRawCpu.patch
Patch59: net-snmp-5.1.2-sigpipe.patch
Patch60: net-snmp-5.1.2-exec.patch
Patch61: net-snmp-5.1.2-mib-option.patch
Patch62: net-snmp-5.1.2-snmpconf-selinux.patch
Patch63: net-snmp-5.1.2-tcp-scalars.patch
Patch64: net-snmp-5.1.2-maxreps.patch
Patch65: net-snmp-5.1.2-device-holes.patch
Patch66: net-snmp-5.1.2-smux-select.patch
Patch67: net-snmp-5.3.1-tmp-dir.patch
Patch68: net-snmp-5.3.1-disk-spaces.patch
Patch69: net-snmp-5.3.1-cmdline.patch
Patch70: net-snmp-5.3.1-config_libdir.patch
Patch71: net-snmp-5.1.2-authfail.patch
Patch72: net-snmp-5.1.2-man-exec.patch
Patch73: net-snmp-5.1.2-diskio-truncation.patch
Patch74: net-snmp-5.1.2-override.patch
Patch75: net-snmp-5.1.2-man-ignoredisk.patch
Patch76: net-snmp-5.4.1-hmac-check.patch
Patch77: net-snmp-5.1.2-perl-snprintf.patch
Patch78: net-snmp-5.1.2-load-avg-long.patch
Patch79: net-snmp-5.1.2-smux-traps.patch
Patch80: net-snmp-5.1.2-trap-agent-addr.patch
Patch81: net-snmp-5.1.2-dontlog.patch
Patch82: net-snmp-5.1.2-local-addr-v3.patch
Patch83: net-snmp-5.1.2-deprecated-log-option.patch
Patch84: net-snmp-5.1.2-ip-size.patch
Patch85: net-snmp-5.1.2-getbulk-crash.patch
Patch86: net-snmp-5.1.2-cmdline-crash.patch
Patch87: net-snmp-5.1.2-cpu.patch
Patch88: net-snmp-5.1.2-processor-load.patch

Requires: /sbin/chkconfig
Requires: %{name}-libs = %{version}-%{release}
Obsoletes: ucd-snmp
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: openssl-devel, bzip2-devel, beecrypt-devel, elfutils-devel, libselinux-devel
%ifarch %{ix86} x86_64
BuildRequires: lm_sensors-devel
%endif
%if %{tcp_wrappers}
BuildRequires: tcp_wrappers
%endif
BuildRequires: perl, coreutils, grep, sed, findutils, rpm-devel

#%define __libtoolize /bin/true
%{expand: %%define _includedir	%{_includedir}/%{name}}

%description
SNMP (Simple Network Management Protocol) is a protocol used for
network management. The NET-SNMP project includes various SNMP tools:
an extensible agent, an SNMP library, tools for requesting or setting
information from SNMP agents, tools for generating and handling SNMP
traps, a version of the netstat command which uses SNMP, and a Tk/Perl
mib browser. This package contains the snmpd and snmptrapd daemons,
documentation, etc.

You will probably also want to install the net-snmp-utils package,
which contains NET-SNMP utilities.

Building option:
	--without tcp_wrappers : disable tcp_wrappers support

%package utils
Group: Applications/System
Summary: Network management utilities using SNMP, from the NET-SNMP project.
Requires: %{name} = %{version}-%{release}
Obsoletes: ucd-snmp-utils

%description utils
The net-snmp-utils package contains various utilities for use with the
NET-SNMP network management project.

Install this package if you need utilities for managing your network
using the SNMP protocol. You will also need to install the net-snmp
package.

%package devel
Group: Development/Libraries
Summary: The development environment for the NET-SNMP project.
Requires: %{name} = %{version}-%{release}
Obsoletes: ucd-snmp-devel
BuildRequires: elfutils-libelf-devel
Requires: beecrypt-devel, elfutils-devel, rpm-devel

%description devel
The net-snmp-devel package contains the development libraries and
header files for use with the NET-SNMP project's network management
tools.

Install the net-snmp-devel package if you would like to develop
applications for use with the NET-SNMP project's network management
tools. You'll also need to have the net-snmp and net-snmp-utils
packages installed.

%package perl
Group: Development/Libraries
Summary: The perl NET-SNMP module and the mib2c tool.
Requires: %{name} = %{version}-%{release}, perl >= 5
BuildRequires: perl >= 5

%description perl
The net-snmp-perl package contains the perl files to use SNMP from within
Perl.

Install the net-snmp-perl package, if you want to use mib2c or SNMP with perl.

%package libs
Group: Development/Libraries
Summary: The NET-SNMP runtime libraries.

%description libs
The net-snmp-libs package contains the runtime libraries for shared binaries
and applications.

%prep
%setup -q
#%patch1 -p1 -b .mnttab
%patch2 -p1 -b .syslog
#%patch3 -p1 -b .compat
%patch4 -p1 -b .libtool
%patch5 -p1 -b .ipv6-sock-close
%patch6 -p1 -b .readonly
#%patch7 -p1 -b .libwrap
#%patch9 -p1 -b .xs-label-iid
#%patch10 -p1 -b .async-getnext
#%patch11 -p1 -b .hr_storage-mbuf-v2

%ifnarch ia64
#%patch12 -p1 -b .pie
%endif

#%patch13 -p1 -b .bsdcompat
#%patch14 -p1 -b .64bit
#%patch15 -p1 -b .ipAdEntIfIndex
#%patch16 -p1 -b .quiet-memshared
#%patch17 -p1 -b .stack
#%patch18 -p1 -b .agentx-little64
#%patch19 -p1 -b .lelf
#%patch20 -p1 -b .hup
#%patch21 -p0 -b .int-sizes
%patch23 -p1 -b .file_offset
#%patch24 -p1 -b .64bit_iface
%patch25 -p1 -b .hrSwSegfault
#%patch26 -p1 -b .moresensors
%patch27 -p1 -b .setcache
#%patch28 -p1 -b .ethtool
#%patch29 -p1 -b .callback3
#%patch30 -p1 -b .doublefree
#%patch31 -b .mktemp
#%patch32 -p1 -b .tcp_dos
#%patch34 -p1 -b .set_leak
#%patch35 -p1 -b .64bit_iface
#%patch36 -p1 -b .ip2mac
#%patch37 -p1 
#%patch38 -p1 -b .libwrap

#%patch39 -p1 -b .agent_old
#%patch40 -p1 -b .bulk_patch
#%patch41 -p1 -b .long_args
#%patch42 -p1 -b .counter32
#%patch43 -p1 -b .mem_leak
#%patch44 -p1 -b .agentx_crash
%patch45 -p1 -b .hr_proc

#%patch46 -p1 -b .agent_req
#%patch47 -p1 -b .log
#%patch48 -p1 -b .mem-leak1
#%patch49 -p1 -b .libwrap3

#%patch50 -p1 -b .api_leaks
#%patch51 -p1 -b .order
#%patch52 -p1 -b .negative
#%patch53 -p1 -b .trap_ack
#%patch54 -p1 -b .faster-log
%patch55 -p1 -b .man-config
%patch56 -p1 -b .man-snmpusm
%patch57 -p1 -b .port
#%patch58 -p0 -b .ssRawCpu
#%patch59 -p1 -b .sigpipe
#%patch60 -p0 -b .exec
#%patch61 -p1 -b .mib-option
%patch62 -p1 -b .selinux
#%patch63 -p0 -b .tcp-scalars
#%patch64 -p1 -b .maxreps
#%patch65 -p0 -b .device-holes
#%patch66 -p1 -b .smux-select
%patch67 -p1 -b .tmp-dir
#%patch68 -p1 -b .disk-spaces
#%patch69 -p0 -b .cmdline
%patch70 -p1 -b .config-libdir
#%patch71 -p0 -b .authfail
#%patch72 -p1 -b .man-exec
#%patch73 -p0 -b .diskio-truncation
#%patch74 -p0 -b .override
#%patch75 -p1 -b .man-ignoredisk
%patch76 -p1 -b .hmac-check
#%patch77 -p1 -b .perl-snprinf
%patch78 -p1 -b .load-avg-long
#%patch79 -p2 -b .smux-traps
#%patch80 -p1 -b .trap-agent-addr
#%patch81 -p1 -b .dontlog
#%patch82 -p1 -b .local-addr
#%patch83 -p1 -b .deprecated-log-option
#%patch84 -p1 -b .ip-size
#%patch85 -p1 -b .getbulk-crash
#%patch86 -p1 -b .cmdline-crash
#%patch87 -p1 -b .cpu
#%patch88 -p1 -b .processor-load

# Do this patch with a perl hack...
perl -pi -e "s|'\\\$install_libdir'|'%{_libdir}'|" ltmain.sh

%build
export CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -lcrypto -L%{_libdir}"
%ifarch ia64 x86_64 s390x ppc64
export LDFLAGS="-L%{_libdir}"
%endif

MIBS="host agentx smux ucd-snmp/diskio disman/event-mib"
%if %{lm_sensors}
%ifarch %{ix86} x86_64
MIBS="$MIBS ucd-snmp/lmSensors"
%endif
%endif

%configure \
	--enable-static --enable-shared			\
	--with-cflags="$CFLAGS"         		\
	--with-sys-location="Unknown"			\
	--with-logfile="/var/log/snmpd.log"		\
	--with-persistent-directory="/var/net-snmp"	\
	--with-mib-modules="$MIBS"	\
%if %{tcp_wrappers}
	--with-libwrap=%{_libdir}			\
%endif
	--sysconfdir=%{_sysconfdir}			\
	--enable-ipv6					\
	--enable-ucd-snmp-compatibility			\
	--enable-mfd-rewrites				\
	--with-pic					\
	--with-sys-contact="root@localhost" <<EOF


EOF

make

pushd perl
# Use just built libs for perl module building, not the system libs.
perl Makefile.PL -NET-SNMP-IN-SOURCE=true PREFIX=${RPM_BUILD_ROOT}/%{_prefix} INSTALLDIRS=vendor
perl -pi -e 's/^LD_RUN_PATH.*//;s/LD_RUN_PATH=\".*\" //;' default_store/Makefile OID/Makefile agent/Makefile agent/default_store/Makefile ASN/Makefile SNMP/Makefile
#perl Makefile.PL PREFIX=${RPM_BUILD_ROOT}/%{_prefix} INSTALLDIRS=vendor -NET-SNMP-CONFIG="sh ../../net-snmp-config" -NET-SNMP-IN-SOURCE=true
make
popd

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall  ucdincludedir=${RPM_BUILD_ROOT}/usr/include/ucd-snmp

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp
install -m 644 %SOURCE1 ${RPM_BUILD_ROOT}%{_sysconfdir}/snmp/snmpd.conf

install -d ${RPM_BUILD_ROOT}%{_initrddir}
install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}%{_initrddir}/snmpd
install -m 755 %SOURCE3 ${RPM_BUILD_ROOT}%{_initrddir}/snmptrapd

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/snmpd

install -d ${RPM_BUILD_ROOT}%{_bindir}
install -m 755 %SOURCE5 ${RPM_BUILD_ROOT}%{_bindir}/ucd5820stat

rm -f ${RPM_BUILD_ROOT}%{_bindir}/snmpinform
rm -f ${RPM_BUILD_ROOT}%{_bindir}/tkmib
rm -f ${RPM_BUILD_ROOT}%{_bindir}/snmpcheck
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man1/snmpconf.1*
ln -s snmptrap ${RPM_BUILD_ROOT}/usr/bin/snmpinform

# copy missing mib2c.conf files
cp local/mib2c.*.conf ${RPM_BUILD_ROOT}%{_datadir}/snmp

pushd perl
make install_vendor
eval $(perl '-V:installvendorarch')

# Urgs, what an evil hack. Brrr.
#%if "%{_libdir}" == "/usr/lib64"
#installvendorarch=`echo $installvendorarch | sed 's/lib/lib64/'`
#%endif

# remove special files
find $RPM_BUILD_ROOT -name perllocal.pod \
	-o -name .packlist \
	-o -name "*.bs" \
	-o -name Makefile.subs.pl \
	| xargs -ri rm -f {}

# no empty directories
find $RPM_BUILD_ROOT/$installvendorarch \
	-depth -type d -a -empty -exec rmdir {} \;

# build files list
find $RPM_BUILD_ROOT/$installvendorarch -type f -print \
	-o -type d -a -printf '%%%%dir %%p\n' \
	| sed "s@$RPM_BUILD_ROOT@@g" \
	| grep -v "$installvendorarch\$" \
	| grep -v '/auto$' \
	> ../perl.lst
popd
find $RPM_BUILD_ROOT -name '*.so' | xargs chmod 0755

# remove docs that do not apply to Linux
for file in "README.aix README.hpux11 README.osX README.Panasonic_AM3X.txt README.solaris README.win32"
do
	rm $file
done
# trim down massive ChangeLog
dd bs=1024 count=250 if=ChangeLog of=ChangeLog.trimmed

# pre-create /var/run/snmpd for temporary files
install -d ${RPM_BUILD_ROOT}/var/run/snmpd

%post
/sbin/chkconfig --add snmpd 
/sbin/chkconfig --add snmptrapd

%preun
if [ $1 = 0 ]; then
   service snmpd stop >/dev/null 2>&1
   /sbin/chkconfig --del snmpd
   service snmptrapd stop >/dev/null 2>&1
   /sbin/chkconfig --del snmptrapd
   # remove stale autogenerated file
   rm -f %{_datadir}/snmp/mibs/.index
fi

%postun
if [ "$1" -ge "1" ]; then
    service snmpd condrestart >/dev/null 2>&1 || :
    service snmptrapd condrestart >/dev/null 2>&1 || :
fi

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc	AGENT.txt COPYING ChangeLog.trimmed EXAMPLE.conf FAQ NEWS PORTING README* TODO
%doc	local/passtest local/README.mib2c local/ipf-mod.pl
%dir	%{_sysconfdir}/snmp
%dir    /var/run/snmpd

%config(noreplace,missingok) %{_sysconfdir}/snmp/snmpd.conf
%config(noreplace) %{_initrddir}/snmpd
%config(noreplace) %{_initrddir}/snmptrapd
%config(noreplace) %{_sysconfdir}/logrotate.d/snmpd
%{_datadir}/snmp
%{_bindir}/ucd5820stat
%{_sbindir}/*
%attr(0644,root,root)	%{_mandir}/man[58]/*

%files utils
%defattr(-,root,root,-)

%{_bindir}/fixproc
%{_bindir}/ipf-mod.pl
%{_bindir}/encode_keychange
%{_bindir}/snmp*
%{_bindir}/traptoemail
%{_bindir}/mib2c-update
%attr(0644,root,root)	%{_mandir}/man1/*.1*

%files devel
%defattr(0644,root,root,0755)
%{_libdir}/lib*.so
/usr/include/*
%attr(0644,root,root)	%{_mandir}/man3/*.3.*
%attr(0755,root,root)	%{_bindir}/net-snmp-config

%files perl -f perl.lst
%defattr(-,root,root)
%{_bindir}/mib2c
%attr(0644,root,root)	%{_mandir}/man1/mib2c.1*
%attr(0644,root,root)   %{_mandir}/man3/*.3pm.*

%files libs
%defattr(0644,root,root,0755)
%{_libdir}/lib*.so.*
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Fri Mar  9 2012 Santi Saez <santi@woop.es> - 5.3.4-1
- Upgrade to upstream net-snmp 5.3.4 (required for PHP 5.4 branch on RHEL-4)
- Remove some legacy patches for RHEL-4

* Fri Jan 23 2009 Jan Safranek <jsafranek@redhat.com> 5.1.2-18
- fix regressions caused by new compilation flags

* Tue Nov 11 2008 Jan Safranek <jsafranek@redhat.com> 5.1.2-17
- fix UCD-SNMP-MIB::ssCpu* statistics - show one-minute load average instead
  of average since agent startup (#469607)
- fix HOST-RESOURCES-MIB::hrProcessorLoad - show one-minute load average instead
  of average since last query (#458996)
- fix UCD-SNMP-MIB::dskPercent to support filesystems > 32TB (#474161)

* Mon Oct  6 2008 Jan Safranek <jsafranek@redhat.com> 5.1.2-16
- snmpd no longer reports '-f' option as deprecated (#440220)
- fix parsing of command line parameters to allow hostnames in
  specification of transport address (#447839)
- fix IpAddress length on 64bit systems (#464764)
- fix a regression in 5.1.2-15 - snmptrapd no longer passes "<UNKNOWN>" 
  as hostname of sender of received trap (#437494)
- fix crash in bulk request processing (#469371)
- fix net-snmp package dependencies (#469679)
- fix crash when parsing '-LS', '-LF' and '-LO' command line arguments
  (#469620)

* Mon Oct  6 2008 Jan Safranek <jsafranek@redhat.com> 5.1.2-15
- fix trap forwarding from SMUX peers (#462016)
- implement 'v1trapaddress' snmpd.conf option to set fixed agent address in
  outgoing SNMPv1 traps (#437494)
- implement 'dontLogTCPWrappersConnects' snmpd.conf option to turn off
  logging of incoming connections (#444657)
- UDP responses are now sent from the interface that received the request
  (#447947)

* Wed Sep 10 2008 Jan Safranek <jsafranek@redhat.com> 5.1.2-14
- fix hrProcessorLoad on 64-bit systems (#461503)

* Wed Jun  4 2008 Jan Safranek <jsafranek@redhat.com> 5.1.2-13
- fix buffer overflow in perl module (CVE-2008-2292) (#449896)
- fix SNMPv3 authentication checks (unknown CVE) (#449896)

* Mon Nov  5 2007 Jan Safranek <jsafranek@redhat.com> 5.1.2-11.EL4.12
- fix bulkwalk security flaw (#366611)
- fix hrDeviceStatus and hrDeviceErrors missing during walk
  (#387091)
- fix crash when smux communication fails (#394591)
- store temporary files to /var/run/snmpd to prevent
  users to modify them and to make selinux happy (#417921)
- fix disk statistics of mount points with spaces (#325881)
- fix race condition when reading /proc/*/cmdline (#311241)
- fix linking with libcrypto on x86_64 (#409821)
- allow extensions to return INTEGER as int, not only long
  (#329631)
- fix 'authfail' config option (#426497)
- fix documentation of 'exec' statement - it does not cache results
  (#172984)
- correctly cut values to 32bits in UCD-DISKIO-MIB, preventing
  "truncating unsigned value to 32 bits (11)" to appear (#428948)
- fix override config option (#432182)
- fix snmpd.conf man page to mention ignoredisk working only in 
  hrDiskStorageTable and hrDeviceTable (#430069)
- fix net-snmp package dependencies (#434564)

* Thu Jul 19 2007 Jan Safranek <jsafranek@redhat.com> 5.1.2-11.EL4.11
- decrease logging of incoming connections, which slows down syslog
  (#241581)
- reference to net-snmp-config removed from snmpd.conf man page
  (#202599)
- fix snmpusm man page to describe all options (#202745)
- check if port number is valid (#205154)
- fix ssRawCpu* counters to wrap correctly on overflow (#223775)
- add rpm-devel to BuildPreReq to enable hrSWInstalled OID
  (#235885)
- snmptrapd survives logrotate (#239663)
- output of exec statement can be longer than 1023 characters
  (#242775)
- fix -M option of net-snmp-utils (#199165)
- add diskio MIB (#245380)
- snmpconf should generate config files with proper selinux context
  (#192447)
- fix snmpwalk / bulkwalk on TCP scalars (#248196)
 
* Thu Feb 22 2007 Radek Vokál <rvokal@redhat.com> 5.1.2-11.EL4.10
- add disman/event-mib support also for ia64 and s390x

* Wed Jan 10 2007 Radek Vokál <rvokal@redhat.com> 5.1.2-11.EL4.9
- add disman/event-mib for link notifications
- fix crash on unacknowledged informs
- fix for negative OID values 
- store pid in /var/run/snmpd.pid
- communication can be limited by tcp_wrappers
- Resolves: #202584 #211264 #212282 #211457 #220045 #206005

* Thu Nov 16 2006 Radek Vokál <rvokal@redhat.com> 5.1.2-11.EL4.8.hf1
- hotfix package fo #204729

* Wed Nov  8 2006 Radek Vokál <rvokal@redhat.com> 
- finally fixing bug #204729
- cleaning up the testing mess
- patch from Josef Moellers <josef.moellers@fujitsu-siemens.com>

* Mon Oct 23 2006 Radek Vokál <rvokal@redhat.com>
- testing version for bug #204729

* Wed Oct  4 2006 Radek Vokal <rvokal@redhat.com>
- processor table added (#201850)
- fixed snmptrapd init script, the path for config file is /etc/sysconfig/snmptrapd.options (#197752)
- fixed snmptrapd init script, don't overide user settings (#195702)
- fixed leak in snmptrapd (#192769)
- fixed snmpd init script, the path for config file is /etc/sysconfig/snmpd.options (#199450)

* Wed Sep 20 2006 Radek Vokal <rvokal@redhat.com>
- another leak fix 

* Fri Aug 11 2006 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.7.hf1
- hot fix for memleak in snmptrapd (#199376)

* Wed Apr 19 2006 Radek Vokál <rvokal@redhat.com> 5.1.2-11.EL4.7
- return inInOctets/ifOutOctets properly (#175536)

* Tue Apr 04 2006 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.6.hf1
- snmpd loops forever in host resources (#171135)
- fix agent crash for certain MIBs (#177692)
- fix crash when using invalid override line (#176922)
– fix snmptrapd segv with long trap (#187106)
- fix Extend MIB to work with TCP-wrapper (#173373)

* Tue Sep 06 2005 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.6
- agentx leak patches
- return IP address instead of MAC address (#167588)
- changes in tcp_dos patch

* Tue Aug 30 2005 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.5
- removed boggus code from tcp_dos patch (#166990)

* Thu Jul 14 2005 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.4
- CAN-2005-2177 fixed net-snmp denial of service (#162907)

* Mon May 09 2005 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.3
- snmpd reports gigabit Ethernet speeds using ethtool (#152480)
– fixed doublefree error (#157539)
- CAN-2005-1740 fixed insecure temporary file usage (#158769) <suse.de>

* Mon Apr 25 2005 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.2
- frequent restarts no longer crash snmpd (#152278)

* Wed Apr 20 2005 Radek Vokal <rvokal@redhat.com> 5.1.2-11.EL4.1
- lmSensors correctly recognized (#150199)
- fixed retreiving swap size (#150084)
- net-snmp no longer dies when querying hrSWInstalledLastUpdateTime (#155038)
- Fixed error building ASN.1 representation (#154421)
- 64bit network counters correctly wrap (#154455)
- net-snmp properly deals with large partitions (#153101) <jryska@redhat.com>
- unexpected length for type ASN_UNSIGNED fixed (#151892)
- snmptrapd initscript reads correctly options from /etc/snmp/snmptrapd.options (#154798)

* Fri Oct 15 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-11
- Logrotate support added (#125004)

* Thu Oct 14 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-10
- Extended the libwrap and bsdcompat patches

* Mon Oct 11 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-9
- Droped obsolete lm-sensors patch and enabled lmSensors module
- Marked several patches to be removed for 5.1.3

* Wed Sep 29 2004 Warren Togami <wtogami@redhat.com> 5.1.2-8
- remove README* that do not apply to Linux
- trim massive ChangeLog

* Wed Sep 22 2004 Florian La Roche <Florian.LaRoche@redhat.de>
- move ldconfig post/postun to libs subrpm

* Wed Sep 15 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-6
- Split out libs package for multilib compatibility

* Wed Sep 08 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-4
- New prereq for net-snmp-devel
- lelf check removed from configure.in (#128748)
- fixed snmpd coredump when sent SIGHUP (#127314)

* Tue Sep 07 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-3
- Agentx failed to send trap, fixed (#130752, #122338)

* Mon Sep 06 2004 Radek Vokal <rvokal@redhat.com> 5.1.2-2
- Patch fixing uninitalized stack variable in smux_trap_process (#130179)

* Wed Aug 18 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.2-1
- Update to 5.1.2
- Removed net-snmp-5.0.1-initializer patch, included upstream

* Tue Jun 15 2004 Phil Knirsch <pknirsch@redhat.com>
- Fixed small bug in snmptrapd initscript (#126000).

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 06 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.1-3
- Reworked the perl filelist stuff (Thanks to marius feraru).

* Thu Apr 08 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.1-2
- Added Kaj J. Niemi that fixes ipAdEntIfIndex problem (#119106)
- Added Kaj J. Niemi to shut up memshared message for 2.6 kernel (#119203)

* Tue Mar 23 2004 Phil Knirsch <pknirsch@redhat.com> 5.1.1-1
- Update to latest upstream version 5.1.1
- Included updated patches from Kaj J. Niemi (#118580).

* Thu Mar 18 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-12
- Hacked an ugly perl hack to get rid of perl RPATH problems.
- Fixed 64bit patch and applied it. ;-)

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-10
- Included 64bit fix from Mark Langsdorf (#114645).

* Tue Feb 03 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-9
- Reverted removal of _includir redefiniton due to php-snmp dependancy.
- Remove SO_BSDCOMPAT setsockopt() call, deprecated.

* Thu Jan 29 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-8
- Quite a bit of specfile cleanup from Marius FERARU.

* Thu Jan 22 2004 Thomas Woerner <twoerner@redhat.com> 5.1-7
- enabled pie (snmpd, snmptrapd) - postponed for ia64
- added --with-pic to configure call

* Thu Jan 15 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-6
- Fixed 64bit build problems when 32bit popt lib is installed.

* Tue Jan 13 2004 Phil Knirsch <pknirsch@redhat.com> 5.1-5
- rebuilt

* Sun Jan 11 2004 Florian La Roche <Florian.LaRoche@redhat.de> 5.1-4
- rebuild for new rpm

* Wed Dec 10 2003 Phil Knirsch <pknirsch@redhat.com> 5.1-3
- Removed snmpcheck again, needs perl(Tk) which we don't ship (#111194).
- Fixed getopt definition in include file (#111209).
- Included Kaj J. Niemi's patch for broken perl module (#111319).
- Included Kaj J. Niemi's patch for broken async getnext perl call (#111479).
- Included Kaj J. Niemi's patch for broken hr_storage (#111502).

* Wed Nov 26 2003 Phil Knirsch <pknirsch@redhat.com> 5.1-2
- Included BuildPrereq on lm_sensors-devel on x86 archs (#110616).
- Fixed deprecated initscript options (#110618).

* Wed Nov 19 2003 Phil Knirsch <pknirsch@redhat.com> 5.1-1
- Updated to latest net-snmp-5.1 upstream version.
- Tons of specfile and patch cleanup.
- Cleaned up perl stuff (mib2c etc, see #107707).
- Added lm_sensors support patch for x86 archs from Kaj J. Niemi (#107618).
- Added support for custom mib paths and mibs to snmptrapd initscript (#102762)

* Mon Oct 13 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.9-2
- Due to rpm-devel we need elfutils-devel, too (#103982).

* Mon Sep 29 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.9-1
- Updated to latest upstream version net-snmp-5.0.9
- Added patch to fix net-snmp-perl problems (#105842).

* Tue Sep 23 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- allow compiling without tcp_wrappers

* Wed Sep 17 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-11.1
- rebuilt

* Wed Sep 17 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-11
- Fixed permission for net-snmp-config in net-snmp-devel

* Mon Sep 08 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-10.1
- rebuilt

* Mon Sep 08 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-10
- Moved net-snmp-config into devel package (#103927)

* Fri Aug 22 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-9.1
- rebuilt

* Thu Aug 21 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-9
- Added sample config to make net-snmp RFC 1213 compliant.

* Fri Aug 15 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-8
- Fixed problem with perl option (#102420).
- Added patch for libwrap fix (#77926).

* Tue Aug 12 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-7.1
- rebuilt

* Tue Aug 12 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-7
- Fixed build problems on ppc64
- Fixed double packaged manpages (#102075).

* Thu Aug 07 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed problem with new proc output (#98619, #89960).

* Wed Aug 06 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed ro/rw problem with v2 and v3 request (#89612)

* Tue Aug 05 2003 Phil Knirsch <pknirsch@redhat.com>
- Fixed permission problem for debuginfo (#101456)

* Thu Jul 31 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-6.1
- Fixed file list for latest build.

* Thu Jul 31 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-6
- Fixed build problems for net-snmp-perl.

* Sun Jul 27 2003 Florian La Roche <Florian.LaRoche@redhat.de> 5.0.8-5
- actually apply ipv6 patch

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 29 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-3
- bumped release and rebuilt.

* Tue Apr 29 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-2
- Hack to make it build on 64bit platforms with /usr/lib64 correctly.
- Fixed bug #85071 (leak of open descriptors for ipv6).

* Fri Mar 28 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.8-1
- Updated to latest upstream version 5.0.8 (bug #88580)

* Thu Feb 13 2003 Phil Knirsch <pknirsch@redhat.com>
- Included generation of perl stuff. Thanks to Harald Hoyer.

* Wed Feb 12 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.7-1
- Updated to net-snmp-5.0.7. Fixed especially the performance problem with
  limited trees.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-17
- Fixed ucd-snmp.redhat.conf (#78391).
- Fixed snmpwalk examples in config file.

* Mon Feb 10 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-15
- Fixed invalid SMUX packet (#83487).

* Thu Feb 06 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-14
- Fixed the libdir problem.

* Wed Feb 05 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-13
- Updated the old libtool rpath patch.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 5.0.6-12
- rebuilt

* Tue Jan 14 2003 Phil Knirsch <pknirsch@redhat.com> 5.0.6-11
- Updated nolibelf patch and activated it again.

* Tue Jan  7 2003 Nalin Dahyabhai <nalin@redhat.com> 5.0.6-10
- Rebuild

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-9
- Added bzip2-devel to BuildPreReq (#76086, #70199).

* Thu Nov 28 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-8
- Added patch to increase SMUXMAXSTRLEN. 

* Thu Nov  7 2002 Tim Powers <timp@redhat.com> 5.0.6-6
- rebuilt to fix broken deps
- remove files from the buildroot that we don't want to ship

* Thu Nov  7 2002 Joe Orton <jorton@redhat.com> 5.0.6-5
- add fix for -DUCD_COMPATIBLE (#77405)

* Thu Nov 07 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-4
- Another bump required. Some more specfile changes.

* Wed Nov 06 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-3
- Bumped release and rebuilt.
- Removed all dbFOO cruft again.

* Wed Oct 09 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.6-2
- Updated to latest released version.

* Sat Aug 31 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not link against -lelf

* Thu Jun 27 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.1-5
- Added --enable-ucd-snmp-compatibility for compatibility with older version
  and fixed installation thereof.
- Got rid of the perl(Tk) dependancy by removing snmpcheck.
- Include /usr/include/ucd-snmp in the filelist.
- Fixed a problem with the ucd-snmp/version.h file.

* Wed Jun 26 2002 Phil Knirsch <pknirsch@redhat.com> 5.0.1-1
- Updated to 5.0.1
- Dropped --enable-reentrant as it's currently broken

* Tue Apr 23 2002 Phil Knirsch <pknirsch@redhat.com> 5.0-1
- Switch to latest stable version, 5.0
- Renamed the packate to net-snmp and obsoleted ucd-snmp.

* Wed Apr 17 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4-3
- Fixed problem with reload in initscript (#63526).

* Mon Apr 15 2002 Tim Powers <timp@redhat.com> 4.2.4-2
- rebuilt in new environment

* Mon Apr 15 2002 Tim Powers <timp@redhat.com> 4.2.4-1
- update to 4.2.4 final

* Sat Apr 13 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-5
- Added some missing files to the %files section.

* Tue Apr 09 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-4
- Hardcoded the ETC_MNTTAB to point to "/etc/mtab".

* Mon Apr 08 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-3
- Removed the check for dbFOO as we don't want to add another requirement.

* Fri Apr 05 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-2
- Added missing BuildPrereq to openssl-devel (#61525)

* Thu Apr 04 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre3-1
- Added ucd5820stat to the files section.
- Updated to latest version (4.2.4.pre3)

* Mon Mar 18 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.4.pre2-1
- Updated to latest version (4.2.4.pre2)

* Tue Jan 29 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.3-4
- Added the snmptrapd init script as per request (#49205)
- Fixed the again broken rpm query stuff (#57444)
- Removed all old and none-used db related stuff (libs and header checks/files)

* Mon Jan 07 2002 Phil Knirsch <pknirsch@redhat.com> 4.2.3-2
- Included the Axioma Security Research fix for snmpnetstat from bugtraq.

* Mon Dec 03 2001 Phil Knirsch <phil@redhat.de> 4.2.3-1
- Update to 4.2.3 final.
- Fixed libtool/rpath buildroot pollution problem.
- Fixed library naming problem.

* Fri Oct  5 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed a server segfault for snmpset operation (#53640). Thanks to Josh Giles
  and Wes Hardaker for the patch.

* Mon Sep 10 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed problem with RUNTESTS script.

* Tue Sep  4 2001 Preston Brown <pbrown@redhat.com>
- fixed patch related to bug #35016 (Dell)

* Fri Aug 24 2001 Philipp Knirsch <pknirsch@redhat.de> 4.2.1-6
- Fixed snmpd description (#52366)

* Wed Aug 22 2001 Philipp Knirsch <pknirsch@redhat.de>
- Final bcm5820 fix. Last one was broken.
- Fixed bugzilla bug (#51960) where the binaries contained rpath references.

* Wed Aug 15 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed a couple of security issues:
  o /tmp race and setgroups() privilege problem
  o Various buffer overflow and format string issues.
  o One signedness problem in ASN handling.
- Fixed an important RFE to support bcm5820 cards. (#51125)

* Fri Jul 20 2001 Philipp Knirsch <pknirsch@redhat.de>
- Removed tkmib from the package once again as we don't ship the Tk.pm CPAN
  perl module required to run it (#49363)
- Added missing Provides for the .so.0 libraries as rpm doesn't seem to find
  those during the build anymore (it used to) (#46388)

* Thu Jul 19 2001 Philipp Knirsch <pknirsch@redhat.de>
- Enabled IPv6 support (RFE #47764)
- Hopefully final fix of snmpwalk problem (#42153). Thanks to Douglas Warzecha
  for the patch and Matt Domsch for reporting the problem.

* Tue Jun 26 2001 Philipp Knirsch <pknirsch@redhat.de>
- Fixed smux compilation problems (#41452)
- Fixed wrong paths displayed in manpages (#43053)

* Mon Jun 25 2001 Philipp Knirsch <pknirsch@redhat.de>
- Updated to 4.2.1. Removed 2 obsolete patches (fromcvs and #18153)
- Include /usr/share/snmp/snmpconf in %files

* Wed Jun 13 2001 Than Ngo <than@redhat.com>
- fix to use libwrap in distro
- add buildprereq: tcp_wrappers

* Fri Jun  1 2001 Bill Nottingham <notting@redhat.com>
- add a *new* patch for IP address return sizes

* Fri Apr 20 2001 Bill Nottingham <notting@redhat.com>
- add patch so that only four bytes are returned for IP addresses on ia64 (#32244)

* Wed Apr 11 2001 Bill Nottingham <notting@redhat.com>
- rebuild (missing alpha packages)

* Fri Apr  6 2001 Matt Wilson <msw@redhat.com>
- added ucd-snmp-4.2-null.patch to correcly handle a NULL value (#35016)

* Tue Apr  3 2001 Preston Brown <pbrown@redhat.com>
- clean up deinstallation (#34168)

* Tue Mar 27 2001 Matt Wilson <msw@redhat.com>
- return a usable RETVAL when running "service snmpd status" (#33571)

* Tue Mar 13 2001 Matt Wilson <msw@redhat.com>
- configure with --enable-reentrant and added "smux" and "agentx" to
  --with-mib-modules= argument (#29626)

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Mon Feb 26 2001 Tim Powers <timp@redhat.com>
- fixed initscript, for reload and restart it was start then stop,
  fixed. (#28477)

* Fri Feb  2 2001 Trond Eivind Glomsr�d <teg@redhat.com>
- i18nize initscript

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- don't depend on /etc/init.d so that package will work with 6.2.
- perl path fiddles no longer needed.
- rely on brp-compress frpm rpm to compress man pages.
- patch from ucd-snmp CVS (Wes Hardaker).
- configure.in needs to check for rpm libraries correctly (#23033).
- add simple logrotate script (#21399).
- add options to create pidfile and log with syslog with addresses (#23476).

* Sat Dec 30 2000 Jeff Johnson <jbj@redhat.com>
- package for Red Hat 7.1.

* Thu Dec 07 2000 Wes Hardaker <hardaker@users.sourceforge.net>
- update for 4.2

* Thu Oct 12 2000 Jeff Johnson <jbj@redhat.com>
- add explicit format for syslog call (#18153).

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Thu Jul 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild per Trond's request.

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix syntax error that crept in with condrestart

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Preston Brown <pbrown@redhat.com>
- move initscript and add condrestart magic

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- fix %%attr on man pages

* Mon Jun 12 2000 Jeff Johnson <jbj@redhat.com>
- tkmib doco had #!/usr/bin/perl55
- include snmpcheck and tkmib again (still needs some CPAN module, however).

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- update to 4.1.2.
- FHS packaging.
- patch for rpm 4.0.

* Thu May 18 2000 Trond Eivind Glomsr�d <teg@redhat.com>
- add version to buildroot
- rebuilt with new libraries

* Sun Feb 27 2000 Jeff Johnson <jbj@redhat.com>
- default config was broken (from Wes Hardaker) (#9752)

* Sun Feb 13 2000 Jeff Johnson <jbj@redhat.com>
- compressed man pages.

* Fri Feb 11 2000 Wes Hardaker <wjhardaker@ucdavis.edu>
- update to 4.1.1

* Sat Feb  5 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- change %postun to %preun

* Thu Feb 3 2000 Elliot Lee <sopwith@redhat.com>
- Don't ship tkmib, since we don't ship the perl modules needed to run it.
(Bug #4881)

* Tue Aug 31 1999 Jeff Johnson <jbj@redhat.com>
- default config permits RO access to system group only (Wed Hardaker).

* Sun Aug 29 1999 Jeff Johnson <jbj@redhat.com>
- implement suggestions from Wes Hardaker.

* Fri Aug 27 1999 Jeff Johnson <jbj@redhat.com>
- stateless access to rpm database.

* Wed Aug 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 4.0.1.

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Sat Jun 12 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.6.2 (#3219,#3259).
- add missing man pages (#3057).

* Thu Apr  8 1999 Wes Hardaker <wjhardaker@ucdavis.edu>
- fix Source0 location.
- fix the snmpd.conf file to use real community names.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 3.6.1, fix configuration file stuff.

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- restore host resources mib
- simplified config file
- rebuild for 6.0.

* Tue Dec 22 1998 Bill Nottingham <notting@redhat.com>
- remove backup file to fix perl dependencies

* Tue Dec  8 1998 Jeff Johnson <jbj@redhat.com>
- add all relevant rpm scalars to host resources mib.

* Sun Dec  6 1998 Jeff Johnson <jbj@redhat.com>
- enable libwrap (#253)
- enable host module (rpm queries over SNMP!).

* Mon Oct 12 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries

* Fri Oct  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.3.
- don't include snmpcheck until perl-SNMP is packaged.

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- ucd-snmpd.init: start daemon w/o -f.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- don't start snmpd unless requested
- start snmpd after pcmcia.

* Sun Jun 21 1998 Jeff Johnson <jbj@redhat.com>
- all but config (especially SNMPv2p) ready for prime time

* Sat Jun 20 1998 Jeff Johnson <jbj@redhat.com>
- update to 3.5.

* Tue Dec 30 1997 Otto Hammersmith <otto@redhat.com>
- created the package... possibly replace cmu-snmp with this.
