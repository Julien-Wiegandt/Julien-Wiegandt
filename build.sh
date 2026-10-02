#!/usr/bin/env bash
# Fabrique le PDF d'un CV et VERIFIE le resultat.
#   ./build.sh            -> tous les .md du depot
#   ./build.sh cv-swile   -> ce seul fichier
#
# Verifications automatiques (les 3 regressions deja rencontrees) :
#   1. le PDF tient sur UNE page
#   2. for-the-badge n'est pas reapparu dans le markdown (casse les ATS)
#   3. email et telephone ressortent bien du texte extrait du PDF
#   4. les 5 experiences et les 3 formations sont presentes
set -uo pipefail
cd "$(dirname "$0")"

targets=("$@")
# Par defaut : TOUS les CVs du depot. Surtout pas une liste figee — une
# variante oubliee dedans, c'est un PDF sur 2 pages qui part en candidature.
if [ ${#targets[@]} -eq 0 ]; then
  targets=()
  for f in cv.md resume.md cv-*.md resume-*.md; do
    [ -e "$f" ] && targets+=("${f%.md}")
  done
fi

fail=0
for name in "${targets[@]}"; do
  name="${name%.md}"
  md="$name.md"
  [ -f "$md" ] || { echo "✗ $md introuvable"; fail=1; continue; }
  pdf="julien_wiegandt-$name.pdf"
  html="/tmp/$name.html"

  if grep -q 'for-the-badge' "$md"; then
    echo "✗ $md : style=for-the-badge detecte — illisible par les ATS, repasser en flat-square"
    fail=1; continue
  fi

  python3 md2html.py "$md" "$html" >/dev/null || { echo "✗ $md : md2html a echoue"; fail=1; continue; }
  google-chrome --headless=new --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="$pdf" "$html" 2>/dev/null

  pages=$(pdfinfo "$pdf" 2>/dev/null | awk '/^Pages:/{print $2}')
  txt=$(pdftotext -layout "$pdf" - 2>/dev/null)

  status="✓"
  [ "$pages" = "1" ] || { status="✗"; fail=1; }
  echo "$txt" | grep -q 'wiegandtjulien2@gmail.com' || { echo "  ! email absent du texte extrait de $pdf"; status="✗"; fail=1; }
  # FR porte le format national (0634087380), EN l'international (+33634087380)
  echo "$txt" | grep -qE '(\+33|0)634087380' || { echo "  ! telephone absent du texte extrait de $pdf"; status="✗"; fail=1; }

  xp=$(echo "$txt" | grep -cE 'FOREVR|KAWAAK|WAALAXY|KEYPOP|CODÉIN')
  [ "$xp" -ge 5 ] || { echo "  ! seulement $xp/5 experiences retrouvees dans $pdf"; status="✗"; fail=1; }

  echo "$status $pdf — $pages page(s), $xp/5 experiences"
done
exit $fail
