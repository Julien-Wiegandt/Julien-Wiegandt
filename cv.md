<style>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap');
@page {
  size: A4;
  margin: 11mm 14mm;
}
* {
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
}
body {
  font-size: 12.5px !important;
  line-height: 1.42 !important;
  font-family: 'Ubuntu', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif !important;
  color: #1a1a1a !important;
}
p, li, td, h4, h1, h3 {
  font-family: 'Ubuntu', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif !important;
}
p, li, td, h4 {
  font-size: 12.5px !important;
  line-height: 1.42 !important;
}
h1 {
  font-size: 22px !important;
  margin: 0 0 4px !important;
  color: #14161A !important;
  font-weight: 700 !important;
  border-bottom: none !important;
  padding-bottom: 0 !important;
}
h3 {
  font-size: 15px !important;
  margin: 19px 0 7px !important;
  padding-bottom: 4px !important;
  color: #14161A !important;
  font-weight: 600 !important;
  display: flex !important;
  align-items: flex-end !important;
  gap: 7px !important;
}
h3 img { margin: 0 !important; }
p { margin: 4px 0 !important; }
ul { margin: 3px 0 8px !important; padding-left: 18px !important; }
li { margin: 2px 0 !important; }
hr { margin: 9px 0 !important; }
table { font-size: 12.5px !important; border-collapse: collapse !important; }
td { padding: 4px 7px !important; vertical-align: middle !important; }
/* Tech stack badges: slightly smaller to fit on one line */
td img { height: 18px !important; }
h4 { margin: 3px 0 !important; }
img { vertical-align: middle; }
/* Contact badges in header: smaller to fit one line */
p[align="left"] img { height: 19px !important; margin: 0 1px !important; }
/* Dates (inline code): bold colored text */
code {
  background: #eef0ff !important;
  color: #4F46E5 !important;
  padding: 1px 6px !important;
  border-radius: 4px !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  font-family: 'SF Mono', 'Consolas', monospace !important;
}
</style>

<h1 align="left">Julien Wiegandt</h1>
<p align="left"><strong style="font-size:15px;">Founding & Full-stack Engineer</strong> <span style="font-size:15px;">· TypeScript / React / Node.js · <strong>5+ ans d'xp</strong></span></p>

<p align="left">
<a href="mailto:wiegandtjulien2@gmail.com"><img src="https://img.shields.io/badge/Email-wiegandtjulien2%40gmail.com-4F46E5?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://calendar.app.google/CQjuoc67hZe4452G8"><img src="https://img.shields.io/badge/Prendre%20RDV-4285F4?style=for-the-badge&logo=googlecalendar&logoColor=white" /></a>
<a href="https://github.com/Julien-Wiegandt"><img src="https://img.shields.io/badge/GitHub-CV%20détaillé%20ici-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

Founding Engineer & Co-fondateur d'un **SaaS IA** adopté par **PayFit, Canva & Notion**. À l'aise sur l'ensemble du **full stack**, de l'architecture système et API jusqu'au motion UI et à la qualité produit. J'écris du **TypeScript strict**, des **systèmes type-safe de bout en bout**, et livre des produits scalables.


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Briefcase.png" alt="Expérience" width="22" /> Expérience

