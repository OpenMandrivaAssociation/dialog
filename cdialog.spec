%define fname dialog
%define date 20150920

%bcond_with uclibc

Summary:	A utility for creating TTY dialog boxes
Name:		cdialog
Version:	1.2
Release:	1.%{date}.3
License:	LGPLv2+
Group:		Development/Other
Url:		http://invisible-island.net/dialog/
Source0:	ftp://invisible-island.net/dialog/%{fname}-%{version}-%{date}.tgz
Patch0:		dialog-1.2-20150920-fix-linking-with-llvm-ar.patch
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

%if %{with uclibc}
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
%endif

%prep
%setup -qn %{fname}-%{version}-%{date}
%apply_patches

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
#cb cant use uclibc_configure due to localedir
%configure2_5x \
        --libdir=%{uclibc_root}%{_libdir} \
        --prefix=%{uclibc_root}%{_prefix} \
        --exec-prefix=%{uclibc_root}%{_prefix} \
        --bindir=%{uclibc_root}%{_bindir} \
        --sbindir=%{uclibc_root}%{_sbindir} \
        --enable-nls \
        --with-ncursesw \
        --disable-rpath-hack \
        --enable-static \
        CC="%{uclibc_cc}" \
        CXX="%{uclibc_cxx}" \
        CFLAGS="%{uclibc_cflags}" \
        CXXFLAGS="%{uclibc_cxxflags}"
%make
popd
%endif

mkdir -p system
pushd system
%configure	\
	--enable-nls \
	--with-ncursesw \
	--disable-rpath-hack
%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
rm -f %{buildroot}/%{uclibc_root}/%{_libdir}/*.a
%endif

%makeinstall_std -C system
rm -f %{buildroot}%{_libdir}/*.a

%find_lang %{fname}

%files -f %{fname}.lang
%doc README
%{_bindir}/%{fname}
%{_mandir}/man1/%{fname}.*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/%{fname}
%endif
