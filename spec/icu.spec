Name:      icu
Version:   3.6
Release:   4
Summary:   International Components for Unicode
Group:     System Environment/Libraries
License:   MIT
URL:       http://www.ibm.com/software/globalization/icu/
Source0:   ftp://ftp.software.ibm.com/software/globalization/icu/3.6/icu4c-3_6-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  doxygen, autoconf

Patch1:  icu-3.4-multiarchdevel.patch
Patch2:  icu-config
Patch3:  icu.icu5365.dependantvowels.patch
Patch4:  icu.icu5418.malayam.patch
Patch5:  icu.icu5431.malayam.patch
Patch6:  icu.icu5433.oriya.patch
Patch7:  icu.icuXXXX.virama.prevnext.patch
Patch8:  icu.icu5465.telegu.patch
Patch9:  icu.icu5488.assamese.patch
Patch10: icu.icu5500.devicetablecrash.patch
Patch11: icu.icu5501.sinhala.biggerexpand.patch
Patch12: icu.icu5557.safety.patch
Patch13: icu.icu5506.multiplevowels.patch
Patch14: icu.icu5594.gujarati.patch
Patch15: icu.icuXXXX.malayalam.bysyllable.patch
Patch16: icu.regexp.patch

%description
The International Components for Unicode (ICU) libraries provide
robust and full-featured Unicode services on a wide variety of
platforms. ICU supports the most current version of the Unicode
standard, and they provide support for supplementary Unicode
characters (needed for GB 18030 repertoire support).
As computing environments become more heterogeneous, software
portability becomes more important. ICU lets you produce the same
results across all the various platforms you support, without
sacrificing performance. It offers great flexibility to extend and
customize the supplied services.

%package -n lib%{name}
Summary: International Components for Unicode - libraries
Group:   System Environment/Libraries

%description -n lib%{name}
%{summary}.

%package  -n lib%{name}-devel
Summary:  Development files for International Components for Unicode
Group:    Development/Libraries
Requires: lib%{name} = %{version}-%{release}
Requires: pkgconfig

%description -n lib%{name}-devel
%{summary}.

%package -n lib%{name}-doc
Summary: Documentation for International Components for Unicode
Group:   Documentation

%description -n lib%{name}-doc
%{summary}.

%prep
%setup -q -n %{name}
%patch1  -p1 -b .multiarchdevel
%patch3  -p1 -b .dependantvowels
%patch4  -p1 -b .icu5418.malayam.patch
%patch5  -p1 -b .icu5431.malayam.patch
%patch6  -p1 -b .icu5433.oriya.patch
%patch7  -p1 -b .icuXXXX.virama.prevnext.patch
%patch8  -p1 -b .icu5465.telegu.patch
%patch9  -p1 -b .icu5488.assamese.patch
%patch10 -p1 -b .icu5500.devicetablecrash.patch
%patch11 -p1 -b .icu5501.sinhala.biggerexpand.patch
%patch12 -p1 -b .icu5557.safety.patch
%patch13 -p1 -b .icu5506.multiplevowels.patch
%patch15 -p1 -b .icuXXXX.malayalam.bysyllable.patch
%patch16 -p1 -b .regexp.patch

%build
cd source
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
autoconf
%configure --with-data-packaging=library --disable-samples
make # %{?_smp_mflags} # -j(X>1) may "break" man pages as of 3.2, b.f.u #2357
make doc

%install
rm -rf $RPM_BUILD_ROOT source/__docs
make -C source install DESTDIR=$RPM_BUILD_ROOT
make -C source install-doc docdir=__docs
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*
cp -p %{PATCH2} $RPM_BUILD_ROOT%{_bindir}/%{name}-config
chmod a+x $RPM_BUILD_ROOT%{_bindir}/%{name}-config
sed -i s/\\\$\(THREADSCXXFLAGS\)// $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/icu.pc
sed -i s/\\\$\(THREADSCPPFLAGS\)/-D_REENTRANT/ $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/icu.pc

%check || :
make -C source check

%clean
rm -rf $RPM_BUILD_ROOT

%post -n lib%{name} -p /sbin/ldconfig

