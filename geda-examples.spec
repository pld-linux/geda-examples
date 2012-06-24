Summary:	Examples for gEDA project
Summary(pl.UTF-8):	Przykłady dla projektu gEDA
Name:		geda-examples
Version:	1.4.2
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.4/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	09c7adfcf9cb27955aa273a780538935
URL:		http://www.geda.seul.org/
Requires:	libgeda >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Examples for gEDA project.

%description -l pl.UTF-8
Przykłady dla projektu gEDA.

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog NEWS README
%{_docdir}/geda-doc/examples
