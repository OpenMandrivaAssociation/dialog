%define fname	dialog
%define date	20120706

%bcond_with	uclibc

Summary:	A utility for creating TTY dialog boxes
Name:		cdialog
Version:	1.1
Release:	1.%{date}.2
License:	LGPLv2+
URL:		http://invisible-island.net/dialog/
Group:		Development/Other
Source0:	ftp://invisible-island.net/dialog/%{fname}-%{version}-%{date}.tgz
Patch0:		dialog-1.1-20120706-dont-pass-link-directory.patch
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

%if %{with uclibc}
mkdir .uclibc
cp -a * .uclibc
%endif

%build
%if %{with uclibc}
pushd .uclibc
%uclibc_configure \
	--enable-nls \
	--with-ncursesw \
	--disable-rpath-hack
sed -e 's#-L%{_libdir}##g' -e 's#-L/%{_lib}##g' -i makefile
%make localedir=%{_localedir}
popd
%endif

%configure2_5x	\
	--enable-nls \
	--with-ncursesw \
	--disable-rpath-hack
sed -e 's#-L%{_libdir}##g' -e 's#-L/%{_lib}##g' -i makefile
%make

%install
%if %{with uclibc}
%makeinstall_std -C .uclibc
%endif

%makeinstall_std

%find_lang %{fname}

%files -f %{fname}.lang
%doc README
%{_bindir}/%{fname}
%{_mandir}/man1/%{fname}.*

%if %{with uclibc}
%files -n uclibc-%{name}
%{uclibc_root}%{_bindir}/%{fname}
%endif

%changelog
* Thu Dec 27 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1-1.20120706.1
- do uclibc build
- get rid of stupid rpath

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-1.20100119.3mdv2011.0
+ Revision: 663357
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-1.20100119.2mdv2011.0
+ Revision: 603817
- rebuild

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 1.1-1.20100119.1mdv2010.1
+ Revision: 498390
- New snapshot 20100119

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 1.1-1.20080819.4mdv2010.1
+ Revision: 498368
- should be cdialog
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - do not package huge examples

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

  + Antoine Ginies <aginies@mandriva.com>
    - 2009.1 rebuild

  + Adam Williamson <awilliamson@mandriva.org>
    - update to latest upstream (20080819)
    - clean spec a bit

* Sat Jul 12 2008 Wanderlei Cavassin <cavassin@mandriva.com.br> 1.1-1.20080316.1mdv2009.0
+ Revision: 234016
- update to 20080316 from upstream
- packaged lang files with nls support
- fix UTF-8 display with ncursesw

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-1.20070704.1mdv2009.0
+ Revision: 136289
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.20070704.1mdv2008.1-current
+ Revision: 123037
- kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Adam Williamson <awilliamson@mandriva.org> 1.1-1.20070704.1mdv2008.0
+ Revision: 83202
- rebuild for 2008
- don't package COPYING
- specify source URL
- remove period from summary
- Fedora license policy, correct license (LGPL not GPL)
- improve versioning
- update to 20070704 from upstream (many useful fixes)

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages


* Tue Mar 06 2007 Stefan van der Eijk <stefan@mandriva.org> 1.1-1mdv2007.0
+ Revision: 133660
- 1.1-20070227
- fix makeinstall
- add manpage

* Sat Nov 04 2006 Stefan van der Eijk <stefan@mandriva.org> 0.9b-9mdv2007.1
+ Revision: 76520
- rebuild for signature
- rebuild + %%mkrel
- Import cdialog

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 0.9b-7mdk
- rebuild for sparc

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.9b-6mdk
- Rebuild

* Wed Jun 02 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.9b-5mdk
- 20040421

