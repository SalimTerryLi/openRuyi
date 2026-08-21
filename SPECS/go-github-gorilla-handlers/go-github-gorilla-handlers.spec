# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           handlers
%define go_import_path  github.com/gorilla/handlers

Name:           go-github-gorilla-handlers
Version:        1.5.2
Release:        %autorelease
Summary:        HTTP middleware handlers for Go
License:        BSD-3-Clause
URL:            https://github.com/gorilla/handlers
#!RemoteAsset:  sha256:8760b84a1b5cd49ce81a56c9fce0ba0de157355b1bb38d112bdfd7cf7ad7a44d
Source0:        https://github.com/gorilla/handlers/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Fix a non-constant format string rejected by current Go vet.
Patch2000:      2000-Fix-non-constant-format-string-in-benchmark.patch
# Keep the canonical-host test within its local test server.
Patch2001:      2001-Avoid-external-redirect-in-canonical-host-test.patch
# Validate decompressed content because compressed sizes vary across Go releases.
Patch2002:      2002-tests-validate-compressed-content.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/felixge/httpsnoop)
BuildRequires:  tzdata

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/felixge/httpsnoop)

%description
Gorilla handlers provides reusable HTTP middleware for logging, compression,
CORS, content type restrictions, and request recovery.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
