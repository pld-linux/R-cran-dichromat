%define		fversion	%(echo %{version} |tr r -)
%define		modulename	dichromat
Summary:	Color Schemes for Dichromats
Name:		R-cran-%{modulename}
Version:	2.0r0.1
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	https://cran.r-project.org/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	ce89c0b9bec34cd2d0a4ba4ec64024fb
URL:		http://socserv.socsci.mcmaster.ca/jfox/
BuildRequires:	R >= 2.8.1
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collapse red-green or green-blue distinctions to simulate the effects
of different types of color-blindness.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}
