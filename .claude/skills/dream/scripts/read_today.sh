#!/usr/bin/env bash
# dream, step 1: print index.md, every note (notes/**/*.md) and every log file
# (log/**) as one text dump, each file preceded by a delimiter line.
# Read-only: never writes, moves, renames or deletes anything.

root=$(git rev-parse --show-toplevel 2>/dev/null) || root=$PWD
cd "$root" || exit 0

# NUL-delimited, byte-order sorted file lists (safe for spaces in names).
notes=()
logs=()
[ -d notes ] && mapfile -d '' notes < <(find notes -type f -name '*.md' -print0 | LC_ALL=C sort -z)
[ -d log ] && mapfile -d '' logs < <(find log -type f -print0 | LC_ALL=C sort -z)

index=()
[ -f index.md ] && [ -s index.md ] && index=(index.md)

total=0
for f in "${index[@]}" "${notes[@]}" "${logs[@]}"; do
  total=$(( total + $(wc -c < "$f") ))
done

print_file() {
  printf '===== FILE: %s =====\n' "$1"
  cat -- "$1"
  # Keep the next delimiter on its own line if the file lacks a final newline.
  if [ -n "$(tail -c1 -- "$1")" ]; then printf '\n'; fi
}

printf '===== DREAM STEP 1: read_today =====\n'
printf 'notes: %d\n' "${#notes[@]}"
printf 'log files: %d\n' "${#logs[@]}"
printf 'total bytes: %d\n' "$total"

if [ ${#index[@]} -gt 0 ]; then
  print_file index.md
else
  printf '===== MISSING: index.md =====\n'
fi

if [ ${#notes[@]} -gt 0 ]; then
  for f in "${notes[@]}"; do print_file "$f"; done
else
  printf '===== MISSING: notes/ =====\n'
fi

if [ ${#logs[@]} -gt 0 ]; then
  for f in "${logs[@]}"; do print_file "$f"; done
else
  printf '===== MISSING: log/ =====\n'
fi

exit 0
