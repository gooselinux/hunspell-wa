Name: hunspell-wa
Summary: Walloon hunspell dictionaries
Version: 0.4.15
Release: 4.1%{?dist}
Source0: http://chanae.walon.org/walon/aspell-wa-%{version}.tar.bz2
Group: Applications/Text
URL: http://chanae.walon.org/walon/aspell.php
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
Patch0: hunspell-wa-0.4.15-buildfix.patch

Requires: hunspell

%description
Walloon hunspell dictionaries.

%prep
%setup -q -n aspell-wa-%{version}
%patch0 -p1 -b .buildfix

%build
make myspell
for i in TODO README; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-1 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p wa.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/wa_BE.dic
cp -p wa.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/wa_BE.aff

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README LGPL ChangeLog TODO
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.4.15-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.4.15-3
- tidy spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 22 2008 Caolan McNamara <caolanm@redhat.com> - 0.4.15-1
- initial version
