# design-divergent

<p>
  <a href="LICENSE"><img alt="Licence" src="https://img.shields.io/badge/licence-MIT-8f8a7c"></a>
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-skill-D97757">
  <img alt="Statut" src="https://img.shields.io/badge/statut-exp%C3%A9rimental-e07a3f">
  <a href="README.md"><b>English</b></a>
</p>

Un skill Claude Code pour obtenir des propositions de design **vraiment**
différentes, puis trancher sur pièces.

Demande un écran à trois modèles, tu as trois fois le même écran. Demande
« quelque chose d'audacieux », tu as le même écran avec un dégradé. Le
problème, ce n'est pas le modèle, c'est le brief. Ce skill travaille le brief.

## Ce qu'il fait

1. **Il nettoie le brief.** Il écrit l'usage au lieu de l'artefact (« trois
   secondes et un pouce », pas « un tableau de bord »), passe le test des noms
   pour retirer les décisions de design cachées dans la demande, enlève les
   références qui seraient copiées, sépare les contraintes dures du goût.
2. **Il propose des mandats orthogonaux.** Six à huit partis pris
   esthétiques, jamais des objets à dessiner, plus une rupture qui casse la
   catégorie. Tu en choisis trois plus la rupture.
3. **Il produit en aveugle.** Quatre agents Sonnet en parallèle, chacun avec
   son seul mandat. Chacun écrit d'abord ce qu'il ferait par défaut, puis a
   interdiction de le faire.
4. **Il lit les défauts.** Mis côte à côte, les défauts écartés montrent
   l'*attracteur* : à quoi ressemble le banal sur ce brief.
5. **Il compose.** Un agent Opus propose une direction faite de morceaux pris
   aux variantes, et dit ce qu'il refuse de prendre à chacune.
6. **Tu tranches**, sur pièces visibles. Tes refus sont gardés mot pour mot,
   comme interdits pour le tour suivant.

## Installer

```bash
git clone https://github.com/amiel-35/ix-design-divergent ~/.claude/skills/design-divergent
```

Puis dans Claude Code : `/design-divergent` suivi de ta demande, ou juste
« fais diverger » quand les propositions se ressemblent toutes.

En option : copie `local.example.md` en `local.md` pour tes propres
contraintes dures (design system, outils à ne jamais utiliser). `local.md`
est ignoré par git.

## Coût

Environ 12 minutes et 185 000 tokens par variante, mesurés sur un run, soit à
peu près 750 000 tokens pour un tour complet. Ça se réserve aux livrables qui
comptent, pas aux retouches.

## Documentation

- [Ce qu'on sait](docs/fr/methode.md) : dix constats, chacun avec le cas d'où
  il vient.
- [Les cinq cas](docs/fr/cas.md) : des runs réels, anonymisés.
- [Ce qu'on ne sait pas encore](docs/fr/questions-ouvertes.md), dont la
  raison pour laquelle la composition a été rejetée aux deux derniers runs.

## Licence

MIT.
