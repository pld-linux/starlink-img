Summary:	IMG - simple image data access
Summary(pl):	IMG - prosty dostêp do danych z obrazów
Name:		starlink-img
Version:	1.3_1.218
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/img/img.tar.Z
# Source0-md5:	cf2ee9e2c8a6b23314493c57615af049
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_IMG.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-ndf-devel
BuildRequires:	starlink-sae-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
IMG is a subroutine library for accessing astronomical image data and
associated header information. It is designed to be easy to use and
understand.

%description -l pl
IMG to biblioteka funkcji dostêpu do danych obrazów astronomicznych i
powi±zanych informacji z nag³ówków. Jest tak zaprojektowana, by by³a
³atwa w u¿yciu i do zrozumienia.

%package devel
Summary:	Header files for IMG library
Summary(pl):	Pliki nag³ówkowe biblioteki IMG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-ndf-devel

%description devel
Header files for IMG library.

%description devel -l pl
Pliki nag³ówkowe biblioteki IMG.

%package static
Summary:	Static Starlink IMG library
Summary(pl):	Statyczna biblioteka Starlink IMG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink IMG library.

%description static -l pl
Statyczna biblioteka Starlink IMG.

%prep
%setup -q -c

sed -i -e "s/ -O / %{rpmcflags} /;s/ ld -shared -soname / g77 -shared \\\$\\\$3 -Wl,-soname=/" mk
sed -i -e "s/-L\\\$(STAR_LIB) /-L\\\$(STARLINK)\\/share -lhdspar_adam /" makefile

%build
PATH="$PATH:%{stardir}/bin" \
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc img.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/img_dev
%attr(755,root,root) %{stardir}/bin/img_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
