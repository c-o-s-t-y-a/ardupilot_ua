#!/usr/bin/env bash
# Порівнює commit hash-і з translation-status.md з поточним upstream
# і виводить сторінки, джерело яких змінилося після перекладу.
# Використання: scripts/check-stale.sh [--no-fetch]
set -euo pipefail
cd "$(dirname "$0")/.."
[ "${1:-}" = "--no-fetch" ] || scripts/fetch-upstream.sh >/dev/null
stale=0
while IFS='|' read -r _ page md src commit date _; do
  src=$(echo "$src" | tr -d ' `'); commit=$(echo "$commit" | tr -d ' `'); page=$(echo "$page" | xargs)
  [[ "$src" == *.rst ]] || continue
  current=$(git -C .upstream log -1 --format=%H -- "$src")
  if [ -z "$current" ]; then
    echo "ВИДАЛЕНО  $page ($src більше немає в upstream)"; stale=1
  elif [[ "$current" != "$commit"* ]]; then
    echo "ЗМІНЕНО   $page ($src)"
    git -C .upstream log --format='            %h %cs %s' "$commit..$current" -- "$src"
    stale=1
  fi
done < translation-status.md
[ $stale = 1 ] || echo "Усі перекладені сторінки актуальні."
exit $stale
