# $Id: smeserver-zabbix-server.spec,v 1.20 2022/12/11 07:12:36 jpp Exp $
# Authority: vip-ire
# Name: Daniel Berteaud

%define name smeserver-zabbix-server
%define version 0.1
%define release 34
Summary: sme server integration of zabbix server and web front-end
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://www.zabbix.com/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.xz


BuildArchitectures: noarch
BuildRequires: smeserver-devtools
BuildRoot: /var/tmp/%{name}-%{version}
Requires: smeserver-release >= 11
Requires: smeserver-apache >= 11
Requires: smeserver-php >= 11
Requires: fping
Requires: zabbix-server-mysql >= 7.0.1
Requires: zabbix-sql-scripts
# this will force pulling it from zabbix repo not from EPEL
Requires: /usr/share/doc/zabbix-web/AUTHORS
Requires: /usr/share/doc/zabbix-web/COPYING
Conflicts:  zabbix7.0 zabbix7.0-dbfiles-mysql zabbix7.0-selinux zabbix7.0-server zabbix7.0-server-mysql zabbix7.0-web zabbix7.0-web-mysql
Conflicts:  zabbix8.0 zabbix8.0-dbfiles-mysql zabbix8.0-selinux zabbix8.0-server zabbix8.0-server-mysql zabbix8.0-web zabbix8.0-web-mysql
Requires: zabbix-web-mysql >= 7.0.1
Requires: zabbix-web >= 7.0.1
Requires: sendxmpp
Requires: smeserver-remoteuseraccess
# for telegram bot
Requires: python2-pysocks python2-requests 
#python2-requests-oauthlib
Requires: python3-pysocks python3-requests python3-requests-oauthlib
Obsoletes: zabbix-server
Conflicts: smeserver-zabbix-proxy
AutoReqProv: no

%description
smserver integration of zabbix server and web front-end.
Zabbix is an entreprise-class open source distributed monitoring
solution

%changelog
* Thu May 28 2026 Jean-Philippe Pialasse <jpp@koozali.org> 0.1-34.sme
- import to SME11
- use php 8.4, fix php-fpm, mariadb 11.4
- set headers including CSP and referer

* Sun Sep 08 2024 fix-e-smith-pkg.sh by Trevor Batley <trevor@batley.id.au> 0.1-33.sme
- Fix e-smith references in smeserver-zabbix-server [SME: 12732]

* Sat Sep 07 2024 cvs2git.sh aka Brian Read <brianr@koozali.org> 0.1-32.sme
- Roll up patches and move to git repo [SME: 12338]

* Sat Sep 07 2024 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.

* Sat Dec 10 2022 Jean-Philippe Pialasse <tests@pialasse.com> 0.1-31.sme
- original package build for Zabbix 5.0 using Remi SCLO [SME: 11748]
  support for LTS 5.0 EOL May 31, 2025
  needs mariadb105. 
  manual migration from mariadb55 to mariadb105 needed for existing installs

* Mon Aug 01 2022 Jean-Philippe Pialasse <tests@pialasse.com> 0.1-30.sme
- update to httpd 2.4 access syntax [SME: 12068]
  thanks to Vasarhelyi Zsolt
- add to core backup [SME: 12031]
  non rpm owned files in /etc/zabbix, /etc/zabbix/zabbix_agentd.conf.d/
  and /var/lib/zabbix/bin/

* Tue Nov 09 2021 Jean-Philippe Pialasse <tests@pialasse.com> 0.1-29.sme
- set random password to Admin i fuser exists and password is zabbix [SME: 11749]

* Mon Nov 08 2021 Jean-Philippe Pialasse <tests@pialasse.com> 0.1-28.sme
- add check cert scripts and telegram [SME: 10802]
  no template provided to use with

* Sun Nov 07 2021 Jean-Philippe Pialasse <tests@pialasse.com> 0.1-27.sme
- fix init sql, typo and reload deamon [SME: 11232]

* Sun Nov 07 2021 Jean-Philippe Pialasse <tests@pialasse.com> 0.1-26.sme
- fix session and log issue [SME: 11232]
  fix mysql-init not launched

* Mon Nov 01 2021 BogusDateBot
- Eliminated rpmbuild "bogus date" warnings due to inconsistent weekday,
  by assuming the date is correct and changing the weekday.
  Tue Mar 02 2009 --> Tue Feb 24 2009 or Mon Mar 02 2009 or Tue Mar 03 2009 or ....
  Wed Feb 07 2016 --> Wed Feb 03 2016 or Sun Feb 07 2016 or Wed Feb 10 2016 or ....

* Mon Nov 01 2021 Brian Read <brianr@bjsystems.co.uk> 0.1-25.sme
- Switch-to-specific-php-fpm [SME: 11232]

* Mon Nov 01 2021 Brian Read <brianr@bjsystems.co.uk> 0.1-24.sme
- Remove post and postun command in spec file [SME: 11232]

* Thu Dec 10 2020 Brian Read <brianr@bjsystems.co.uk> 0.1-23.sme
- Add in post instructions to spec for SQL db creation [SME: 11232]

