Name:       nodejs
Version:    0.6.11
Release:    1
Summary:    Evented I/O for V8 JavaScript
License:    BSD and MIT and ASL 2.0 and GPLv3
Group:      Development/Languages
URL:        http://nodejs.org/
Source0:    http://nodejs.org/dist/node-v%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# RPM macros for node.js library packages
Source1:    macros.nodejs

# fix the man page to reflect the moved binary
Patch2:     %{name}-man.patch

# force node to use /usr/lib/nodejs as the systemwide module directory
Patch4:     %{name}-libpath.patch

# use /usr/lib64/nodejs as an arch-specific module dir when appropriate
Patch5:     %{name}-lib64path.patch

# use proper include directory
Patch7:     %{name}-includedir.patch

# make waf import from correct directory
Patch8:     %{name}-wafimport.patch

# make modules build properly with WAF
Patch9:     %{name}-0.6.0-waf-modules.patch

BuildRequires:  python
BuildRequires:  dos2unix
BuildRequires:  v8-devel >= 3.6.6
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  python-markdown

# V8 sucks at sonames so we're explicit here
Conflicts:      chromium <= 14
Requires:       v8 >= 3.6.6.19

%description
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

%package devel
Summary:    Evented I/O for V8 JavaScript - development headers
Group:      Development/Libraries
Requires:   nodejs = %{version}-%{release}
Requires:   v8-devel%{?isa}

%description devel
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

This package contains the development headers, RPM macros, and a copy of the
built-in modules for nodejs.

%package doc
Summary:    Evented I/O for V8 JavaScript - documentation
Group:      Documentation
%if (0%{?rhel} >= 6 || 0%{?fedora})
BuildArch:  noarch
%endif

%description doc
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

This package contains the documentation for nodejs.

%package waf
Summary:   Evented I/O for V8 JavaScript - customized WAF build system
Group:     Development/Tools
Requires:  nodejs = %{version}-%{release}
%if (0%{?rhel} >= 6 || 0%{?fedora})
BuildArch:  noarch
%endif

%description waf
Node.js is a server-side JavaScript environment that uses an asynchronous
event-driven model.  Node's goal is to provide an easy way to build scalable
network programs.

This package contains the customized version of the WAF build system used by
Node.js and many of its modules.

%prep
%setup -q -n node-v%{version}
%patch7
%patch8
%patch9

%if %{_lib} == "lib64"
%patch5
%else
%patch4
%endif

%patch2
mv doc/node.1 doc/nodejs.1

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ;

# nodejs-v0.6.8 FTBFS without this
LINKFLAGS="-lz"; export LINKFLAGS ;

# NOT autoconf so dont use macro
./configure     \
        --prefix=%{_prefix}     \
        --shared-v8     \
        --shared-zlib

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

# gzip man page and put it where it belongs
gzip doc/nodejs.1
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/nodejs.1.gz %{buildroot}%{_mandir}/man1/
rm doc/nodejs.1.gz

