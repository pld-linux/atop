# TODO
# - initscripts, logs, crons (see rpm files section at bottom of the spec)
Summary:	AT Computing System and Process Monitor
Summary(pl.UTF-8):	Monitor obciążenia systemu alternatywny dla programu top
Name:		atop
Version:	2.3.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.atoptool.nl/download/%{name}-%{version}.tar.gz
# Source0-md5:	48e1dbef8c7d826e68829a8d5fc920fc
URL:		https://www.atoptool.nl/
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program atop is an interactive monitor to view the load on a
Linux-system. It shows the occupation of the most critical
hardware-resources (from a performance point of view) on system-level,
i.e. cpu, memory, disk and network. It also shows which processes are
responsible for the indicated load (again cpu-, memory-, disk- and
network-load on process-level).

%description -l pl.UTF-8
Program atop to interaktywny monitor służący do obserwacji obciążenia
systemu linuksowego. Pokazuje zajętość najbardziej krytycznych dla
funkcjonowania systemu zasobów (z wydajnościowego punktu widzenia) na
poziomie systemu, np. procesora, pamięci, dysków czy sieci. Pokazuje
również które procesy są odpowiedzialne za generowane obciążenie
(znów: na poziomie procesora, pamięci, dysków czy sieci).

%prep
%setup -q

%{__sed} -i -e '/chown root/d' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} -j1 sysvinstall systemdinstall \
	INIPATH=/etc/rc.d/init.d \
	DESTDIR=$RPM_BUILD_ROOT

# drop versioned links
%{__rm} $RPM_BUILD_ROOT%{_bindir}/{atop,atopsar}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHOR ChangeLog README
%attr(755,root,root) %{_bindir}/atop
%attr(755,root,root) %{_bindir}/atopsar
%attr(755,root,root) %{_sbindir}/atopacctd
%{_mandir}/man1/atop*.1*
%{_mandir}/man5/atoprc*.5*
%{_mandir}/man8/atopacctd.8*

# review and package these:
# don't forget R: procps, find, etc what they use
%if 0
%dir %{_sysconfdir}/%{name}
# atop.daily - invoked from cron, move to %{_prefix}/lib instead?
%attr(755,root,root) %{_sysconfdir}/%{name}/atop.daily
%attr(754,root,root) /etc/rc.d/init.d/atop
%attr(754,root,root) /etc/rc.d/init.d/atopacct
%config(noreplace) %verify(not md5 mtime size) /etc/cron.d/atop
%config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/psaccs_atop
%config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/psaccu_atop
%dir /var/log/atop
%ghost /var/log/atop/dummy_after
%ghost /var/log/atop/dummy_before
%endif
