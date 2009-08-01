%define upstream_name    Template-Plugin-Class
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Allow calling of class methods on arbitrary classes
License:    Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Template/%{upstream_name}-%{upstream_version}.tar.bz2

Buildrequires:  perl(Template)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
Template::Plugin::Class allows you to call class methods on arbitrary classes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL installdirs=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Template
%{_mandir}/*/*
