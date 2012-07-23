[PowerStack](http://powerstack.org) is a Yum repository for CentOS with aditional packages, focused on enterprise-grade Linux.



### Installing PowerStack

In order tu use PowerStack repository you must install "powerstack-release" package, that's it! Now you can upgrade PHP, MySQL, Apache, etc. to latest stable versions or install extra packages not available on CentOS base repository.

Update

    rpm -Uvh http://download.powerstack.org/powerstack-release-0-2.noarch.rpm
    yum update

Install new packages with Yum, for example:

    yum install nginx



### Features

* Latest versions for LAMP stack (PHP 5.4, MySQL 5.5 and Apache 2.2)
* [+100 extra packages](http://wiki.powerstack.org/Packages)
* Compatible with EPEL
