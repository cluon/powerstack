Name:		powerstack-release       
Version:	0
Release:	2
Summary:	Run latest LAMP versions in your Enterprise Linux
Group:		System Environment/Base 
License:	GPLv2
URL:		http://powerstack.org/
Source0:	powerstack.repo	
Source1:	RPM-GPG-KEY-powerstack
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch


%description
This package contains the PowerStack repository configuration for Yum


%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .


%build


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-powerstack


%clean
rm -rf $RPM_BUILD_ROOT


%post


%postun 


%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/RPM-GPG-KEY-powerstack


%changelog
* Fri May 20 2011 Santi Saez <santi@woop.es> - 0-2
- PowerStack 0.2

* Wed Jan 19 2011 Santi Saez <santi@woop.es> - 0-1
- Initial package for PowerStack repository configuration for Yum
