# - Based on php-extras from EPEL (http://download.fedora.redhat.com/pub/epel/5/SRPMS/repoview/php-extras.html)
# - Provides: mcrypt, mssql
# - Extensions moved to PECL: mhash, dbase
# - Disabled: interbase (requires firebird-devel, EPEL), tidy, recode and readline (available in PHP from RHEL-6)

%define def()	%%{!?_without_default:%%{!?_without_%1: %%global _with_%1 --with-%1}}

#%{expand:%def readline}
#  recode
%{expand:%def mcrypt}
#%{expand:%def mhash}
#%{expand:%def tidy}
%{expand:%def mssql}
#%{expand:%def interbase}


%define list	%{?_with_recode:recode} %{?_with_mcrypt:mcrypt} %{?_with_mssql:mssql pdo_dblib}

#%define opts	%{?_with_interbase:--with-interbase=%{_libdir}/firebird --with-pdo-firebird=%{_libdir}/firebird}

%global extdir	%(php-config --extension-dir 2>/dev/null || echo "undefined")
%global apiver	%((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)


Name: php-extras
Summary: Additional PHP modules from the standard PHP distribution
#Version: %(php-config --version 2>/dev/null || echo 0)
Version: 5.4.4
Release: 1
Group: Development/Languages
License: The PHP License
URL: http://www.php.net/
Source0: http://www.php.net/distributions/php-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: php-devel = %{version}
Patch1:  php-extras-5.1.2-readline.patch
Patch2:  php-extras-5.1.6-mssql.patch


%description
PHP is an HTML-embedded scripting language.

This package contains various additional modules for PHP, which
have not been included in the basic PHP package for Fedora Core.


%package -n php-readline
Summary: Standard PHP module provides readline library support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}
%{?_with_readline:BuildRequires: readline-devel}

%description -n php-readline
Standard PHP module provides readline library support


%package -n php-recode
Summary: Standard PHP module provides GNU recode support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}
%{?_with_recode:BuildRequires: recode-devel}

%description -n php-recode
Standard PHP module provides GNU recode support


%package -n php-mcrypt
Summary: Standard PHP module provides mcrypt library support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}
%{?_with_mcrypt:BuildRequires: libmcrypt-devel}

%description -n php-mcrypt
Standard PHP module provides mcrypt library support


%package -n php-mhash
Summary: Standard PHP module provides mhash support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}
%{?_with_mhash:BuildRequires: mhash-devel}

%description -n php-mhash
Standard PHP module provides mhash support


%package -n php-tidy
Summary: Standard PHP module provides tidy library support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}
%{?_with_tidy:BuildRequires: libtidy-devel}

%description -n php-tidy
Standard PHP module provides tidy library support


%package -n php-mssql
Summary: Standard PHP module provides mssql support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}, php-pdo >= %{version}
Provides: php_database
%{?_with_mssql:BuildRequires: freetds-devel}

%description -n php-mssql
Standard PHP module provides mssql support


%package -n php-interbase
Summary: Standard PHP module provides interbase/firebird support
Group: Development/Languages
Requires: php >= %{version}, php-api = %{apiver}, php-pdo >= %{version}
Provides: php_database, php-firebird
#%{?_with_interbase:BuildRequires: firebird-devel}

%description -n php-interbase
Standard PHP module provides interbase/firebird support


%prep
%setup -q -n php-%{version}
#%patch1 -p1
#%patch2 -p1

# avoid tests which requires databases
rm -rf ext/{mssql,pdo_dblib,interbase,pdo_firebird,readline,mcrypt}/tests


%build

%if 0%{?rhel} >= 5
	CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-pointer-sign"
%else
	CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%endif
export CFLAGS

for mod in %{list}
do
    pushd ext/$mod

    phpize
    %configure --with-libdir=%{_lib} %{opts}

    # cause libtool to avoid passing -rpath when linking
    # (this hack is well-known as "libtool rpath workaround")
    sed -i 's|^hardcode_libdir_flag_spec|hardcode_libdir_flag_spec=" -D__LIBTOOL_IS_A_FOOL__ "|' libtool

    make %{?_smp_mflags}

    popd
done


%check

#
# As we don't build whole php here, we must do all the tests
# with the system php executable. Unfortunately, we cannot use
# system's /usr/bin/php directly, therefore a wrapper is needed.
# 
# Some reasons for such a wrapper are:
# - /usr/bin/php cannot handle "-d extension=" etc. on the command line
#   (probably because of the CGI-oriented variant of php executable is
#   installed as /usr/bin/php). We should use own config file for this.
# - During "run-tests.php" execution, php is invoked again (recursively).
#   (i.e. we cannot explicitly set another config for deeper php invokation).
# - We cannot exclude /etc/php.d/* files on the host machine. It can lead to
#   some stderr reports, which spoil the tests' output. To omit extra warnings,
#   the stderr is redirected to /dev/null
# - When invoked again, some CGI-related environment variables are set 
#   by default, which confuse php a lot. Therefore the environment is cleared,
#   and only needed variables are provided.
# 
# The test stuff is derived from the original tests in the php tarball,
# with preserving some needed specifications etc.
#
  

mkdir modules || exit 1

cat >modules.ini <<EOF
open_basedir=
safe_mode=0
output_buffering=0
extension_dir=$PWD/modules
EOF

for mod in %{list}
do
    cp -a ext/$mod/modules/${mod}.so modules
    echo "extension=${mod}.so" >>modules.ini
done

cat >php <<EOF
#!/bin/sh
exec 2>/dev/null
env -i TEST_PHP_EXECUTABLE=$PWD/php TEST_PHP_SRCDIR=\$TEST_PHP_SRCDIR \
	NO_INTERACTION=1 REPORT_EXIT_STATUS=1 MALLOC_CHECK_=2 \
	%{_bindir}/php -c $PWD/modules.ini "\$@"