%postun -n lib%{name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc license.html readme.html
%{_bindir}/derb
%{_bindir}/genbrk
%{_bindir}/gencnval
%{_bindir}/genctd
%{_bindir}/genrb
%{_bindir}/makeconv
%{_bindir}/pkgdata
%{_bindir}/uconv
%{_sbindir}/*
%{_mandir}/man1/derb.1*
%{_mandir}/man1/gencnval.1*
%{_mandir}/man1/genrb.1*
%{_mandir}/man1/genbrk.1*
%{_mandir}/man1/genctd.1*
%{_mandir}/man1/makeconv.1*
%{_mandir}/man1/pkgdata.1*
%{_mandir}/man1/uconv.1*
%{_mandir}/man8/*.8*

%files -n lib%{name}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n lib%{name}-devel
%defattr(-,root,root,-)
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config.1*
%{_includedir}/layout
%{_includedir}/unicode
%{_libdir}/*.so
%{_libdir}/%{name}
%{_libdir}/pkgconfig/icu.pc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/3.6
%{_datadir}/%{name}/3.6/mkinstalldirs
%{_datadir}/%{name}/3.6/config
%doc %{_datadir}/%{name}/3.6/license.html

%files -n lib%{name}-doc
%defattr(-,root,root,-)
%doc source/__docs/%{name}/html/*

%changelog
* Sun Jan 26 2008 Thorsten Leemhuis <fedora AT leemhuis DOT info> - 3.6-4.20
- Sync with F7 3.6-20, but ship as 3.6-4.20 to have a proper updates path 
  EPEL4 (old icu) -> RHEL5 (is has icu-3.6-5.11 right now)

* Thu Jan 24 2008 Caolan McNamara <caolanm@redhat.com> - 3.6-20
- CVE-2007-4770 CVE-2007-4771 add icu.regexp.patch

* Mon Apr 30 2007 Caolan McNamara <caolanm@redhat.com> - 3.6-19
- Resolves: rhbz#220867 Malayalam rendering

* Tue Feb 13 2007 Caolan McNamara <caolanm@redhat.com> - 3.6-18
- Resolves: rhbz#228457 icu.icu5594.gujarati.patch

* Mon Feb 09 2007 Caolan McNamara <caolanm@redhat.com> - 3.6-17
- spec cleanups

* Mon Feb 05 2007 Caolan McNamara <caolanm@redhat.com> - 3.6-16
- Resolves: rhbz#226949 layout telegu like pango

* Fri Jan 19 2007 Caolan McNamara <caolanm@redhat.com> - 3.6-15
- Resolves: rhbz#214948 icu.icu5506.multiplevowels.patch

* Thu Jan 09 2007 Caolan McNamara <caolanm@redhat.com> - 3.6-14
- Related: rhbz#216089 add icu.icu5557.safety.patch

* Thu Dec 21 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-13
- Resolves: rhbz#220433 modify icu.icu5431.malayam.patch

* Fri Nov 10 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-12
- Resolves: rhbz#214948 icu.icu5506.multiplevowels.patch

* Wed Nov 08 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-11
- Resolves: rhbz#214555 icu.icu5501.sinhala.biggerexpand.patch

* Wed Nov 08 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-10
- Resolves: rhbz#214555 icu.icu5500.devicetablecrash.patch

* Thu Oct 18 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-9
- Resolves: rhbz#213648 extend prev/next to handle ZWJ

* Tue Oct 18 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-8
- Resolves: rhbz213375 (icu.icu5488.assamese.patch)

* Tue Oct 18 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-7
- Resolves: rhbz#211258 (icu.icu5465.telegu.patch)

* Thu Oct 05 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-6
- rh#209391# add icu.icuXXXX.virama.prevnext.patch

* Mon Oct 02 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-5
- rh#208705# add pkg-config Require for -devel package
- add icu.icu5431.malayam.patch for rh#208551#/rh#209084#
- add icu.icu5433.oriya.patch for rh#208559#/rh#209083#

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 3.6-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Mon Sep 25 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-3
- rh#206615# render malayam like pango

* Wed Sep 06 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-2
- fix rh#205252#/icu#5365 (gnome#121882#/#icu#4026#) to make icu 
  like pango for multiple dependant vowels

* Mon Sep 03 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-1
- final release

* Mon Aug 14 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-0.1.d02
- bump

* Tue Aug 08 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-0.2.d01
- c++ code not alias correct

* Mon Jul 31 2006 Caolan McNamara <caolanm@redhat.com> - 3.6-0.1.d01
- rh#200728# update to prelease 3.6d01 to pick up on sinhala fixes
- drop integrated rh190879.patch
- drop integrated icu-3.4-sinhala1.patch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.4-10.1.1
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.4-10.1
- rebuild

* Sat Jun 10 2006 Caolan McNamara <caolanm@redhat.com> - 3.4-10
- rh#194686# BuildRequires

* Tue May 09 2006 Caolan McNamara <caolanm@redhat.com> - 3.4-9
- rh#190879# backport fix

* Wed May 03 2006 Caolan McNamara <caolanm@redhat.com> - 3.4-8
- add Harshula's icu-3.4-sinhala1.patch for some Sinhala support

* Tue May 02 2006 Caolan McNamara <caolanm@redhat.com> - 3.4-7
- add a pkgconfig.pc, make icu-config use it

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 3.4-6.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.4-6.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 03 2006 Caolan McNamara <caolanm@redhat.com> - 3.4-6
- add icu-gcc41.patch

* Tue Oct 11 2005 Caolan McNamara <caolanm@redhat.com> - 3.4-5
- clear execstack requirement for libicudata

* Mon Sep 12 2005 Caolan McNamara <caolanm@redhat.com> - 3.4-4
- import extra icu.spec into fedora core for openoffice.org
- build with gcc 4

* Wed Aug 31 2005 Thorsten Leemhuis <fedora at leemhuis.info> - 3.4-3
- Use dist
- gcc32 does not understand -fstack-protector and 
  --param=ssp-buffer-size=4

* Tue Aug  2 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.4-2
- 3.4.

* Sun Jul 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.4-0.2.d02
- 3.4-d02.
- Don't ship static libraries.

* Wed Apr 27 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.2-3
- Apply upstream case mapping mutex lock removal patch.
- Build with gcc 3.2 as a temporary workaround for #152495.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 3.2-2
- rebuilt

* Sat Jan  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.2-1
- Don't use %%{_smp_mflags} (b.f.u #2357).
- Remove unnecessary Epochs.

* Sat Dec  4 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.2-0.fdr.1
- Update to 3.2.

* Sun Jul 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:3.0-0.fdr.1
- Update to 3.0, datadirs patch no longer needed.
- Package data in shared libs, drop -locales subpackage.
- Rename -docs subpackage to libicu-doc, and generate graphs with graphviz.

* Sat Dec 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.1-0.fdr.3
- Partial fix for bad datadirs returned by icu-config (works as long as
  data packaging mode is not "common" or "dll").

* Sun Nov 23 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.1-0.fdr.2
- First complete version.

* Sun Sep 28 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6.1-0.fdr.1
- Update to 2.6.1.

* Wed Aug 27 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6-0.fdr.1
- First build, based on upstream and SuSE 8.2 packages.
