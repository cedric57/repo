# spec file for glpi-genericobject
#
# Copyright (c) 2014 Cedric Grun
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%global pluginname   genericobject

Name:		glpi-%{pluginname}
Version:	2.3.2
Release:	1%{?dist}
Summary:	Add new inventory objects.
Summary(fr):	Ajout de nouveaux types d'objets d'inventaire.

Group:		Applications/Internet
License:	AGPLv3+
URL:		https://forge.indepnet.net/projects/%{pluginname}

Source0:	https://forge.indepnet.net/attachments/download/1822/%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	glpi >= 0.84
Requires:	glpi < 0.85

%description
This plugin allows you to add new inventory types without programmation. It manages :
- Type creation
- Available fields
- Framework integration (Helpdesk, loans, templates, etc.)
- Integration with the file injection plugin

%description -l fr
Ce plugin vous permet d'ajouter de nouveaux types d'objets d'inventaire sans avoir à programmer.Il gère :
- La création du type
- Les champs disponibles
- L'intégration dans GLPI (Helpdesk, réservation, gabarits, etc.)
- L'intégration avec le plugin d'injection des données


%prep
%setup -q -c

mv %{pluginname}/docs docs
mv %{pluginname}/AUTHORS.txt AUTHORS.txt
mv %{pluginname}/README README

# dos2unix to avoid rpmlint warnings
for doc in docs/* ; do
	sed -i -e 's/\r//' $doc
done

# Create link to LICENSE for standard doc folder
ln -s %{_datadir}/glpi/plugins/%{pluginname}/LICENSE LICENSE

# For developer only
rm -rf %{pluginname}/tools


%build
# Regenerate the locales
for po in %{pluginname}/locales/*.po
do
	msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
done


%install
rm -rf %{buildroot}

# Plugin
mkdir -p %{buildroot}/%{_datadir}/glpi/plugins
cp -ar %{pluginname} %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}

# Locales
for i in %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}/locales/*
do
	lang=$(basename $i)
	echo "%lang(${lang:0:2}) %{_datadir}/glpi/plugins/%{pluginname}/locales/${lang}"
done | tee %{name}.lang


%clean
rm -rf %{buildroot}


%files  -f %{name}.lang
%defattr(-,root,root,-)
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc docs/* README AUTHORS.txt
%dir %{_datadir}/glpi/plugins/%{pluginname}
%dir %{_datadir}/glpi/plugins/%{pluginname}/locales
%{_datadir}/glpi/plugins/%{pluginname}/*.php
%{_datadir}/glpi/plugins/%{pluginname}/ajax
%{_datadir}/glpi/plugins/%{pluginname}/front
%{_datadir}/glpi/plugins/%{pluginname}/inc
%{_datadir}/glpi/plugins/%{pluginname}/fields
%{_datadir}/glpi/plugins/%{pluginname}/objects
# Keep here as required from interface
%{_datadir}/glpi/plugins/%{pluginname}/LICENSE

%changelog
* Thu Sep 11 2104 Cedric Grun <cedric.grun@gmail.com> - 2.3.2-1
- version 2.3.2 for GLPI 0.84
  https://forge.indepnet.net/versions/977

