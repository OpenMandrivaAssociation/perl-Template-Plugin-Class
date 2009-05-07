%define module  Template-Plugin-Class
%define name    perl-%{module}
%define version 0.14
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Allow calling of class methods on arbitrary classes
License:        Artistic
group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.bz2
Buildrequires:  perl(Template)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}

%description
Template::Plugin::Class allows you to call class methods on arbitrary classes.

%prep
%setup -q -n %{module}-%{version} 

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

