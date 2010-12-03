Name: pcre
Version: 6.6
Release: 2
Summary: Perl-compatible regular expression library
URL: http://www.pcre.org/
Source: ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/%{name}-%{version}.tar.bz2
Patch1: pcre-6.6-multilib.patch
Patch2: pcre-6.6-CVE-2007-1659.patch
Patch3: pcre-6.6-CVE-2007-1660.patch
Patch4: pcre-6.6-CVE-2006-7224.patch
Patch5: pcre-6.6-CVE-2006-7225.patch
Patch6: pcre-6.6-CVE-2006-7226.patch
Patch7: pcre-6.6-CVE-2006-7230.patch
License: BSD
Group: System Environment/Libraries
Prefix: %{_prefix}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prereq: /sbin/ldconfig
BuildPrereq: sed

%description
Perl-compatible regular expression library.
PCRE has its own native API, but a set of "wrapper" functions that are based on
the POSIX API are also supplied in the library libpcreposix. Note that this
just provides a POSIX calling interface to PCRE: the regular expressions
themselves still follow Perl syntax and semantics. The header file
for the POSIX-style functions is called pcreposix.h.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files (Headers, libraries for static linking, etc) for %{name}.

%prep
%setup -q
%patch1 -p1 -b .multilib
%patch2 -p1 -b .CVE-2007-1659
%patch3 -p1 -b .CVE-2007-1660
%patch4 -p1 -b .CVE-2006-7224
%patch5 -p1 -b .CVE-2006-7225
%patch6 -p1 -b .CVE-2006-7226
%patch7 -p1 -b .CVE-2006-7230

%build
%configure --enable-utf8

make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/libpcre.so.* %{buildroot}/%{_lib}/
pushd %{buildroot}%{_libdir}
ln -fs ../../%{_lib}/libpcre.so.0 libpcre.so
popd

# get rid of unneeded *.la files
rm -f %{buildroot}%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/%{_lib}/*.so.*
%{_libdir}/*.so.*
%{_mandir}/man1/*
%{_bindir}/pcregrep
%{_bindir}/pcretest
%doc LICENCE AUTHORS

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*
%{_includedir}/*.h
%{_mandir}/man3/*
%{_bindir}/pcre-config

%changelog
* Mon Nov 19 2007 Stepan Kasal <skasal@redhat.com> - 6.6-2.7
- Fix the names of the pacthes added in 6.6-2.5:
  mv pcre-6.4-posix.diff pcre-6.6-CVE-2006-7225.patch
  mv pcre-6.4-fix1.patch pcre-6.6-CVE-2006-7226.patch
- Update pcre-6.6-CVE-2007-1659.patch
- Update pcre-6.6-CVE-2007-1660.patch
- Add pcre-6.6-CVE-2006-7230.patch
- Resolves: #380531

* Tue Nov 13 2007 Stepan Kasal <skasal@redhat.com> - 6.6-2.6
- Fix a typo in this changelog.
- Related: #373441

* Tue Nov 13 2007 Stepan Kasal <skasal@redhat.com> - 6.6-2.5
- Improve the fix for CVE-2006-7224 by updating
  pcre-6.6-CVE-2006-7224.patch and adding pcre-6.4-fix1.patch
  and pcre-6.4-posix.diff
- Related: #373441

* Fri Nov 09 2007 Josh Bressers <bressers@redhat.com> - 6.6-2.el5_1.1
- Resolves: #373441, CVE-2006-7224

* Thu Oct 11 2007 Than Ngo <than@redhat.com> - 6.6-2.1
- Resolves: #315951, CVE-2007-1659, CVE-2007-1660

* Thu Oct 11 2007 Than Ngo <than@redhat.com> - 6.6-1.2
- Resolves: #315951, CVE-2007-1659, CVE-2007-1660

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.6-1.1
- rebuild

* Tue May 09 2006 Than Ngo <than@redhat.com> 6.6-1
- update to 6.6
- fix multilib problem

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6.3-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6.3-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Aug 24 2005 Than Ngo <than@redhat.com> 6.3-1
- update to 6.3

* Fri Mar  4 2005 Joe Orton <jorton@redhat.com> 5.0-4
- rebuild

* Fri Feb 11 2005 Joe Orton <jorton@redhat.com> 5.0-3
- don't print $libdir in 'pcre-config --libs' output

* Thu Nov 18 2004 Joe Orton <jorton@redhat.com> 5.0-2
- include LICENCE, AUTHORS in docdir
- run make check
- move %%configure to %%build

* Thu Nov 18 2004 Than Ngo <than@redhat.com> 5.0-1
- update to 5.0
- change License: BSD
- fix header location #64248

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 23 2004 Than Ngo <than@redhat.com> 4.5-2
- add the correct pcre license, #118781

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 4.5-1
- update to 4.5

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Sep 26 2003 Harald Hoyer <harald@redhat.de> 4.4-1
- 4.4

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  7 2003 Than Ngo <than@redhat.com> 4.2-1
- update to 4.2

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Than Ngo <than@redhat.com> 3.9-9
- build with utf8, bug #81504

* Fri Nov 22 2002 Elliot Lee <sopwith@redhat.com> 3.9-8
- Really remove .la files

* Fri Oct 11 2002 Than Ngo <than@redhat.com> 3.9-7
- remove .la

* Thu Oct 10 2002 Than Ngo <than@redhat.com> 3.9-7
- Typo bug

* Wed Oct  9 2002 Than Ngo <than@redhat.com> 3.9-6
- Added missing so symlink

* Thu Sep 19 2002 Than Ngo <than@redhat.com> 3.9-5.1
- Fixed to build s390/s390x/x86_64

* Wed Jun 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.9-5
- Fix #65009

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Mar  4 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.9-2
- rebuild

* Fri Jan 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.9-1
- Update to 3.9

* Wed Nov 14 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.7-1
- Update to 3.7

* Thu May 17 2001 Bernhard Rosenkraenzer <bero@redhat.com> 3.4-2
- Move libpcre to /lib, grep uses it these days (#41104)

* Wed Apr 18 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Move this to a separate package, used to be in kdesupport, but it's
  generally useful...
