%define name	cdialog
%define version	1.1
%define release	%mkrel 1
%define datetag 20070227

Summary:	A utility for creating TTY dialog boxes.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://invisible-island.net/dialog/
Group:		Development/Other
BuildRequires:	ncurses-devel
Source:		dialog-%{version}-%{datetag}.tar.bz2
Obsoletes:	dialog
Provides:	dialog
BuildRoot:	%{_tmppath}/%{name}-root

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.  

Install dialog if you would like to create TTY dialog boxes.

%prep
%setup -q -n dialog-%{version}-%{datetag}

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
%doc COPYING README samples
%{_bindir}/dialog
%{_mandir}/man1/dialog.*
%{_mandir}/man3/dialog.*


