Summary:	Program that displays CPU load as fire in a small icon
Summary(pl):	Aplet pokazuj�cy obci��enie CPU w ma�ym okienku
Name:		wmfire
Version:	0.0.3.9pre4
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmfire is an eye-candy dock applet for Window Maker that displays
generated fire, possibly according to how much load the system is
experiencing, or from a number somewhere in a file. wmfire requires
very little CPU. It has options for cyanish or orange/red flames, you
can even set it to display your motherboard temperature through
lm_sensors.

%description -l pl
wmfire jest apletem dla Window Makera pokazuj�cym wygenerowany ogie�
w zale�no�ci od stopnia obci��enia systemu lub liczby w jakim� pliku.
Nieznacznie obci��a procesor, wy�wietla niebieskie, pomara�czowe lub
czerwone p�omienie, mo�e wy�wietla� tak�e temperatur� p�yty g��wnej
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
install -d $RPM_BUILD_ROOT%{_bindir}

install wmfire fireload_cpu fireload_file  $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS CREDITS
%attr(755,root,root) %{_bindir}/*
