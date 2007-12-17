%define name	cdialog
%define fname	dialog
%define version	1.1
%define date	20070704
%define release	%mkrel 1.%{date}.1

Summary:	A utility for creating TTY dialog boxes
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
URL:		http://invisible-island.net/dialog/
Group:		Development/Other
BuildRequires:	ncurses-devel
Source:		ftp://invisible-island.net/dialog/%{fname}-%{version}-%{date}.tgz
Obsoletes:	dialog
Provides:	dialog

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.  

Install dialog if you would like to create TTY dialog boxes.

%prep
%setup -q -n %{fname}-%{version}-%{date}

%configure

%build
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
%make OPTIM="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
%makeinstall

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%files
%defattr(-,root,root)
%doc README samples
%{_bindir}/%{fname}
%{_mandir}/man1/%{fname}.*

