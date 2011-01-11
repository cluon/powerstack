Name: mysqlclient15
Version: 5.0.67
Release: 1
Summary: Backlevel MySQL shared libraries
License: GPL
Group: Applications/Databases
URL: http://www.mysql.com

Source0: http://dev.mysql.com/get/Downloads/MySQL-5.0/mysql-%{version}.tar.gz
Source1: mysql.init
Source3: my.cnf
Source4: scriptstub.c
Source5: my_config.h
# Working around perl dependency checking bug in rpm FTTB. Remove later.
Source999: filter-requires-mysql.sh 
Patch1: mysql-libdir.patch
Patch2: mysql-errno.patch
Patch3: mysql-stack.patch
Patch4: mysql-5.0.67-testing.patch
Patch5: mysql-no-atomic.patch
Patch6: mysql-rpl_ddl.patch
Patch7: mysql-rpl-test.patch
Patch8: mysql-install-test.patch
Patch9: mysql-bdb-link.patch
Patch10: mysql-bdb-open.patch
#Patch11: mysql-innodb-crash.patch
#Patch12: mysql-ssl.patch
Patch13: mysql-no-dbug.patch
Patch14: mysql-5.0.67-ss-test.patch
Patch15: mysql-stack-guard.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prereq: /sbin/ldconfig, /sbin/install-info, grep, fileutils, chkconfig
BuildRequires: gperf, perl, readline-devel, openssl-devel
BuildRequires: gcc-c++, ncurses-devel, zlib-devel
BuildRequires: libtool automake autoconf
# make test requires time and ps
BuildRequires: time procps

Requires: bash

# Working around perl dependency checking bug in rpm FTTB. Remove later.
%define __perl_requires %{SOURCE999}

# Force include and library files into a nonstandard place
%{expand: %%define _origincludedir %{_includedir}}
%{expand: %%define _origlibdir %{_libdir}}
%define _includedir %{_origincludedir}/mysql50
%define _libdir %{_origlibdir}/mysql50

%description
This package contains backlevel versions of the MySQL client libraries
for use with applications linked against them.  These shared libraries
were created using MySQL %[version}.

%package devel

Summary: Nextlevel files for development of MySQL applications.
License: GPL
Group: Applications/Databases
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed for
developing MySQL applications using backlevel client libraries.

%prep
%setup -q -n mysql-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p1
#%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

libtoolize --force
aclocal
automake --add-missing -Wno-portability
autoconf
autoheader

%build
CFLAGS="%{optflags} -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
CFLAGS="$CFLAGS -fno-strict-aliasing -fwrapv"
%ifarch alpha
# Can't link C++ objects into an executable without this. Odd!
# -ECL 2002-12-19
CFLAGS="$CFLAGS -fPIC"
%endif
CXXFLAGS="$CFLAGS -fno-rtti -fno-exceptions"
export CFLAGS CXXFLAGS

%configure \
	--with-readline \
	--with-openssl \
	--without-debug \
	--enable-shared \
	--without-bench \
	--without-server \
	--without-docs \
	--without-man \
	--localstatedir=/var/lib/mysql \
	--with-unix-socket-path=/var/lib/mysql/mysql.sock \
	--with-mysqld-user="mysql" \
	--with-extra-charsets=all \
	--enable-local-infile \
	--enable-largefile \
	--enable-thread-safe-client \
	--disable-dependency-tracking \
	--with-named-thread-libs="-lpthread"

make %{?_smp_mflags}
make check

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

install -m 644 include/my_config.h $RPM_BUILD_ROOT%{_includedir}/mysql/my_config_`uname -i`.h
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_includedir}/mysql/

# We want the .so files both in regular _libdir (for execution) and
# in special _libdir/mysql4 directory (for convenient building of clients).
# The ones in the latter directory should be just symlinks though.
mkdir -p ${RPM_BUILD_ROOT}%{_origlibdir}/mysql
pushd ${RPM_BUILD_ROOT}%{_origlibdir}/mysql
mv -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient.so.15.*.* .
mv -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient_r.so.15.*.* .
cp -p -d ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient*.so.* .
popd
pushd ${RPM_BUILD_ROOT}%{_libdir}/mysql
ln -s ../../mysql/libmysqlclient.so.15.*.* .
ln -s ../../mysql/libmysqlclient_r.so.15.*.* .
popd

# Put the config script into special libdir
cp -p $RPM_BUILD_ROOT%{_bindir}/mysql_config ${RPM_BUILD_ROOT}%{_libdir}/mysql

rm -rf $RPM_BUILD_ROOT%{_prefix}/mysql-test
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/*.a
rm -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/mysql
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_libexecdir}
rm -rf $RPM_BUILD_ROOT%{_infodir}/*
rm -rf $RPM_BUILD_ROOT%{_mandir}/man?/*

mkdir -p $RPM_BUILD_ROOT/etc/ld.so.conf.d
echo "%{_origlibdir}/mysql" > $RPM_BUILD_ROOT/etc/ld.so.conf.d/%{name}-%{_arch}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING EXCEPTIONS-CLIENT

%{_origlibdir}/mysql/libmysqlclient*.so.*
/etc/ld.so.conf.d/*

%files devel
%defattr(-,root,root)
%{_includedir}
%{_libdir}

%changelog
* Sat Nov 08 2008 Remi Collet <RPMS@FamilleCollet.com> 5.0.67-1.fc10.remi
- F9 rebuild
- update to 5.0.67
 
* Sat Apr 19 2008 Remi Collet <RPMS@FamilleCollet.com> 5.0.51a-1.fc9.remi
- F9 rebuild
- update to 5.0.51a 

* Tue Aug 14 2007 Remi Collet <RPMS@FamilleCollet.com> 5.0.45-1.fc7.remi
- build for backward compatibility on F7 (for use with mysql 5.2.x)

* Sat Jan 21 2006 Remi Collet <RPMS@FamilleCollet.com> 5.0.18-1.fc{3,4}.remi
- first build of mysqlclient15
