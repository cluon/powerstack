Name:           powerstack-release       
Version:        0
Release:        1
Summary:        Run latest LAMP versions in your Enterprise Linux

Group:          System Environment/Base 
License:        GPLv2

URL:            http://powerstack.org/
Source0:        powersack.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch

%description
This package contains the PowerStack repository configuration for Yum

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun 

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*


%changelog
* Wed Jan 19 2011 Santi Saez <santi@woop.es> - 0-1
- Initial package for PowerStack repository configuration for Yum
