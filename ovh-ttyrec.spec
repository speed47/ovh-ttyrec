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
ovh-ttyrec (1.1.6.5) master; urgency=medium

  * fix: race condition when running w/o pty

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Thu, 15 Sep 2020 10:59:22 +0200

ovh-ttyrec (1.1.6.4) master; urgency=medium

  * fix: -k was not working correctly when used without -t

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Thu, 05 Mar 2020 16:29:12 +0100

ovh-ttyrec (1.1.6.3) master; urgency=medium

  * fix: race condition on exit when a sighandler gets called while we're in libc's exit(), fixes #7

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Fri, 10 Oct 2019 14:43:17 +0200

ovh-ttyrec (1.1.6.2) master; urgency=medium

  * fix: race condition on exit where ttyrec could get stuck

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Fri, 30 Aug 2019 12:39:23 +0200

ovh-ttyrec (1.1.6.1) master; urgency=medium

  * enh: with -f, auto-append .zst if -Z or --zstd was specified
  * fix: allow usage of -f even if -F if specified

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Fri, 14 Jun 2019 12:41:54 +0200

ovh-ttyrec (1.1.6.0) master; urgency=medium

  * feat: added generic fread/fwrite/fclose wrappers as a framework to support several (de)compression algorithms
  * feat: add zstd support to ttyrec and ttyplay
        ttyrec: add -Z option to enable on-the-fly compression if available
        ttyrec: add --zstd to force on-the-fly zstd compression
        ttyrec: add -l option to fine-tune the zstd compression ratio (between 1 and 19, default 3)
        ttyrec: add --max-flush-time to specify a number of seconds after which we force zstd to flush
          its output buffers to ensure somewhat idle sessions still get flushed to disk regularly
        ttyplay: zstd decompression is automatically enabled if the file suffix is ".zst"
        ttyplay: add -Z option to force on-the-fly zstd decompression regardless of the file suffix
        ttytime: add a warning if timing a .zst file is attempted (not supported)
  * feat: implement long-options parsing for ttyrec
  * feat: add --name-format (-F) to specify a custom file name compatible with strftime()
  * feat: add --warn-before-lock and --warn-before-kill options
  * fix: abort if doinput() can't write to master
  * chore: nicify termios debug output
  * chore: get rid of help2man requirement
  * chore: portability fixes, tested under Linux, FreeBSD, NetBSD, OpenBSD, DragonFlyBSD, Darwin, Haiku, OmniOS

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Tue, 04 Jun 2019 10:17:11 +0200

ovh-ttyrec (1.1.5.0) master; urgency=medium

  * First public release
  * Add -c option to enable cheatcodes, as they're now disabled by default

 -- Stéphane Lesimple (deb packages) <stephane.lesimple@corp.ovh.com>  Thu, 09 May 2019 12:55:21 +0200
