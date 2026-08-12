#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PATCH_FILE="$ROOT_DIR/scripts/rbconfig_cxx_patch.rb"
LOCAL_CONFIG_FILE="${LOCAL_CONFIG_FILE:-$ROOT_DIR/_config_docker.yml}"
JEKYLL_CONFIG_ARGS=(--config "$ROOT_DIR/_config.yml")
PROJECT_RUBY_VERSION="$(tr -d '[:space:]' < "$ROOT_DIR/.ruby-version")"

if [[ -f "$LOCAL_CONFIG_FILE" ]]; then
  JEKYLL_CONFIG_ARGS=(--config "$ROOT_DIR/_config.yml,$LOCAL_CONFIG_FILE")
fi

if ! command -v rbenv >/dev/null 2>&1; then
  echo "rbenv is required. Install it with: brew install rbenv ruby-build" >&2
  exit 1
fi

export RBENV_VERSION="${RBENV_VERSION:-$PROJECT_RUBY_VERSION}"
if ! rbenv versions --bare | grep -Fxq "$RBENV_VERSION"; then
  echo "Ruby $RBENV_VERSION is not installed. Run: rbenv install $RBENV_VERSION" >&2
  exit 1
fi

export PATH="$(rbenv root)/shims:$PATH"
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
    bundle exec jekyll build "${JEKYLL_CONFIG_ARGS[@]}"
    ;;
  serve)
    run_bundle_install
    bundle exec jekyll serve "${JEKYLL_CONFIG_ARGS[@]}" -l -H localhost
    ;;
  *)
    echo "Usage: $0 [install|build|serve]" >&2
    exit 1
    ;;
esac
