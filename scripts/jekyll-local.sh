#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PATCH_FILE="$ROOT_DIR/scripts/rbconfig_cxx_patch.rb"

export RBENV_VERSION="${RBENV_VERSION:-3.2.9}"
export BUNDLE_PATH="${BUNDLE_PATH:-$ROOT_DIR/vendor/bundle}"
export RUBYOPT="-r$PATCH_FILE${RUBYOPT:+ $RUBYOPT}"
if command -v xcrun >/dev/null 2>&1; then
  export SDKROOT="${SDKROOT:-$(xcrun --show-sdk-path)}"
  export CPLUS_INCLUDE_PATH="${SDKROOT}/usr/include/c++/v1${CPLUS_INCLUDE_PATH:+:${CPLUS_INCLUDE_PATH}}"
fi

cd "$ROOT_DIR"

ACTION="${1:-serve}"

run_bundle_install() {
  bundle install
}

case "$ACTION" in
  install)
    run_bundle_install
    ;;
  build)
    run_bundle_install
    bundle exec jekyll build
    ;;
  serve)
    run_bundle_install
    bundle exec jekyll serve -l -H localhost
    ;;
  *)
    echo "Usage: $0 [install|build|serve]" >&2
    exit 1
    ;;
esac
