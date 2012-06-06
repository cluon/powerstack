#%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global upstream_name redis

Name:		python-redis
Version:	2.4.13
Release:	1
Summary:	A Python client/interface for Redis key-value store

Group:		Development/Languages
License:	MIT
URL:		http://github.com/andymccurdy/redis-py
Source0:	http://github.com/downloads/andymccurdy/redis-py/%{upstream_name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
BuildRequires:	python-devel

%description
This is a Python client/interface for Redis key-value store

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE README.md
%{python_sitelib}/%{upstream_name}
/usr/lib/python2.6/site-packages/%{upstream_name}-%{version}-py2.6.egg-info

%changelog
* Wed Jun  6 2012 Santi Saez <santi@woop.es> - 2.4.13-1
- First release of redis-py based on EPEL-6 .spec, upgraded to upstream 2.4.13
