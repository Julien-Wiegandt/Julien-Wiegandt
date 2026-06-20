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
<p align="left"><strong style="font-size:15px;">Founding & Full-stack Engineer</strong> <span style="font-size:15px;">· TypeScript / React / Node.js · <strong>5+ years xp</strong></span></p>

<p align="left">
<a href="mailto:wiegandtjulien2@gmail.com"><img src="https://img.shields.io/badge/Email-wiegandtjulien2%40gmail.com-4F46E5?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://calendar.app.google/CQjuoc67hZe4452G8"><img src="https://img.shields.io/badge/Book%20a%20meeting-4285F4?style=for-the-badge&logo=googlecalendar&logoColor=white" /></a>
<a href="https://github.com/Julien-Wiegandt"><img src="https://img.shields.io/badge/GitHub-Full%20résumé%20here-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

Founding Engineer & Co-founder of an **AI SaaS** adopted by **PayFit, Canva & Notion**. Comfortable across the **full stack**, from system design and API architecture to UI animations and product quality. I write **strict TypeScript**, care about **type-safe end-to-end systems**, and ship products that hold at scale.


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Briefcase.png" alt="Experience" width="22" /> Experience

- **Founding Engineer & Co-founder · [KAWAAK](https://kawaak.com)** · `Nov. 2024 → Present`
  AI-powered LinkedIn content SaaS, built from scratch with a team of 3.
  - **+23K users · +€200K ARR · adopted by PayFit, Canva, Notion · 4.8/5 (150+ reviews)**
  - Full-stack architecture: NX monorepo, React / Vite (strict TS), Node / Express / Zod type-safe backend, MongoDB + Redis + BullMQ
  - Multi-LLM orchestration (OpenAI, Anthropic) · Clerk auth · Stripe + PayPal · AWS · Sentry / PostHog / Mixpanel
  - End-to-end ownership: architecture, code review, deployment, observability, user support

- **Founder & CEO · [FOREVR](https://www.forevr.fr)** · `2025 → Present`
  Digital memorial platform where families preserve and share memories (photos, videos, audio) through a QR code engraved on a plexiglass plaque. Built with Next.js / React / TypeScript.

- **Founder & CEO · [KEYPOP](https://www.keypop.io)** · `2023 → Present`
  Desktop app (Electron) and Chrome extension that bind AI prompts to keyboard shortcuts.

- **Full-stack Engineer · [WAALAXY](https://www.waalaxy.com)** · `May 2022 → Nov. 2024`
  LinkedIn prospecting platform, **+1M users**, team of 16 engineers.
  - Built **vector-search lead discovery (Pinecone)** into the onboarding flow, lifting **conversion by +80%** (validated via A/B testing)
  - Shipped an **email prospecting service** that **increased 10x email send volume** + **native HubSpot integration**
  - High-throughput micro-services architecture: event-driven (Kafka), MongoDB, containerized deployment

- **Front-end React Developer · CODÉIN** · `Jun. 2021 → Aug. 2021`
  Built **90% of the new web interface** for [OPPBTP](https://www.oppbtp.com/)'s personnel management tool in React TypeScript.


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Hammer%20and%20Wrench.png" alt="Stack" width="22" /> Technical stack

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
      <h4 align="center">Practices</h4>
    </td>
    <td>
      <img src="https://img.shields.io/badge/Monorepo_NX-143055?style=flat-square&logo=nx&logoColor=white" />
      <img src="https://img.shields.io/badge/Continuous_Delivery-0A0A0A?style=flat-square" />
      <img src="https://img.shields.io/badge/Code_Review-4F46E5?style=flat-square" />
      <img src="https://img.shields.io/badge/Web_Scraping-FF6B35?style=flat-square" />
    </td>
  </tr>
</table>


### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Graduation%20Cap.png" alt="Graduation Cap" width="22" height="22" /> Education

- **M.Sc. Software Engineering** · University of Sherbrooke (Québec, Canada) *(double degree)* · 2021–2022
- **Engineering Degree, CS & Management** · Polytech Montpellier *(double degree)* · 2019–2022
- **2-year Computer Science Degree (DUT)** · IUT de Blagnac · 2017–2019

### <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Globe%20Showing%20Europe-Africa.png" alt="Languages" width="22" height="22" /> Languages

🇫🇷 **French** · Native &nbsp;·&nbsp; 🇬🇧 **English** · C1 / TOEIC 910
