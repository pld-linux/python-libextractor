Summary:	Python bindings for GNU libextractor
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GNU libextractor
Name:		python-libextractor
Version:	0.6
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://ftp.gnu.org/gnu/libextractor/libextractor-python-%{version}.tar.gz
# Source0-md5:	adea21c10163d262e02154b21b4f74a2
URL:		http://gnunet.org/libextractor/
BuildRequires:	libextractor-devel >= 0.6
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	libextractor >= 0.6
%pyrequires_eq	python-libs
Obsoletes:	python-extractor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for GNU libextractor.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki GNU libextractor.

%prep
%setup -q -n Extractor-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--skip-build \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/extract.py
%{py_sitescriptdir}/extractor.py[co]
%{py_sitescriptdir}/Extractor-0.6-py*.egg-info
