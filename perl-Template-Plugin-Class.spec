%define module  Template-Plugin-Class
%define name    perl-%{module}
%define version 0.13
%define release %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Allow calling of class methods on arbitrary classes
License:        Artistic
group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Template/%{module}-%{version}.tar.bz2
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(Template)
buildArch:      noarch
buildRoot:      %{_tmppath}/%{name}-%{version}

%description
Template::Plugin::Class allows you to call class methods on arbitrary classes.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Template
%{_mandir}/*/*

