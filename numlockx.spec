Summary:	numlockx - turn NumLock on for X Window
Summary(pl.UTF-8):   numlockx - włączanie NumLock w X Window
Name:		numlockx
Version:	1.0
Release:	1
License:	Free (?)
Group:		X11/XFree86
Source0:	http://ourworld.cs.com/kvsmaster/files/%{name}-%{version}.tar.gz
# Source0-md5:	e6956c130f29d0099291281dc99f049b
BuildRequires:	XFree86
BuildRequires:	XFree86-devel
Requires:	XFree86
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

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/numlockx
