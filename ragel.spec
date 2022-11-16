Summary:        Finite state machine compiler
Name:           ragel
Version:        7.0.4
Release:        1
Group:          Development/Other
License:        GPLv2+
Url:            http://www.cs.queensu.ca/~thurston/ragel/
Source0:        http://www.cs.queensu.ca/~thurston/ragel/%{name}-%{version}.tar.gz

%description
Ragel compiles finite state machines from regular languages into executable C,
C++, Objective-C, D, Java or Ruby code.

Ragel state machines can not only recognize byte sequences as regular
expression machines do, but can also execute code at arbitrary points in the
recognition of a regular language.

Code embedding is done using inline operators that do not disrupt the regular
language syntax.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --disable-manual \
  RUBY=ruby \
  JAVAC=javac \
  GMCS=gmcs

%make_build

%install
%make_install
chmod a-x examples/*

%files
%doc ragel.vim
%doc examples
%doc doc/ragel-guide.pdf
%doc CREDITS ChangeLog
%{_bindir}/ragel
%{_mandir}/*/*

