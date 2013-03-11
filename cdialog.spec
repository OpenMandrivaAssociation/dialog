%define fname	dialog
%define date	20120706

%bcond_without	uclibc

Summary:	A utility for creating TTY dialog boxes
Name:		cdialog
Version:	1.1
Release:	1.%{date}.2
License:	LGPLv2+
Group:		Development/Other
Url:		http://invisible-island.net/dialog/
Source0:	ftp://invisible-island.net/dialog/%{fname}-%{version}-%{date}.tgz
Patch0:		dialog-1.1-20120706-localedir.patch
Patch1:		dialog-1.1-20120706-wholeprogram.patch

BuildRequires:	pkgconfig(ncursesw)
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif
%rename		%{fname}

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.  

Install dialog if you would like to create TTY dialog boxes.

%package -n	uclibc-%{name}
Summary:	A utility for creating TTY dialog boxes (uClibc build)
Group:		Development/Other

%description -n	uclibc-%{name}
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.  

Install dialog if you would like to create TTY dialog boxes.

%prep
%setup -qn %{fname}-%{version}-%{date}
%patch0 -p1 -b .localedir~
%patch1 -p1 -b .whole_program~

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%uclibc_configure \
	--enable-nls \
	--with-ncursesw \
	--disable-rpath-hack
%make WHOLE_PROGRAM=1
popd
%endif

mkdir -p system
pushd system
%configure2_5x	\
	--enable-nls \
	--with-ncursesw \
	--disable-rpath-hack
%make WHOLE_PROGRAM=1
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc WHOLE_PROGRAM=1
%endif

%makeinstall_std -C system WHOLE_PROGRAM=1

%find_lang %{fname}

%files -f %{fname}.lang
%doc README
%{_bindir}/%{fname}
%{_mandir}/man1/%{fname}.*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/%{fname}
%endif

