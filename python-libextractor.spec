Summary:	Python support for libextractor
Summary(pl.UTF-8):	Moduł języka Python dla biblioteki libextractor
Name:		python-libextractor
Version:	0.5.4
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	http://gnunet.org/libextractor/download/libextractor-python-%{version}.tar.gz
# Source0-md5:	fbe72b00b8780b528892274b96c9d40f
Patch0:		libextractor-python-destdir.patch
URL:		http://gnunet.org/libextractor/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libextractor-devel >= %{version}
BuildRequires:	python-devel >= 1:2.3
Requires:	libextractor >= %{version}
%pyrequires_eq	python-libs
Obsoletes:	python-extractor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python support for libextractor.

%description -l pl.UTF-8
Moduł języka Python dla biblioteki libextractor.

%prep
%setup -q -n libextractor-python-%{version}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-extractor=/usr

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/*.so
