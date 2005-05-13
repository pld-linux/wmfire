Summary:	Program that displays CPU load as fire in a small icon
Summary(pl):	Aplet pokazuj±cy obci±¿enie CPU w ma³ym okienku
Name:		wmfire
Version:	1.2.2
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.swanson.ukfsn.org/wmfire/%{name}-%{version}.tar.gz
# Source0-md5:	43eaca423b965c6093f4f22651e24d1d
Source1:	%{name}.desktop
URL:		http://www.swanson.ukfsn.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libgtop-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmfire is an eye-candy dock applet for Window Maker that displays
generated fire, possibly according to how much load the system is
experiencing, or from a number somewhere in a file. wmfire requires
very little CPU. It has options for cyanish or orange/red flames, you
can even set it to display your motherboard temperature through
lm_sensors.

%description -l pl
wmfire jest apletem dla Window Makera pokazuj±cym wygenerowany ogieñ w
zale¿no¶ci od stopnia obci±¿enia systemu lub liczby w jakim¶ pliku.
Nieznacznie obci±¿a procesor, wy¶wietla niebieskie, pomarañczowe lub
czerwone p³omienie, mo¿e wy¶wietlaæ tak¿e temperaturê p³yty g³ównej
poprzez lm_sensors.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
%{_mandir}/man1/*
