%define date 20240619
%global optflags %{optflags} -Oz

Summary:	A utility for creating TTY dialog boxes
Name:		dialog
Version:	1.3
Release:	0.%{date}.1
License:	LGPLv2+
Group:		Development/Other
Url:		http://invisible-island.net/dialog/
Source0:	http://invisible-island.net/archives/dialog/%{name}-%{version}-%{date}.tgz
Patch0:		dialog-1.2-20150920-fix-linking-with-llvm-ar.patch
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	gettext
BuildRequires:	locales-extra-charsets
%rename		cdialog

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.

Install dialog if you would like to create TTY dialog boxes.

%prep
%autosetup -n %{name}-%{version}-%{date} -p1

%build
%configure \
    --enable-nls \
    --with-ncursesw \
    --disable-rpath-hack || :
if ! [ -e makefile ]; then
    printf '%s\n' "Configure failed:"
    cat config.log
    exit 1
fi

%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.a

%find_lang %{name}

%files -f %{name}.lang
%doc README
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.*
