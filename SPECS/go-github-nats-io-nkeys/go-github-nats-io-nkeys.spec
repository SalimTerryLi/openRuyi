# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           nkeys
%define go_import_path  github.com/nats-io/nkeys

Name:           go-github-nats-io-nkeys
Version:        0.4.16
Release:        %autorelease
Summary:        Ed25519 key and signature support for NATS
License:        Apache-2.0
URL:            https://github.com/nats-io/nkeys
#!RemoteAsset:  sha256:4c73b6badcb6337cb3ec895b4d0a819c2b6e7d6b1b6e753549d4ee6f2c2df29f
Source0:        https://github.com/nats-io/nkeys/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(golang.org/x/crypto)

%description
NKEYS provides Ed25519-based keys, seeds, signing, and verification for the
NATS ecosystem.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
