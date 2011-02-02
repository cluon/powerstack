Name: mysqlclient14
Version: 4.1.22
Release: 1
Summary: Backlevel MySQL shared libraries.
License: GPL
Group: Applications/Databases
URL: http://www.mysql.com

Source0: http://dev.mysql.com/get/Downloads/MySQL-4.1/mysql-%{version}.tar.gz
Source5: my_config.h
# Working around perl dependency checking bug in rpm FTTB. Remove later.
Source999: filter-requires-mysql.sh 
Patch1: mysql-libdir.patch
Patch2: mysql-errno.patch
Patch3: mysql-libtool.patch
Patch4: mysql-testing.patch
Patch5: mysql-no-atomic.patch
Patch8: mysql-buffer-warning.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prereq: /sbin/ldconfig, /sbin/install-info, grep, fileutils, chkconfig
BuildRequires: gperf, perl, readline-devel, openssl-devel
BuildRequires: gcc-c++, ncurses-devel, zlib-devel
BuildRequires: libtool automake autoconf
Requires: bash

# Working around perl dependency checking bug in rpm FTTB. Remove later.
%define __perl_requires %{SOURCE999}

# Force include and library files into a nonstandard place
%{expand: %%define _origincludedir %{_includedir}}
%{expand: %%define _origlibdir %{_libdir}}
%define _includedir %{_origincludedir}/mysql4
%define _libdir %{_origlibdir}/mysql4

%description
This package contains backlevel versions of the MySQL client libraries
for use with applications linked against them.  These shared libraries
were created using MySQL %{version}.

%package devel

Summary: Backlevel files for development of MySQL applications.
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
%patch8 -p1

libtoolize --force
aclocal
automake
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
	--with-vio \
	--with-openssl \
	--without-debug \
	--enable-shared \
	--without-bench \
	--localstatedir=/var/lib/mysql \
	--with-unix-socket-path=/var/lib/mysql/mysql.sock \
	--with-mysqld-user="mysql" \
	--with-extra-charsets=all \
	--enable-local-infile \
	--enable-large-files=yes --enable-largefile=yes \
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
mv -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient.so.14.*.* .
mv -f ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient_r.so.14.*.* .
cp -p -d ${RPM_BUILD_ROOT}%{_libdir}/mysql/libmysqlclient*.so.* .
popd
pushd ${RPM_BUILD_ROOT}%{_libdir}/mysql
ln -s ../../mysql/libmysqlclient.so.14.*.* .
ln -s ../../mysql/libmysqlclient_r.so.14.*.* .
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
rm -rf $RPM_BUILD_ROOT%{_mandir}/man*

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
* Wed Feb 2 2011 Santi Saez <santi@woop.es> 4.1.22-1
- Backlevel MySQL v4.1.22 shared libraries, based on Remi Collect mysqlclient14.spec 

* Tue May 01 2007 Remi Collet <RPMS@FamilleCollet.com> 4.1.22-1.###.remi
- update to 4.1.22

* Wed Jul 26 2006 Remi Collet <RPMS@FamilleCollet.com> 4.1.20-1.fc4.remi
- update to 4.1.20

* Sat Jan 21 2006 Remi Collet <RPMS@FamilleCollet.com> 4.1.16-1.fc{3,4}.remi
- update to 4.1.16

* Thu Dec 15 2005 Tom Lane <tgl@redhat.com> 4.1.14-4
- fix my_config.h for 64-bit and ppc platforms

* Wed Dec 14 2005 Tom Lane <tgl@redhat.com> 4.1.14-3
- oops, looks like we want uname -i not uname -m

* Wed Dec 14 2005 Tom Lane <tgl@redhat.com> 4.1.14-2
- Make my_config.h architecture-independent for multilib installs;
  put the original my_config.h into my_config_$ARCH.h
- Add license info (COPYING, EXCEPTIONS-CLIENT) to the shipped documentation
- Add -fwrapv to CFLAGS so that gcc 4.1 doesn't break it

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov  3 2005 Tom Lane <tgl@redhat.com> 4.1.14-1
- created based on latest FC-4 package and mysqlclient10 specfile

* Sat Oct  8 2005 Remi Collet <Remi.Collet@univ-reims;fr> 4.1.14-0.1.fc3.remi
- first build of mysqlclient14

* Fri Apr  8 2005 Tom Lane <tgl@redhat.com> 3.23.58-6
- Avoid dependency on <asm/atomic.h>, cause it won't build anymore on ia64.
- Override configure thread library test to suppress HAVE_LINUXTHREADS check

* Sun Mar  6 2005 Tom Lane <tgl@redhat.com> 3.23.58-5
- Rebuild with gcc4.

* Fri Oct 29 2004 Tom Lane <tgl@redhat.com> 3.23.58-4
- Seems we do need to export mysqld_error.h after all.

* Fri Oct 29 2004 Tom Lane <tgl@redhat.com> 3.23.58-3
- Handle ldconfig more cleanly (put a file in /etc/ld.so.conf.d/).
- Make .so files in devel be just symlinks to those in main package.

* Thu Oct 28 2004 Tom Lane <tgl@redhat.com> 3.23.58-2
- Install libraries and mysql_config under %%{_libdir}/mysql3/mysql,
  to provide an easier way to build dependent packages.

* Wed Oct 27 2004 Tom Lane <tgl@redhat.com> 3.23.58-1
- Update to latest 3.x release, add relevant patches from mysql package
- add -devel subpackage to allow building other packages against LGPL libs

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu May 29 2003 Patrick Macdonald <patrickm@redhat.com> 3.23.56-1
- created - originated from the mysql package
- removed all other files and install/uninstall/test procedures
- changed description
