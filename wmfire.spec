Summary:	program that displays CPU load as fire in a small icon.
Name:		aplecik pokazujacy uzycie CPU w malym okienku 
Version:	0.0.3.9pre4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.zebra.net/~dm/wmfire
Requires:	XFree86-libs
Requires:	xpm
BuildRequires:	XFree86-devel
BuildRequires:  xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)



%define            _prefix         /usr/X11R6

%description
wmfire is an eye-candy dock applet for Window Maker that displays
generated fire, possibly according to how much load the system is
experiencing, or from a number somewhere in a file. wmfire requires
very little CPU. It has options for cyanish or orange/red flames, you
can even set it to display your motherboard temperature through
lm_sensors.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%_prefix/bin
install -m 755 {wmfire,fireload_cpu,fireload_file}  $RPM_BUILD_ROOT%_prefix/bin/


gzip -9nf README ChangeLog NEWS AUTHORS CREDITS 

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/*
