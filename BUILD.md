# Fabrication des CVs

```bash
./build.sh              # reconstruit les 4 PDFs et les verifie
./build.sh cv-pave      # un seul fichier
```

`build.sh` echoue si une des regressions deja rencontrees revient :
le PDF deborde sur 2 pages, `for-the-badge` reapparait, l'email ou le
telephone ne ressort pas du texte extrait, ou une experience manque.

## Tronc commun / couche variable

| Fichier | Role |
|---|---|
| `cv.md` / `resume.md` | **Tronc commun** FR et EN. Base de verite. |
| `cv-<cible>.md` | Variante d'une candidature **active**. Derivee de la base, supprimee quand le process est clos. |
| `style.css` | Feuille unique de tous les CVs. Tout correctif de mise en page se fait ici. |

**Sens du flux : un correctif atterrit dans la base, puis on re-derive
les variantes.** Jamais l'inverse — c'est comme ca que la base s'etait
retrouvee en retard de six semaines sur la variante Swile.

## Invariants geles (ne pas rediscuter sans refaire un test ATS)

- **Badges en `style=flat-square`.** Jamais `for-the-badge` : il applique
  majuscules + letter-spacing cote serveur dans le SVG, et aucun parser
  ATS n'en tire de texte. Cause reelle des echecs de parsing, prouvee
  par un test controle sur trois styles.
- **Badge LinkedIn** : glyphe inline en base64. shields.io ne sert plus
  `logo=linkedin`, un `logo=linkedin` nu rend un badge vide.
- **Ligne de contact**, dans cet ordre : Lieu · Email · Telephone ·
  LinkedIn · Prendre RDV · GitHub. Telephone sans espaces. Pays sur le
  lieu, pas de code postal.
- **Experiences** : `**[ENTREPRISE](url)** · Role · Ville, Pays · date`.
  Entreprise **en premier** (un ATS inversait entreprise et role sur
  l'ancien format). Mois ecrits en entier, tiret simple, pas de demi-cadratin.
- **Ordre antechronologique strict**, a une entorse assumee pres :
  Keypop (2023-2024) reste apres Waalaxy (2022-2024) malgre sa date de
  debut plus recente, parce que remonter une micro-experience au-dessus
  du poste le plus solide dessert la lecture humaine.
- **Budget de puces** : Forevr 2, Kawaak 3, Waalaxy 4, Keypop 0, Codein 0.
  Soit 9 puces — le maximum qui tient sur une page A4.
- **Stack** : 6 categories, ~30 badges, 6-7 max par ligne. Le contenu
  *dans* les lignes est variable par offre (ex. `Ruby on Rails - learning`
  pour Swile, absent de la base).
- **Mise en page** : `line-height: 1.33`, badges 18px. Seules valeurs qui
  tiennent sur une page avec 9 puces.

## Dettes ouvertes

- Repasser un checker ATS **en vue import** sur la base corrigee. Dernier
  resultat connu (avant corrections) : email tronque en `2@GMAIL.`,
  2 formations sur 3 perdues, 2 experiences sur 5 perdues.
- 4 puces non chiffrees, dont la plus couteuse : la revue de code et le
  mentorat chez Waalaxy. Manquent le volume de PR/semaine, le nombre de
  personnes onboardees et le nombre de meetups animes.