* Tue Dec 08 2020 Brian Read <brianr@bjsystems.co.uk> 0.1-22.sme
- Add expand zabbix-server.conf and .user.ini to creatlinks update event [SME:11232]

* Tue Dec 08 2020 Brian Read <brianr@bjsystems.co.uk> 0.1-21.sme
- Template-user-dot-ini-and-override-service-file-change-pid-in-conf-file [SME: 11232]

* Mon Dec 07 2020 Brian Read <brianr@bjsystems.co.uk> 0.1-20.sme
- Import to SME10 tree [SME: 11232]
- Update createlinks for systemd
- Update httpd.conf for php-fpw
- Add .user.ini for php-admin-flags that where in httpd.conf

* Sun May 10 2020 Jean-Philipe Pialasse <tests@pialasse.com> 0.1-19.sme
- adapt for zabbix 4.4.6 [SME: 10944]

* Thu Sep 05 2019 Jean-Philipe Pialasse <tests@pialasse.com> 0.1-17.sme
- remove deprecated option preventing from starting service [SME: 10458]

* Wed Mar 29 2017 Jean-Philipe Pialasse <tests@pialasse.com> 0.1-16.sme
- fix sql init not finding default sql dump to import [SME: 9569]
- NodeID support droped as per zabbix 2.4.0 and higher
- requires smeserver-php-scl as Zabbix-server 3.2.4 requires php 5.4 or higher

* Mon Jun 13 2016 Jean-Philipe Pialasse <tests@pialasse.com> 0.1-15.sme
- finitial import [SME: 9569]
- fix php requirement
- fix add path to new db

* Sun Feb 07 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1-14.sme
  Wed Feb 07 2016 --> Wed Feb 03 2016 or Sun Feb 07 2016 or Wed Feb 10 2016 or ....
- New roll for sme9

* Mon Apr 29 2013 Daniel B. <daniel@firewall-services.com> 0.1-13
- Increase PHP mem limit to 128M

* Mon Mar 8 2010 Daniel B. <daniel@firewall-services.com> 0.1-12
- Use global TimeZone

* Wed Dec 2 2009 Daniel B. <daniel@firewall-services.com> 0.1-11
- Support several mysql DB patches

* Tue Mar 03 2009 Daniel B. <daniel@firewall-services.com> 0.1-10
- Add smeserver-remoteuseraccess as a dependencie (sudoers template problem)

* Mon Mar 02 2009 Daniel B. <daniel@firewall-services.com> 0.1-9
- specify path to .sendxmpprc file in the script sendxmpp

* Mon Mar 02 2009 Daniel B. <daniel@firewall-services.com> 0.1-8
- move .sendxmpprc template to the correct directory

* Mon Mar 02 2009 Daniel B. <daniel@firewall-services.com> 0.1-7
- Move jabber account informations to xmpprc

* Mon Mar 02 2009 Daniel B. <daniel@firewall-services.com> 0.1-6
- Adjust service masq during zabbix-server-update event
- Enable DB cache module with StartDBSyncers directive

* Sun Mar 01 2009 Daniel B. <daniel@firewall-services.com> 0.1-5
- Fix permissions on /var/lib/zabbix/tmp

* Tue Feb 17 2009 Daniel B. <daniel@firewall-services.com> 0.1-4
- rename event zabbix-update to zabbix-server-update

* Wed Feb 11 2009 Daniel B. <daniel@firewall-services.com> 0.1-3
- disable web access (usefull for distributed monitoring)
- Use stronger password for mysql database
- Use /var/lib/zabbix/bin as default location for scripts
- Use /var/lib/zabbix/tmp for temp dir

* Fri Feb 06 2009 Daniel B. <daniel@firewall-services.com> 0.1-2
- Link template-begin-shell to template-begin for sendxmpp script

* Fri Feb 06 2009 Daniel B. <daniel@firewall-services.com> 0.1-1
- templatize sendxmpp as zabbix user doesn't have access to SME db
- Add JabberTLS option in the db

* Mon Feb 02 2009 Daniel B. <daniel@firewall-services.com> 0.1-0
- initial release

%prep
%setup

%build
perl ./createlinks
%{__mkdir_p} root/var/lib/zabbix/tmp
#%{__mkdir_p} root/var/log/zabbix - conflict with zabbix-server-mysql
%{__mkdir_p} root/var/log/php/zabbix
%{__mkdir_p} root/var/lib/php/zabbix/{tmp,wsdlcache,opcache,session}


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
	--file /var/lib/zabbix/bin/fping 'attr(0750,root,zabbix)' \
	--file /var/lib/zabbix/bin/fping6 'attr(0750,root,zabbix)' \
	--dir /var/lib/zabbix/tmp 'attr(0750,zabbix,zabbix)' \
	--dir /var/log/php/zabbix  'attr(0770,www,www)' \
	--dir /var/lib/php/zabbix  'attr(0755,root,www)' \
 	--dir /var/lib/php/zabbix/tmp 'attr(0770,root,www)' \
 	--dir /var/lib/php/zabbix/opcache 'attr(0770,root,www)' \
 	--dir /var/lib/php/zabbix/session 'attr(0770,root,www)' \
	|grep -v '.pyc'|grep -v '.pyo' \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

