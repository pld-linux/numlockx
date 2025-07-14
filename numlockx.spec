Summary:	numlockx - turn NumLock on for X Window
Summary(pl.UTF-8):	numlockx - włączanie NumLock w X Window
Name:		numlockx
Version:	1.2
Release:	1
License:	Free (?)
Group:		X11
Source0:	http://ktown.kde.org/~seli/numlockx/%{name}-%{version}.tar.gz
# Source0-md5:	be9109370447eae23f6f3f8527bb1a67
Patch0:		%{name}-acam.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little thingy allows you to start X with NumLock turned on (which
is a feature that a lot of people seem to miss and nobody really knew
how to achieve this).

%description -l pl.UTF-8
Ten programik pozwala na uruchomienie X z włączonym NumLock (co jest
cechą, której wielu osobom brakuje, a nikt tak naprawdę nie wie, jak
ją osiągnąć).

%prep
%setup -q
%patch -P0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog LICENSE TODO
%attr(755,root,root) %{_bindir}/numlockx
