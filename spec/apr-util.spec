
%define apuver 1

Summary: Apache Portable Runtime Utility library
Name: apr-util
Version: 1.2.7
Release: 12
License: Apache Software License 2.0
Group: System Environment/Libraries
URL: http://apr.apache.org/
Source0: %{name}-%{version}.tar.gz
Patch0: apr-util-1.2.2-exports.patch
Patch1: apr-util-1.2.6-ldap.patch
Patch2: apr-util-1.2.7-pkgconf.patch
Patch3: apr-util-1.2.7-ac260.patch
Patch4: apr-util-1.2.7-xmlnspace.patch
Patch5: apr-util-1.2.7-dbddso.patch
Patch6: apr-util-1.2.7-dbdmysql.patch
Patch7: apr-util-1.2.7-expat.patch
# Security fixes
Patch20: apr-util-1.2.7-CVE-2009-0023.patch
Patch21: apr-util-1.2.7-CVE-2009-1955.patch
Patch22: apr-util-1.2.7-CVE-2009-1956.patch
Patch23: apr-util-1.2.7-CVE-2009-2412.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: autoconf, doxygen, apr-devel >= 1.2.0
BuildRequires: openldap-devel, db4-devel, expat-devel
BuildRequires: postgresql-devel, sqlite-devel >= 3.0.0
BuildRequires: e2fsprogs-devel, mysql-devel
Conflicts: subversion < 0.20.1-2

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.  This library
contains additional utility interfaces for APR; including support
for XML, LDAP, database interfaces, URI parsing and more.

%package devel
Group: Development/Libraries
Summary: APR utility library development kit
Requires: apr-util = %{version}-%{release}, apr-devel, pkgconfig
Requires: openldap-devel, db4-devel, expat-devel
Conflicts: subversion-devel < 0.20.1-2

%description devel
This package provides the support files which can be used to 
build applications using the APR utility library.  The mission 
of the Apache Portable Runtime (APR) is to provide a free 
library of C data structures and routines.

%package docs
Group: Development/Documentation
Summary: Documentation for the Apache Portable Runtime Utility library

%description docs
This package provides documentation for the Apache Portable Runtime Utility 
library. The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines.

%package mysql
Group: Development/Libraries
Summary: APR utility library MySQL DBD driver
BuildRequires: mysql-devel
Requires: apr-util = %{version}-%{release}

%description mysql
This package provides the MySQL driver for the apr-util DBD
(database abstraction) interface.

%prep
%setup -q
%patch0 -p1 -b .exports
%patch1 -p1 -b .ldap
%patch2 -p1 -b .pkgconf
%patch3 -p1 -b .ac260
%patch4 -p1 -b .xmlnspace
%patch5 -p1 -b .dbddso
%patch6 -p1 -b .dbdmysql
%patch7 -p1 -b .expat

%patch20 -p1 -b .cve0023
%patch21 -p1 -b .cve1955
%patch22 -p1 -b .cve1956
%patch23 -p1 -b .cve2412

%build
autoheader && autoconf
export LDFLAGS=-L%{_libdir}/mysql
%configure --with-apr=%{_prefix} \
        --includedir=%{_includedir}/apr-%{apuver} \
        --with-expat=%{_prefix} \
        --with-ldap --without-gdbm \
        --with-sqlite3 --with-pgsql --with-mysql \
        --with-berkeley-db \
        --without-sqlite2 \
        --enable-dbd-dso
make %{?_smp_mflags} && make dox

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Documentation
mv docs/dox/html html

# Unpackaged files; remove the static libaprutil
rm -f $RPM_BUILD_ROOT%{_libdir}/aprutil.exp \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.a

# And remove the reference to the static libaprutil from the .la
# file.
sed -i '/^old_library/s,libapr.*\.a,,' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la

# Remove unnecessary exports from dependency_libs
sed -ri '/^dependency_libs/{s,-l(pq|sqlite[0-9]|rt|dl|uuid) ,,g}' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la

