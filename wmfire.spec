Summary:	Program that displays CPU load as fire in a small icon
Summary(pl):	Aplet pokazuj±cy obci¿enie CPU w malym okienku
Name:		wmfire
Version:	0.0.3.9pre4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.zebra.net/~dm/wmfire
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install wmfire fireload_cpu fireload_file  $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README ChangeLog NEWS AUTHORS CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
