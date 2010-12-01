Summary: PHP extension that is used to run code that was encoded or obfuscated using Zend Guard
Name: php-zendguard
Version: 3.3
Release: 1
Group: Development/Languages
License: Zend
URL: http://www.zend.com/en/products/guard/

%ifarch %ix86
Source0: http://downloads.zend.com/guard/5.5.0/ZendGuardLoader-php-5.3-linux-glibc23-i386.tar.gz
%endif

%ifarch x86_64
Source0: http://downloads.zend.com/guard/5.5.0/ZendGuardLoader-php-5.3-linux-glibc23-x86_64.tar.gz
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

Requires: php >= 5.3

%description
PHP extension that is used to run code that was encoded or obfuscated using Zend Guard (replaces Zend Optimizer)
%prep
%setup -c -q
%build

%install
mkdir -p %{buildroot}/usr/lib/php/modules

%ifarch %ix86
cp ZendGuardLoader-php-5.3-linux-glibc23-i386/php-5.3.x/ZendGuardLoader.so %{buildroot}/usr/lib/php/modules/zendguard.so
%endif

%ifarch x86_64
cp ZendGuardLoader-php-5.3-linux-glibc23-x86_64/php-5.3.x/ZendGuardLoader.so %{buildroot}/usr/lib/php/modules/zendguard.so
%endif

mkdir -p %{buildroot}/etc/php.d

cat > %{buildroot}/etc/php.d/zendguard.ini << 'EOF'
; NOTE: If you use ionCube loader load it **BEFORE** Zend Guard Loader

; Enable Zend Guard Loader extension module for PHP
zend_extension=/usr/lib/php/modules/zendguard.so

; Disable license checks (for performance reasons)
zend_loader.disable_licensing=0

; The Obfuscation level supported by Zend Guard Loader
;zend_loader.obfuscation_level_support=3

; Path to where licensed Zend products should look for the product license
zend_loader.license_path=
EOF

%files
%defattr(0755,root,root)
/usr/lib/php/modules/zendguard.so

%defattr(0644,root,root)
/etc/php.d/zendguard.ini
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
