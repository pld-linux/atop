Summary:	AT Computing System and Process Monitor
Summary(pl):	Monitor obci��enia systemu alternatywny dla programu top
Name:		atop
Version:	1.2
Release:	1
License:	GPL
Group:		System Environment
Source0:	ftp://ftp.atcomputing.nl/pub/tools/linux/%{name}-%{version}.tar.gz
URL:		ftp://ftp.atcomputing.nl/pub/tools/linux/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program atop is an interactive monitor to view the load on a
Linux-system. It shows the occupation of the most critical
hardware-resources (from a performance point of view) on system-level,
i.e. cpu, memory, disk and network. It also shows which processes are
responsible for the indicated load (again cpu-, memory-, disk- and
network-load on process-level).

%description -l pl
Program atop to interaktywny monitor s�u��cy do obserwacji obci��enia
systemu Linuksowego. Pokazuje zaj�to�� najbardziej krytycznych dla
funkcjonowania systemu zasob�w (z wydajno�ciowego punktu widzenia) na
poziomie systemu, np. procesora, pami�ci, dysk�w czy sieci. Pokazuje
r�wnie� kt�re procesy s� odpowiedzialne za generowane obci��enie
(zn�w: na poziomie procesora, pamieci, dysk�w czy sieci).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

install man/* $RPM_BUILD_ROOT%{_mandir}/man1/
install atop $RPM_BUILD_ROOT%{_bindir}/atop

gzip -nf9 README

%clean
rm -rf    $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/atop
%{_mandir}/man1/atop.1*
