Name:           maatkit
Version:        7540
Release:        1
Summary:        Essential command-line utilities for MySQL

Group:          Applications/Databases
License:        GPLv2 or Artistic
URL:            http://www.maatkit.org/
Source0:        http://maatkit.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(DBD::mysql) >= 1.0
Requires:       perl(Term::ReadKey) >= 2.10

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This toolkit contains essential command-line utilities for MySQL, such as a 
table checksum tool and query profiler. It provides missing features such as 
checking slaves for data consistency, with emphasis on quality and 
scriptability.


%prep
%setup -q


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor < /dev/null
make %{?_smp_mflags}


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%files
%defattr(-,root,root,-)
%doc COPYING INSTALL Changelog*
%{_bindir}/*
%{_mandir}/man1/*.1*
%{perl_vendorlib}/%{name}.pod


%changelog
* Fri Jul 22 2011 Santi Saez <santi@woop.es> - 7540-1
- Backport from EPEL-5 and updated to 7540 release

* Sun Mar 13  2011 Sven Lankes <sven@lank.es> - 7332-1
- new upstream release
- remove buildroot tags from spec
- Filter out requires brought in by new rpm dependency generator

* Sun Feb 13  2011 Sven Lankes <sven@lank.es> - 7284-1
- new upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6839-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 29 2010 Sven Lankes <sven@lank.es> - 6839-1
- new upstream release

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 5899-2
- Mass rebuild with perl-5.12.0

* Sun Mar 28 2010 Sven Lankes <sven@lank.es> - 5899-1
- new upstream release

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 5014-2
- rebuild against perl 5.10.1

* Sat Nov 14 2009 Sven Lankes <sven@lank.es> - 5014-1
- new upstream release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2725-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2725-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 4 2009 Sven Lankes <sven@lank.es> - 2725-1
- new upstream release 

* Thu Dec 25 2008 Lubomir Rintel <lkundrak@v3.sk> - 2582-3
- Really fix the DBD dependency...

* Wed Dec 24 2008 Lubomir Rintel <lkundrak@v3.sk> - 2582-2
- Fix DBD driver dependency

* Tue Dec 23 2008 Lubomir Rintel <lkundrak@v3.sk> - 2582-1
- Bump release
- Fix BRs

* Sun Jul 13 2008 Lubomir Rintel <lkundrak@v3.sk> - 1972-2
- Cleanup for inclusion in Fedora

* Tue Jun 12 2007 Sven Edge <sven@curverider.co.uk> - 547-1
- initial packaging attempt
