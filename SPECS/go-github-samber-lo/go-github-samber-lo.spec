# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           lo
%define go_import_path  github.com/samber/lo

Name:           go-github-samber-lo
Version:        1.53.0
Release:        %autorelease
Summary:        Generic collection utilities for Go
License:        MIT
URL:            https://github.com/samber/lo
#!RemoteAsset:  sha256:07cbe427cc6c07e6b3b28224cd9a01fc13231d7655ad16f243e697528118f611
Source0:        https://github.com/samber/lo/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Restore test helpers omitted from the v1.53.0 release tag.
Patch2000:      2000-test-restore-helpers-required-by-examples.patch
# Avoid a timing-sensitive exact duration in the retry example output.
Patch2001:      2001-make-retry-example-timing-independent.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/text)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/text)

%description
Lo provides generic helpers for slices, maps, strings, channels, and functions
in a Lodash-style Go library.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
