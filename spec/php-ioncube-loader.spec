Summary: Extension used to handle encoded files with ionCube Encoder
Name: php-ioncube-loader
Version: 4.0.7
Release: 1
Group: Development/Languages
License: ionCube Ltd.
URL: http://www.ioncube.com/loaders.php

%ifarch %ix86
Source0: http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.bz2
Source1: http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.bz2
%endif

%ifarch x86_64
Source1: http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.bz2
Source0: http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.bz2
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: php >= 5.3

%description
PHP extension used to handle encoded files at runtime with ionCube Encoder

%prep
%setup -c -q
%build

%install
mkdir -p %{buildroot}/usr/lib/php/modules

%ifarch %ix86
cp ioncube/ioncube_loader_lin_5.3.so %{buildroot}/usr/lib/php/modules/ioncube-loader.so
%endif

%ifarch x86_64
cp ioncube/ioncube_loader_lin_5.3.so %{buildroot}/usr/lib/php/modules/ioncube-loader.so
%endif

mkdir -p %{buildroot}/etc/php.d

cat > %{buildroot}/etc/php.d/ioncube-loader.ini << 'EOF'
; NOTE: If you use ionCube loader load it **BEFORE** Zend Guard Loader

; Enable ionCube Loader module for PHP
zend_extension=/usr/lib/php/modules/ioncube-loader.so
EOF

%files
%defattr(0755,root,root)
/usr/lib/php/modules/ioncube-loader.so

%defattr(0644,root,root)
/etc/php.d/ioncube-loader.ini

%post

function webserver() {
	ACTION=$1

	case $ACTION in
		restart)
			if [ ! -e /etc/powerstack/php.disable_webserver_restart ] ; then
				if `/bin/rpm -q --quiet httpd` ; then
					if `/usr/bin/pgrep -n httpd > /dev/null` ; then
						echo -en 'Restarting Apache gracefully: '
						/etc/init.d/httpd configtest && /etc/init.d/httpd graceful
					fi
				fi
			fi
			;;
	esac
}

webserver restart
