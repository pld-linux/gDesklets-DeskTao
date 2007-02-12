
%define		pname		DeskTao
%define		pname_file	desktao

Summary:	DeskTao - displaying random passages from the Tao
Summary(pl.UTF-8):   DeskTao - wyświetlanie losowych fragmentów z Tao
Name:		gDesklets-%{pname}
Version:	3.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://gdesklets.gnomedesktop.org/files/%{pname_file}-%{version}.tar.bz2
# Source0-md5:	fbbf7c9491483790aa731a78a63a0d22
Patch0:		%{pname_file}-tao-file.patch
URL:		http://gdesklets.gnomedesktop.org/categories.php?func=gd_show_app&gd_app_id=58
Requires:	gDesklets
Requires:	gDesklets-DeskQuote
Provides:	gDesklets-display
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sensorsdir	%{_datadir}/gdesklets/Sensors
%define		_displaysdir	%{_datadir}/gdesklets/Displays

%description
DeskTao displays random passages from the Tao (or any properly
marked-up text) on your desktop in suitably relaxing colours.

%description -l pl.UTF-8
DeskTao wyświetla losowe fragmenty z Tao (lub dowolnego właściwie
pooznaczanego tekstu) na pulpicie w odpowiednio relaksujących
kolorach.

%prep
%setup -q -n %{pname_file}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sensorsdir}/DeskQuote,%{_displaysdir}/%{pname}}

cp -R gfx *.display $RPM_BUILD_ROOT%{_displaysdir}/%{pname}
cp -R tao $RPM_BUILD_ROOT%{_sensorsdir}/DeskQuote

find $RPM_BUILD_ROOT%{_sensorsdir}/%{pname} -name "CVS" |xargs rm -rf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sensorsdir}/DeskQuote/*
%{_displaysdir}/*