# install documentation
mkdir -p %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/html
cp -pr doc/* %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}/html/
pushd %{buildroot}%{_datadir}/doc/%{name}-doc-%{version}
mkdir -p api
mv html/api/*.markdown api/
mv html/api/api/* html/api
rm -rf html/api/api
popd

# fix EOL encodings on a couple files in docs
dos2unix doc/sh_main.js

# don't conflict with node
pushd %{buildroot}
mv .%{_bindir}/node .%{_bindir}/nodejs
mv .%{_includedir}/node .%{_includedir}/nodejs
mv ./usr/lib/node ./usr/lib/nodejs
popd

# create library directories
mkdir -p %{buildroot}%{_libdir}/nodejs/.npm

%if %{_lib} == "lib64"
mkdir -p %{buildroot}%{_libdir}/../lib/nodejs/.npm
%endif

# install RPM macros
mkdir -p %{buildroot}%{_sysconfdir}/rpm/
install -pm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/

# link to library include files that are typically bundled
ln -s ../v8-debug.h %{buildroot}%{_includedir}/%{name}/
ln -s ../v8.h %{buildroot}%{_includedir}/%{name}/
ln -s ../v8-preparser.h %{buildroot}%{_includedir}/%{name}/
ln -s ../v8-profiler.h %{buildroot}%{_includedir}/%{name}/
ln -s ../v8stdint.h %{buildroot}%{_includedir}/%{name}/
ln -s ../v8-testing.h %{buildroot}%{_includedir}/%{name}/

# compile markdown README file
markdown README.md > README.html

# remove NPM; it's buggy in 0.6.3
rm -rf %{buildroot}%{_libdir}/../lib/node_modules
rm %{buildroot}%{_bindir}/npm

## disable tests, many require network and don't work on koji
#%%check
#cd build
#ctest

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/nodejs
%{_mandir}/man1/nodejs.1.gz
%doc AUTHORS ChangeLog LICENSE README.md README.html

%dir %{_libdir}/nodejs
%dir %{_libdir}/nodejs/.npm

%if %{_lib} == "lib64"
%dir %{_libdir}/../lib/nodejs
%dir %{_libdir}/../lib/nodejs/.npm
%endif

%files devel
%defattr(-,root,root,-)
%{_includedir}/nodejs/
%config %{_sysconfdir}/rpm/macros.nodejs
%doc lib

%files doc
%{_datadir}/doc/%{name}-doc-%{version}/

%files waf
%{_bindir}/node-waf
%{_libdir}/../lib/nodejs/wafadmin/

%changelog
* Sun Feb 26 2012 Santi Saez <santi@woop.es> - 0.6.11-1
- Upgrade to upstream node.js 0.6.11
- Allow multiple WebSocket and WWW-Authenticate headers

* Fri Jan 20 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.8-1
- new upstream release 0.6.8
- drop EL5 build patch; fixed upstream

* Sat Jan 08 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.7-2
- revert commit d5b26154 in libuv on EL5 because it breaks build

* Fri Jan 07 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.7-1
- new upstream release 0.6.7

* Fri Dec 16 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.6-2
- add Group to make EL5 rpmbuild happy
- -doc and -waf can't be noarch on EL5

* Thu Dec 15 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.6-1
- new upstream release 0.6.6

* Sun Dec 04 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.5-1
- new upstream release 0.6.5
- V8 requirement bumped to 3.6.6.11

* Sat Dec 03 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.4-1
- new upstream release 0.6.4

* Fri Nov 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.3-1
- new upstream release 0.6.3

* Fri Nov 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.2-1
- new upstream release 0.6.2
- fix install location of documentation

* Sun Nov 13 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.1-1
- new upstream release 0.6.1

* Mon Nov 07 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.6.0-1
- new upstream release 0.6.0
- switches to libuv, c-ares and libev are bundled in that *sighs*

* Sun Nov 06 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.12-6
- fix building on EL6

* Thu Oct 27 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.12-5
- fix building modules with WAF

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.12-4
- symlink to headers of libraries that are typically bundled
- fixes builds of some native modules
- -devel now Requires v8-devel and libev-devel
- fix Requires on -waf

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.12-3
- import WAF from the correct directory

* Mon Oct 24 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.12-2
- ship a node-waf package with Node.js' customized WAF build system

* Sun Sep 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.12-1
- new upstream release 0.4.12
- set include directory properly
- disable tests, many don't work on koji due to lack of network
- use bundled libs so it actually works (targeting external repo)
- revert to WAF

* Thu Aug 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.11-3
- use jsmin.py from v8-devel, not the bundled v8
- rm -rf the bundled libraries
- fix broken nodejs_fixshebang macro in macros.nodejs

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.11-2
- cp man page instead of mv
- man page doesn't get doc macro
- disable broken tests

* Fri Aug 19 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.11-1
- initial package
