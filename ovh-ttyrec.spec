Summary: Extended (but compatible) fork of ttyrec
Name: ovh-ttyrec
Version: 1.1.6.5
Release: 1
License: 3-Clause BSD
Group: Applications/System
Source: https://github.com/ovh/ovh-ttyrec/archive/master.zip
BuildRoot: /var/tmp/%{name}-buildroot

%description
Description: Extended (but compatible) fork of ttyrec
 ttyrec is a terminal (tty) recorder, it comes with ttyplay, which is a tty player.
 Some features ov ovh-ttyrec follow:
 -   Drop-in replacement of the classic ttyrec, additional features don't break compatibility
 -   The code is portable and OS features that can be used are detected at compile time
 -   Supports ttyrec output file rotation without interrupting the session
 -   Supports locking the session after a keyboard input timeout, optionally displaying a custom message
 -   Supports terminating the session after a keyboard input timeout
 -   Supports manually locking or terminating the session via "cheatcodes" (specific keystrokes)
 -   Supports a no-tty mode, relying on pipes instead of pseudottys, while still recording stdout/stderr
 -   Automatically detects whether to use pseudottys or pipes, also overridable from command-line
 -   Supports reporting the number of bytes that were output to the terminal on session exit

%prep

%setup -q -n ovh-ttyrec

%build
STATIC=1 ./configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf -- "$RPM_BUILD_ROOT"

%files
%doc docs/ttyplay.1 docs/ttytime.1 docs/ttyrec.1
/usr/bin/ttyplay
/usr/bin/ttytime
/usr/bin/ttyrec

%changelog
* Wed Oct 20 2011 John Doe <jdoe@example.com> 2.1.5-0.1
- ovh-ttyrec (1.1.6.5) master; urgency=medium
