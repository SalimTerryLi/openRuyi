# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           libsodium-go
%define go_import_path  github.com/GoKillers/libsodium-go
%define commit_id       dd733721c3cbec0224c4bb759642300c302cc9ad

Name:           go-github-gokillers-libsodium-go
Version:        0+git20260819.dd73372
Release:        %autorelease
Summary:        Go bindings for libsodium
License:        ISC
URL:            https://github.com/GoKillers/libsodium-go
#!RemoteAsset:  sha256:fdfe40f382fd493348fe07b3b51f933a05ebb616b7fd266a764d22223fc5f2ea
Source0:        https://github.com/GoKillers/libsodium-go/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Use the current name of libsodium's internal random implementation symbol.
Patch2000:      2000-Use-current-libsodium-random-implementation-symbol.patch
# Pass the typed AES-GCM state required by current libsodium headers.
Patch2001:      2001-Use-typed-AES-GCM-state-with-current-libsodium.patch
# Use Errorf for formatted output accepted by current Go vet.
Patch2002:      2002-Fix-formatted-test-error-reporting.patch

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/gofuzz)
BuildRequires:  pkgconfig(libsodium)

Provides:       go(%{go_import_path}) = %{version}

Requires:       pkgconfig(libsodium)

%description
Libsodium-go provides Go bindings for authenticated encryption, signatures,
hashing, key derivation, and other libsodium cryptographic primitives.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
