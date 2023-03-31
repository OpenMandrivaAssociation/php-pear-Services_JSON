%define	_class	Services
%define	_subclass	JSON
%define	modname	%{_class}_%{_subclass}

Summary:	PHP implementaion of json_encode/decode
Name:		php-pear-%{modname}
Version:	1.0.3
Release:	13
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/%{modname}
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear

%description
This package provides a simple encoder and decoder for JSON notation. It is
intended for use with client-side Javascript applications that make use of
HTTPRequest to perform server communication functions - data can be encoded
into JSON notation for use in a client-side javascript, or decoded from
incoming Javascript requests. JSON format is native to Javascript, and can be
directly eval()'ed with no further parsing overhead.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%post
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{modname}.xml >/dev/null || :

%preun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{modname}.xml

