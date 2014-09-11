# spec file for glpi-barcode
#
# Copyright (c) 2014 Cedric Grun
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
%global pluginname   barcode
%global projectname  barscode

Name:		glpi-%{pluginname}
Version:	0.84_1.0
Release:	1%{?dist}
Summary:	Barcode
Summary(fr):	Code à barres

Group:		Applications/Internet
License:	AGPLv3+
URL:		https://forge.indepnet.net/projects/%{projectname}

Source0:	https://forge.indepnet.net/attachments/download/1558/%{name}-%{version}.tar.gz

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	glpi >= 0.84
Requires:	glpi < 0.85

%description
Barcode

%description -l fr
Code à barres


%prep
%setup -q -c

mv %{pluginname}/AUTHORS.txt AUTHORS.txt

# Create link to LICENSE for standard doc folder
ln -s %{_datadir}/glpi/plugins/%{pluginname}/LICENSE LICENSE


%build
# Regenerate the locales
for po in %{pluginname}/locales/*.po
do
	msgfmt $po -o $(dirname $po)/$(basename $po .po).mo
done


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_datadir}/glpi/plugins
cp -ar %{pluginname} %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}


for i in %{buildroot}/%{_datadir}/glpi/plugins/%{pluginname}/locales/*
do
	lang=$(basename $i)
	echo "%lang(${lang:0:2}) %{_datadir}/glpi/plugins/%{pluginname}/locales/${lang}"
done | tee %{name}.lang


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS.txt %{pluginname}/LICENSE
%dir %{_datadir}/glpi/plugins/%{pluginname}
%dir %{_datadir}/glpi/plugins/%{pluginname}/locales
%{_datadir}/glpi/plugins/%{pluginname}/*.php
%{_datadir}/glpi/plugins/%{pluginname}/ajax
%{_datadir}/glpi/plugins/%{pluginname}/front
%{_datadir}/glpi/plugins/%{pluginname}/inc
%{_datadir}/glpi/plugins/%{pluginname}/lib
# Keep here as required from interface
%{_datadir}/glpi/plugins/%{pluginname}/LICENSE


%changelog
* Wed Sep 10 2104 Cedric Grun <cedric.grun@gmail.com> - 0.84_1.0-1
- version 0.84_1.0 for GLPI 0.84
  https://forge.indepnet.net/versions/951

