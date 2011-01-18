Summary: Thread-safe hash algorithms library
Name: mhash
Version: 0.9.2
Release: 3
Epoch: 0
URL: http://mhash.sourceforge.net/
License: LGPL
Group: System Environment/Libraries
Source: http://download.sourceforge.net/mhash/mhash-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot-%(%{__id_u} -n)
Provides: libmhash = %{epoch}:%{version}-%{release}

%description
Mhash is a free library which provides a uniform interface to a
large number of hash algorithms. 

These algorithms can be used to compute checksums, message digests,
and other signatures. The HMAC support implements the basics for
message authentication, following RFC 2104. In the later versions
some key generation algorithms, which use hash algorithms, have been
added. Currently, the library supports the algorithms: SHA1, GOST,
HAVAL256, HAVAL224, HAVAL192, HAVAL160, HAVAL128, MD5, MD4, MD2,
RIPEMD128/160/256/320, TIGER, TIGER160, TIGER128, SHA224/384/512,
Whirlpool, SNEFRU128/256, CRC32B and CRC32 checksums.


%package -n %{name}-devel
Summary: Header files and libraries for developing apps which use mhash
Group: Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: libmhash-devel = %{epoch}:%{version}-%{release}

%description -n %{name}-devel
This package contains the header files and libraries needed to
develop programs that use the mhash library.


%prep
%setup -q


%build
%configure --enable-shared --enable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


%post -n %{name} -p /sbin/ldconfig


%postun -n %{name} -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files -n %{name}
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_libdir}/*.so.*


%files -n %{name}-devel
%defattr(-,root,root,-)
%doc ChangeLog ./doc/*.txt ./doc/*.c ./doc/skid2-authentication
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la
%{_mandir}/man3/*


%changelog
* Tue Jul 24 2007 Jon Ciesla <limb@jcomserv.net> - 0:0.9.2-2
- Added disttag for epel.

* Wed Jan 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.2-1
- Update to 0.9.2.

* Sun Apr 18 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.9.1-0.fdr.1
- Update to 0.9.1.
- Add EVR to virtual provides.
- Move some doc files into the main package.

* Tue Aug 12 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.8.18-0.fdr.1
- Initial package.

