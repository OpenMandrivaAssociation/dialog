%define fname	dialog
%define date	20080819

Summary:	A utility for creating TTY dialog boxes
Name:		dialog
Version:	1.1
Release:	%mkrel 1.%{date}.4
License:	LGPLv2+
URL:		http://invisible-island.net/dialog/
Group:		Development/Other
BuildRequires:	libncursesw-devel
Source:		ftp://invisible-island.net/dialog/%{fname}-%{version}-%{date}.tgz
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
%setup -q -n %{fname}-%{version}-%{date}

%build
%configure2_5x \
	--enable-nls \
	--with-ncursesw
%make

%install
rm -fr %buidlroot
%makeinstall_std

%find_lang %{fname}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files -f %{fname}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%{fname}
%{_mandir}/man1/%{fname}.*

