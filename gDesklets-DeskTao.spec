%include        /usr/lib/rpm/macros.python

%define	pname	   DeskTao
%define	pname_file desktao

Summary:	DeskTao displays random passages from the Tao
Name:		gDesklets-%{pname}
Version:	3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname_file}-%{version}.tar.bz2
# Source0-md5:	fbbf7c9491483790aa731a78a63a0d22
Patch0:		%{pname_file}-tao-file.patch
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=58
BuildRequires:	python >= 2.3
BuildRequires:	python-pygtk >= 1.99.14
Requires:	gDesklets
Requires:	gDesklets-DeskQuote
Provides:	gDesklets-display
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sensorsdir	%{_datadir}/gdesklets/Sensors
%define _displaysdir	%{_datadir}/gdesklets/Displays

%description
DeskTao displays random passages from the Tao (or any properly
marked-up text) on your desktop in suitably relaxing colours.

%prep
%setup -q -n %{pname_file}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir}/DeskQuote,%{_displaysdir}/%{pname}}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}
cp -R tao $RPM_BUILD_ROOT%{_sensorsdir}/DeskQuote

find $RPM_BUILD_ROOT%{_sensorsdir}/%{pname} -name "CVS" |xargs rm -rf

%py_comp $RPM_BUILD_ROOT%{_sensorsdir}
%py_ocomp $RPM_BUILD_ROOT%{_sensorsdir}

rm -f $RPM_BUILD_ROOT%{_sensorsdir}/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/DeskQuote/*
%{_displaysdir}/*
