# spec file for glpi-formcreator
#
# Copyright (c) 2014 Cedric Grun
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%global pluginname   formcreator

Name:		glpi-%{pluginname}
Version:	1.8.1
Release:	1%{?dist}
Summary:	Formcreator is a plugin for creating simple form of access to users.
Summary(fr):	Formcreator est un plugin permettant la création de formulaire simple d'accès aux utilisateurs.

Group:		Applications/Internet
License:	AGPLv3+
URL:		https://forge.indepnet.net/projects/%{pluginname}

Source0:	https://forge.indepnet.net/attachments/download/1600/%{pluginname}_%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	glpi >= 0.84
Requires:	glpi < 0.85

%description
Formcreator is a plugin for creating simple form of access to users.

%description -l fr
Formcreator est un plugin permettant la création de formulaire simple d'accès aux utilisateurs.


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
* Wed Sep 10 2104 Cedric Grun <cedric.grun@gmail.com> - 1.8.1-1
- version 1.8.1 for GLPI 0.84
  https://forge.indepnet.net/versions/980

