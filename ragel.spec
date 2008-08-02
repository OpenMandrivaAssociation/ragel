Name:           ragel   
Version:        6.2
Release:        %mkrel 1
Summary:        Finite state machine compiler

Group:          Development/Other
License:        GPLv2+
URL:            http://www.cs.queensu.ca/~thurston/ragel/ 
Source0:        http://www.cs.queensu.ca/~thurston/ragel/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  transfig, tetex-latex

Patch0:         ragel-Makefile-install.patch

%description
Ragel compiles finite state machines from regular languages into executable C,
C++, Objective-C, or D code. Ragel state machines can not only recognize byte
sequences as regular expression machines do, but can also execute code at
arbitrary points in the recognition of a regular language. Code embedding is
done using inline operators that do not disrupt the regular language syntax.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make 
pushd doc
%make
popd


%install
rm -rf %{buildroot}
%makeinstall
chmod a-x examples/*
pushd doc
%makeinstall
popd

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING ragel.vim
%doc examples
%doc doc/ragel-guide.pdf
%{_bindir}/rlgen-ruby
%{_bindir}/rlgen-java
%{_bindir}/rlgen-dot
%{_bindir}/rlgen-cd
%{_bindir}/rlgen-csharp
%{_bindir}/ragel
%{_mandir}/*/*

