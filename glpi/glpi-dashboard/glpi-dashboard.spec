# spec file for glpi-dashboard
#
# Copyright (c) 2014 Cedric Grun
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%global pluginname   dashboard

Name:		glpi-%{pluginname}
Version:	0.5.2
Release:	1%{?dist}
Summary:	Statistics and reports for GLPI.
Summary(fr):	Statistiques et des rapports pour GLPI.

Group:		Applications/Internet
License:	AGPLv3+
URL:		https://forge.indepnet.net/projects/%{pluginname}

Source0:	https://forge.indepnet.net/attachments/download/1844/%{pluginname}_plugin-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	glpi >= 0.84
Requires:	glpi < 0.85

%description
Statistics and reports for GLPI.

%description -l fr
Statistiques et des rapports pour GLPI.


%prep
%setup -q -c


%build
# empty build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/glpi/plugins
cp -ar %{pluginname} %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_datadir}/glpi/plugins/%{pluginname}


%changelog
* Mon Sep  8 2104 Cedric Grun <cedric.grun@gmail.com> - 0.5.2-1
- version 0.5.2 for GLPI 0.84
  https://forge.indepnet.net/versions/1086