- **Founding Engineer & Co-fondateur · [KAWAAK](https://kawaak.com)** · `Nov. 2024 → Aujourd'hui`
  SaaS de génération de contenu LinkedIn par IA, construit de zéro à 3 personnes.
  - **+23K utilisateurs · +200K€ ARR · adopté par PayFit, Canva, Notion · 4.8/5 (150+ avis)**
  - Architecture full-stack : monorepo NX, React / Vite (TS strict), backend Node / Express / Zod type-safe, MongoDB + Redis + BullMQ
  - Orchestration multi-LLM (OpenAI, Anthropic) · auth Clerk · Stripe + PayPal · AWS · Sentry / PostHog / Mixpanel
  - Ownership de bout en bout : architecture, code review, déploiement, observabilité, support utilisateurs

- **Fondateur & CEO · [FOREVR](https://www.forevr.fr)** · `2025 → Aujourd'hui`
  Plateforme mémorielle où les familles préservent et partagent leurs souvenirs (photos, vidéos, audio) via un QR code gravé sur une plaque plexiglas. Développé avec Next.js / React / TypeScript.

- **Fondateur & CEO · [KEYPOP](https://www.keypop.io)** · `2023 → Aujourd'hui`
  Application desktop (Electron) et extension Chrome associant des prompts IA à des raccourcis clavier.

- **Développeur Full-stack · [WAALAXY](https://www.waalaxy.com)** · `Mai 2022 → Nov. 2024`
  Plateforme de prospection LinkedIn, **+1M utilisateurs**, équipe de 16 ingénieurs.
  - Intégré la **recherche vectorielle de prospects (Pinecone)** dans l'onboarding, **+80% de conversion** (validé par A/B testing)
  - Livré un **service de prospection email** qui a **multiplié par 10 le volume d'emails envoyés** + **intégration native HubSpot**
  - Architecture micro-services haute charge : event-driven (Kafka), MongoDB, déploiement conteneurisé

- **Développeur Front-end React · CODÉIN** · `Juin 2021 → Août 2021`
  Développé **90% de la nouvelle web app de gestion du personnel** de [OPPBTP](https://www.oppbtp.com/) en React TypeScript.


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" alt="Stack" width="22" /> Stack technique

<table>
  <tr>
    <td width="20%" valign="top">
      <h4 align="center">Front-end</h4>
    </td>
    <td>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black" />
      <img src="https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white" />
      <img src="https://img.shields.io/badge/Styled--Components-DB7093?style=flat-square&logo=styled-components&logoColor=white" />
      <img src="https://img.shields.io/badge/React_Query-FF4154?style=flat-square&logo=reactquery&logoColor=white" />
      <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h4 align="center">Back-end</h4>
    </td>
    <td>
      <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" />
      <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" />
      <img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" />
      <img src="https://img.shields.io/badge/Zod-3E67B1?style=flat-square&logo=zod&logoColor=white" />
      <img src="https://img.shields.io/badge/REST-02569B?style=flat-square" />
      <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square" />
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h4 align="center">Data & Infra</h4>
    </td>
    <td>
      <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" />
      <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" />
      <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white" />
      <img src="https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white" />
      <img src="https://img.shields.io/badge/BullMQ-FF0000?style=flat-square" />
      <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" />
      <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" />
    </td>
  </tr>
  <tr>
    <td valign="top">
      <h4 align="center">Pratiques</h4>
    </td>
    <td>
      <img src="https://img.shields.io/badge/Monorepo_NX-143055?style=flat-square&logo=nx&logoColor=white" />
      <img src="https://img.shields.io/badge/Continuous_Delivery-0A0A0A?style=flat-square" />
      <img src="https://img.shields.io/badge/Code_Review-4F46E5?style=flat-square" />
      <img src="https://img.shields.io/badge/Web_Scraping-FF6B35?style=flat-square" />
    </td>
  </tr>
</table>


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Graduation%20Cap.png" alt="Formation" width="22" height="22" /> Formation

- **Maîtrise en Génie logiciel** · Université de Sherbrooke (Québec, Canada) *(double diplôme)* · 2021–2022
- **Diplôme d'Ingénieur, Informatique & Gestion** · Polytech Montpellier *(double diplôme)* · 2019–2022
- **DUT Informatique** · IUT de Blagnac · 2017–2019

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Globe%20Showing%20Europe-Africa.png" alt="Langues" width="22" height="22" /> Langues

🇫🇷 **Français** · Natif &nbsp;·&nbsp; 🇬🇧 **Anglais** · C1 / TOEIC 910
