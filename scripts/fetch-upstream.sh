#!/usr/bin/env bash
# Клонує (або оновлює) sparse-копію ardupilot_wiki у ./.upstream з повною історією комітів (без blob-ів).
set -euo pipefail
cd "$(dirname "$0")/.."
if [ ! -d .upstream/.git ]; then
  git clone -q --filter=blob:none --sparse https://github.com/ArduPilot/ardupilot_wiki .upstream
  git -C .upstream sparse-checkout set copter/source/docs common/source/docs plane/source/docs planner/source/docs planner2/source/docs
else
  git -C .upstream pull -q --ff-only
fi
git -C .upstream log -1 --format='upstream: %h %cs'