EOF
chmod +x ./php


for mod in %{list}
do
    [ -d ext/$mod/tests ] || continue

    pushd ext/$mod

    TEST_PHP_SRCDIR=$PWD ../../php ../../run-tests.php tests

    set +x
    fail=0
    for f in tests/*.diff
    do
	[ -f "$f" ] || continue
	echo "TEST FAILURE: $PWD/$f --"
	cat $f
	echo
	echo "-- $PWD/$f result ends."
	fail=1
    done
    [ $fail -ne 0 ] && exit $fail
    
    popd
done


%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{extdir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/php.d

for mod in %{list}
do
    install -m755 ext/${mod}/modules/*.so $RPM_BUILD_ROOT%{extdir}

    cat > $RPM_BUILD_ROOT%{_sysconfdir}/php.d/${mod}.ini <<EOF
; Enable ${mod} extension module
extension=${mod}.so
EOF
    cat > files.${mod} <<EOF
%defattr(-,root,root)
%{extdir}/${mod}.so
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/php.d/${mod}.ini
EOF
done

%{?_with_mssql:cat files.pdo_dblib >>files.mssql}
#%{?_with_interbase:cat files.pdo_firebird >>files.interbase}


%clean
rm -rf $RPM_BUILD_ROOT


#%%files
%define fil()	%%{?_with_%1:%%files -n php-%1 -f files.%1}
%{expand:%fil dbase}
#%{expand:%fil readline}
%{expand:%fil recode}
%{expand:%fil mcrypt}
#%{expand:%fil mhash}
#%{expand:%fil tidy}
%{expand:%fil mssql}
#%{expand:%fil interbase}



%changelog
* Thu Jun 14 2012 Santi Saez <santi@woop.es> - 5.4.4-1
- Upgrade to upstream PHP 5.4.4, issue #25 on GitHub (http://kcy.me/96ls)
- CVE-2012-2143 fix: a weakness in the DES implementation of crypt
- Heap overflow issue in the phar extension
- php://fd streams is now restricted to the CLI SAPI

* Sun Jun 10 2012 Santi Saez <santi@woop.es> - 5.4.3-1
- Upgrade to upstream PHP 5.4.3
- CVE-2012-2311 fix
- CVE-2012-2329 fix

* Sat Mar 17 2012 Santi Saez <santi@woop.es> - 5.4.0-2
- php.spec + php-extras.spec merge still pending, release upgrade

* Thu Mar 10 2012 Santi Saez <santi@woop.es> - 5.4.0-1
- Upgrade to upstream PHP 5.4.0

* Sat Feb  4 2012 Santi Saez <santi@woop.es> - 5.3.10-1
- Upgrade to upstream PHP 5.3.10
- CVE-2012-0830, critical security fix: arbitrary remote code execution

* Thu Jan 12 2012 Santi Saez <santi@woop.es> - 5.3.9-1
- Upgrade to upstream PHP 5.3.9
- CVE-2011-4885 fix (max_input_vars to prevent hash collisions based attacks)
- CVE-2011-4566 (integer overflow during the parsing of invalid exif header)

* Fri Sep 9 2011 Santi Saez <santi@woop.es> - 5.3.8-1
- Update to PHP 5.3.8

* Mon May 16 2011 Santi Saez <santi@woop.es> - 5.3.6-2 
- Update to build against MySQL 5.5.12

* Mon Mar 28 2011 Santi Saez <santi@woop.es> - 5.3.6-1
- Update to PHP 5.3.6

* Tue May 12 2009 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.6-5
- add pdo_dblib module for php-mssql
- add php-interbase support (both interbase and pdo_firebird modules)
  (initial patch from Remi Collet <fedora@famillecollet.com>)

* Wed Jun 20 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.6-4
- add patch for mssql (#244736), a backport of some php-5.2 changes

* Fri Jun 15 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.6-3
- add --with-libdir=%%{_lib} to handle 64bit arches properly

* Thu Jun 14 2007 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.6-2
- add php-mssql support

* Fri Sep  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.6-1
- update to 5.1.6

* Thu Jun 22 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.4-2
- auto-detect extdir and apiver again (needed for x86_64)

* Fri Jun 16 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.4-1
- update to upstream php 5.1.4
- an easier way to auto-detect php-api version
- specify extdir and apiver explicitly, because FE build system
  is not able to auto-detect it now.

* Fri Mar 31 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.2-3
- ppc arch hack: change dir before %%apiver auto-detecting

* Sat Mar 25 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.2-2
- Accepted for Fedora Extras
  (review by Tom "spot" Callaway <tcallawa@redhat.com>)
 
* Wed Mar  1 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.2-2
- more accurate Requires for the main php
  (using php-api, provided now by the Core php package).

* Tue Feb 28 2006 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.2-1
- update to 5.1.2
- replace readline patch (old issue go away and a new appears).
- apply well-known "libtool-rpath-workaround" (see in Internet ;-))
  to avoid use -rpath for linking

* Sat Dec 17 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.1.1-1
- upgrade to 5.1.1 for FC5
- drop now missed "fam" and obsolete "sqlite" (sqlite2) modules

* Mon Nov 14 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.0.4-1
- spec file cleanups

* Mon Oct 10 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 5.0.4-0
- adaptation for php5
- drop tests patch (no more needed).

* Fri Oct  7 2005 Dmitry Butskoy <Dmitry@Butskoy.name> - 4.3.11-0
- initial release
- create test stuff for check section. A lot of work because we play
  with extra modules by our own way...
- add patch to fix some pathes in tests
- add patch for readline configure

