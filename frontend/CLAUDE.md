# CLAUDE.md — MenuDirect Landing Page

## Contexte projet

Site vitrine de **MenuDirect**, solution SaaS de prise de commande WhatsApp automatisée développée par l'agence **Snack-Flow**. Ce repo est indépendant du backend Snack-Flow (repo séparé).

**Objectif unique de ce repo :** Convertir les gérants de snacks/kebabs/pizzerias en prospects qualifiés via une prise de rendez-vous Google Meet avec le closer.

---

## Stack

- HTML/CSS/JS pur — fichier unique auto-contenu, zéro build step
- Tailwind CSS via CDN
- Plus Jakarta Sans via Google Fonts
- Material Symbols via Google Fonts
- Hébergement statique (à décider)

---

## Fichiers

```
/
├── CLAUDE.md          ← ce fichier
├── index.html         ← fichier principal (page entière)
└── assets/            ← images, favicon (si besoin)
```

---

## Produit & avatar

- **Produit :** Menu interactif WhatsApp + prise de commande automatisée + intégration caisse (HubRise)
- **Avatar :** Gérant de kebab/snack/pizzeria indépendant, non-technicien, peu de temps
- **Douleurs :** Appels manqués pendant le rush · commissions Uber Eats/Deliveroo (25-35%) · perte de relation client via plateformes
- **Promesse :** Opérationnel en 24h, zéro compétence technique

---

## Conversion

Tous les CTAs redirigent vers **`CALENDAR_LINK`** (placeholder à remplacer par le lien Google Calendar réel).
- Bouton navbar : "Essayer gratuitement"
- Bouton hero : "Voir la démo en direct →"
- Bouton CTA final : "Réserver ma démo gratuite →"

Tous en `<a href="CALENDAR_LINK" target="_blank" rel="noopener noreferrer">`.

---

## Design system

| Token | Valeur |
|---|---|
| CTA gradient | `linear-gradient(to right, #9f4200, #e8702a)` |
| Texte principal | `#0a1a3a` (navy — jamais noir pur) |
| Fond global | `#f8f9fa` |
| Fond cards | `#ffffff` |
| Fond sections alternées | `#f3f4f5` |
| Vert WhatsApp / succès | `#1b6d24` |
| Font | Plus Jakarta Sans |

Règles : pas de bordures 1px (tonal layering), pas d'illustrations tech/robots, mobile-first.

---

## Skill de référence

Le skill `web-designer-pro` contient tous les principes de design et conversion à appliquer.
Lire `/references/conversion.md` pour le copy et `/references/design-systems.md` pour les composants.

---

## Ce projet n'inclut PAS

- Backend, API, base de données
- Logique de commande WhatsApp (→ repo Snack-Flow)
- Système de paiement
- Back-office ou dashboard
