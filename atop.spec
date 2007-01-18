Summary:	AT Computing System and Process Monitor
Summary(pl):	Monitor obci±¿enia systemu alternatywny dla programu top
Name:		atop
Version:	1.19
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.atconsultancy.nl/atop/packages/%{name}-%{version}.tar.gz
# Source0-md5:	4939916b1f2d03cb6c46752e6311adbb
Patch0:		%{name}-acct-alpha.patch
URL:		http://www.atcomputing.nl/Tools/atop
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program atop is an interactive monitor to view the load on a
Linux-system. It shows the occupation of the most critical
hardware-resources (from a performance point of view) on system-level,
i.e. cpu, memory, disk and network. It also shows which processes are
responsible for the indicated load (again cpu-, memory-, disk- and
network-load on process-level).

%description -l pl
Program atop to interaktywny monitor s³u¿±cy do obserwacji obci±¿enia
systemu linuksowego. Pokazuje zajêto¶æ najbardziej krytycznych dla
funkcjonowania systemu zasobów (z wydajno¶ciowego punktu widzenia) na
poziomie systemu, np. procesora, pamiêci, dysków czy sieci. Pokazuje
równie¿ które procesy s± odpowiedzialne za generowane obci±¿enie
(znów: na poziomie procesora, pamiêci, dysków czy sieci).

%prep
%setup -q
#%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}

install man/* $RPM_BUILD_ROOT%{_mandir}/man1/
install atop $RPM_BUILD_ROOT%{_bindir}/atop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR ChangeLog README
%attr(755,root,root) %{_bindir}/atop
%{_mandir}/man1/atop.1*
