# spec file for glpi-escalation
#
# Copyright (c) 2014 Cedric Grun
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%global pluginname   escalation

Name:		glpi-%{pluginname}
Version:	0.84+1.3
Release:	1%{?dist}
Summary:	Ticket escalation
Summary(fr):	Escalade des tickets

Group:		Applications/Internet
License:	AGPLv3+
URL:		https://forge.indepnet.net/projects/%{pluginname}

Source0:	https://forge.indepnet.net/attachments/download/1832/%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	glpi >= 0.84
Requires:	glpi < 0.85

%description
Ticket escalation

%description -l fr
Escalade des tickets


%prep
%setup -q -c


%build
# Regenerate the locales
#for po in %{pluginname}/locales/*.po
#do
#	msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
#done


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_datadir}/glpi/plugins
cp -ar %{pluginname} %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}

#for i in %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}/locales/*
#do
#	lang=$(basename $i)
#	echo "%lang(${lang:0:2}) %{_datadir}/glpi/plugins/%{pluginname}/locales/${lang}"
#done | tee %{name}.lang


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_datadir}/glpi/plugins/%{pluginname}
%dir %{_datadir}/glpi/plugins/%{pluginname}/locales
%{_datadir}/glpi/plugins/%{pluginname}/*.php
%{_datadir}/glpi/plugins/%{pluginname}/ajax
%{_datadir}/glpi/plugins/%{pluginname}/front
%{_datadir}/glpi/plugins/%{pluginname}/inc
%{_datadir}/glpi/plugins/%{pluginname}/install


%changelog
* Wed Sep 10 2104 Cedric Grun <cedric.grun@gmail.com> - 0.84+1.3-1
- version 0.84+1.3 for GLPI 0.84
  https://forge.indepnet.net/versions/1058