# Trim libtool DSO cruft
rm -f $RPM_BUILD_ROOT%{_libdir}/apr-util-%{apuver}/*.*a

%check
# Run the less verbose test suites
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$(($RANDOM % 255 + 1))
# Pick up DBD DSOs
export LD_LIBRARY_PATH=$PWD/dbd/.libs
cd test
make %{?_smp_mflags} testall testrmm testdbm
./testall -v -q
./testrmm
./testdbm auto tsdbm
./testdbm -tDB auto tbdb.db

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE NOTICE
%dir %{_libdir}/apr-util-%{apuver}
%{_libdir}/libaprutil-%{apuver}.so.*
%{_libdir}/apr-util-%{apuver}/apr_dbd_sqlite*
%{_libdir}/apr-util-%{apuver}/apr_dbd_pgsql*

%files devel
%defattr(-,root,root,-)
%{_bindir}/apu-%{apuver}-config
%{_libdir}/libaprutil-%{apuver}.*a
%{_libdir}/libaprutil-%{apuver}.so
%{_includedir}/apr-%{apuver}/*.h
%{_libdir}/pkgconfig/*.pc

%files mysql
%defattr(-,root,root,-)
%{_libdir}/apr-util-%{apuver}/apr_dbd_mysql*

%files docs
%doc --parents html

%changelog
* Wed Feb  3 2010 Joe Orton <jorton@redhat.com> - 1.2.7-11
- fix mysql driver linkage (#493142)

* Tue Jan 12 2010 Joe Orton <jorton@redhat.com> - 1.2.7-10
- fix expat detection in multilib environments

* Tue Jan  5 2010 Joe Orton <jorton@redhat.com> - 1.2.7-9
- enable DBD DSO support, add mysql DBD support (#252073, #493142)

* Mon Jan  4 2010 Joe Orton <jorton@redhat.com> - 1.2.7-8
- add security fix for CVE-2009-2412 (#515714)
- add security fixes for CVE-2009-0023, CVE-2009-1955, 
  and CVE-2009-1956 (#504561)

* Tue Jan  8 2008 Joe Orton <jorton@redhat.com> 1.2.7-7.el5
- apr_xml: fix XML attribute namespace handling (#234852)

* Wed Jan 17 2007 Deepak Bhole <dbhole@redhat.com> 1.2.7-6
- Resolves: bz222715. Moved the documentation to a -docs subpackage.

* Wed Jul 19 2006 Joe Orton <jorton@redhat.com> 1.2.7-3
- fix buildconf with autoconf 2.60

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.2.7-2.1
- rebuild

* Tue May  2 2006 Joe Orton <jorton@redhat.com> 1.2.7-2
- update to 1.2.7
- use pkg-config in apu-1-config to make it libdir-agnostic

* Thu Apr  6 2006 Joe Orton <jorton@redhat.com> 1.2.6-2
- update to 1.2.6
- define LDAP_DEPRECATED in apr_ldap.h (r391985, #188073)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.2.2-4.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.2.2-4.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 30 2006 Joe Orton <jorton@redhat.com> 1.2.2-4
- rebuild to drop reference to libexpat.la

* Wed Jan 18 2006 Joe Orton <jorton@redhat.com> 1.2.2-3
- disable sqlite2 support
- BuildRequire e2fsprogs-devel
- enable malloc paranoia in %%check

* Tue Jan  3 2006 Jesse Keating <jkeating@redhat.com> 1.2.2-2.2
- rebuilt again

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec  6 2005 Joe Orton <jorton@redhat.com> 1.2.2-2
- trim exports from .la file/--libs output (#174924)

* Fri Nov 25 2005 Joe Orton <jorton@redhat.com> 1.2.2-1
- update to 1.2.2

* Thu Oct 20 2005 Joe Orton <jorton@redhat.com> 0.9.7-3
- fix epoch again

* Thu Oct 20 2005 Joe Orton <jorton@redhat.com> 0.9.7-2
- update to 0.9.7
- drop static libs (#170051)

* Tue Jul 26 2005 Joe Orton <jorton@redhat.com> 0.9.6-3
- add FILE bucket fix for truncated files (#159191)
- add epoch to dependencies

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 0.9.6-2
- rebuild

* Wed Feb  9 2005 Joe Orton <jorton@redhat.com> 0.9.6-1
- update to 0.9.6

* Wed Jan 19 2005 Joe Orton <jorton@redhat.com> 0.9.5-3
- restore db-4.3 detection lost in 0.9.5 upgrade

* Wed Jan 19 2005 Joe Orton <jorton@redhat.com> 0.9.5-2
- rebuild

* Mon Nov 22 2004 Joe Orton <jorton@redhat.com> 0.9.5-1
- update to 0.9.5

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 0.9.4-19
- actually explicitly check for and detect db-4.3.

* Thu Nov 11 2004 Jeff Johnson <jbj@jbj.org> 0.9.4-18
- rebuild against db-4.3.21.

* Fri Sep 17 2004 Joe Orton <jorton@redhat.com> 0.9.4-17
- add security fix for CAN-2004-0786

* Sat Jun 19 2004 Joe Orton <jorton@redhat.com> 0.9.4-16
- have -devel require matching release of apr-util

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  1 2004 Joe Orton <jorton@redhat.com> 0.9.4-14
- fix use of SHA1 passwords (#119651)

* Tue Mar 30 2004 Joe Orton <jorton@redhat.com> 0.9.4-13
- remove fundamentally broken check_sbcs() from xlate code

* Fri Mar 19 2004 Joe Orton <jorton@redhat.com> 0.9.4-12
- tweak xlate fix

* Fri Mar 19 2004 Joe Orton <jorton@redhat.com> 0.9.4-11
- rebuild with xlate fixes and tests enabled

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com> 0.9.4-10.1
- rebuilt

* Tue Mar  2 2004 Joe Orton <jorton@redhat.com> 0.9.4-10
- rename sdbm_* symbols to apu__sdbm_*

* Mon Feb 16 2004 Joe Orton <jorton@redhat.com> 0.9.4-9
- fix sdbm apr_dbm_exists() on s390x/ppc64

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com> 0.9.4-8
- rebuilt

* Thu Feb  5 2004 Joe Orton <jorton@redhat.com> 0.9.4-7
- fix warnings from use of apr_optional*.h with gcc 3.4

* Thu Jan 29 2004 Joe Orton <jorton@redhat.com> 0.9.4-6
- drop gdbm support

* Thu Jan  8 2004 Joe Orton <jorton@redhat.com> 0.9.4-5
- fix DB library detection

* Sat Dec 13 2003 Jeff Johnson <jbj@jbj.org> 0.9.4-4
- rebuild against db-4.2.52.

* Mon Oct 13 2003 Jeff Johnson <jbj@jbj.org> 0.9.4-3
- rebuild against db-4.2.42.

* Mon Oct  6 2003 Joe Orton <jorton@redhat.com> 0.9.4-2
- fix 'apu-config --apu-la-file' output

* Mon Oct  6 2003 Joe Orton <jorton@redhat.com> 0.9.4-1
- update to 0.9.4.

* Tue Jul 22 2003 Nalin Dahyabhai <nalin@redhat.com> 0.9.3-10
- rebuild

* Mon Jul  7 2003 Joe Orton <jorton@redhat.com> 0.9.3-9
- rebuild
- don't run testuuid test because of #98677

* Thu Jul  3 2003 Joe Orton <jorton@redhat.com> 0.9.3-8
- rebuild

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue May 20 2003 Joe Orton <jorton@redhat.com> 0.9.3-6
- fix to detect crypt_r correctly (CAN-2003-0195)

* Thu May 15 2003 Joe Orton <jorton@redhat.com> 0.9.3-5
- fix to try linking against -ldb first (#90917)
- depend on openldap, gdbm, db4, expat appropriately.

* Tue May 13 2003 Joe Orton <jorton@redhat.com> 0.9.3-4
- rebuild

* Wed May  7 2003 Joe Orton <jorton@redhat.com> 0.9.3-3
- make devel package conflict with old subversion-devel
- run the less crufty parts of the test suite

* Tue Apr 29 2003 Joe Orton <jorton@redhat.com> 0.9.3-2
- run ldconfig in post/postun

* Mon Apr 28 2003 Joe Orton <jorton@redhat.com> 0.9.3-1
- initial build
