Summary:        Finite state machine compiler
Name:           ragel
Version:        6.8
Release:        7
Group:          Development/Other
License:        GPLv2+
Url:            http://www.cs.queensu.ca/~thurston/ragel/
Source0:        http://www.cs.queensu.ca/~thurston/ragel/%{name}-%{version}.tar.gz
BuildRequires:  transfig

%description
Ragel compiles finite state machines from regular languages into executable C,
C++, Objective-C, D, Java or Ruby code.

Ragel state machines can not only recognize byte sequences as regular
expression machines do, but can also execute code at arbitrary points in the
recognition of a regular language.

Code embedding is done using inline operators that do not disrupt the regular
language syntax.

%prep
%setup -q

%build
%configure2_5x
%make
pushd doc
%make
popd

%install
%makeinstall
chmod a-x examples/*
pushd doc
%makeinstall
popd

%files
%doc COPYING ragel.vim
%doc examples
%doc doc/ragel-guide.pdf
%{_bindir}/ragel
%{_mandir}/*/*

