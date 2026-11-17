# Avikto — High-Level Architecture Overview

> **What it is:** A unified SaaS platform that merges **Case Manager** and **ConnectNx CRM** into one Next.js application, sold as plug-and-play modules licensed per organization.

---

## 1. Big Picture

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                            case-manager-ui (Monorepo)                        │
│                      pnpm workspaces  ·  Turborepo orchestration             │
│                                                                              │
│  ┌─────────────────────────┐    ┌────────────────────────────────────────┐   │
│  │      apps/avikto        │    │            packages/                   │   │
│  │  (Next.js 16 App Router)│    │  ui · api · analytics · utils · types  │   │
│  └─────────────────────────┘    └────────────────────────────────────────┘   │
│                                                                              │
│  ┌────────────┐  ┌──────────────┐  ┌─────────────┐  ┌────────────────────┐  │
│  │  pipelines/│  │    infra/    │  │   scripts/  │  │       docs/        │  │
│  │  CI/CD     │  │  Kubernetes  │  │  lint/guard │  │  architecture docs │  │
│  └────────────┘  └──────────────┘  └─────────────┘  └────────────────────┘  │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Monorepo Layout

```
case-manager-ui/
├── apps/
│   ├── avikto/              # Main product — Next.js 16 (App Router)
│   └── docs/                # (Placeholder) Future Docusaurus docs site
│
├── packages/
│   ├── ui/                  # @avikto/ui — shadcn/ui + Tailwind v4 design system
│   ├── api/                 # @avikto/api — RTK Query base-query factory
│   ├── analytics/           # @avikto/analytics — event tracking abstraction
│   ├── utils/               # @avikto/utils — cross-app utility functions
│   ├── types/               # @avikto/types — shared TypeScript contract types
│   ├── eslint-config/       # Shared ESLint rules (design, forms, legacy, theme…)
│   └── typescript-config/   # Shared tsconfig bases
│
├── infra/
│   └── kubernetes/
│       ├── config/dev/      # Dev environment K8s manifests
│       └── config/qat/      # QA environment K8s manifests
│
├── pipelines/
│   ├── deploy.yaml          # Build & deploy (Azure DevOps)
│   ├── pr-validation.yaml   # PR gates — lint, typecheck, unit tests
│   ├── security.yaml        # Scheduled Trivy + ZAP security scans
│   └── playwright.yaml      # E2E test pipeline (not yet registered as ADO pipeline)
│
├── docs/
│   └── architecture/        # 10-document architecture decision record (ADR)
│       ├── 00-executive-summary.md
│       ├── 01-current-state.md
│       ├── 02-target-architecture.md
│       ├── 03-implementation-plan.md
│       ├── 04-risks-and-open-questions.md
│       ├── 05-plug-and-play-licensing.md
│       ├── 06-vertical-configurability.md
│       ├── 07-authiris-v2-impact.md
│       ├── 08-ui-migration.md
│       └── 09-execution-handoff.md
│
├── scripts/
│   ├── only-pnpm.js         # Rejects npm/yarn/bun at install time
│   └── check-us-english.mjs # Spelling consistency gate
│
├── turbo.json               # Turborepo task graph
├── pnpm-workspace.yaml      # Workspace members + single version catalog
└── package.json             # Root scripts & devDependencies
```

---

## 3. Technology Stack

| Layer | Technology |
|---|---|
| **Framework** | Next.js 16 (App Router, React 19, Server Components) |
| **Language** | TypeScript 7 (Go port) |
| **Monorepo** | pnpm 11 workspaces + Turborepo 2 |
| **Design System** | shadcn/ui (Radix UI primitives) + Tailwind CSS v4 |
| **Icons** | Phosphor Icons (`@phosphor-icons/react`) |
| **State Management** | Redux Toolkit + RTK Query + react-redux |
| **Data Fetching** | TanStack Query v5 (alongside RTK Query) |
| **Forms** | react-hook-form + zod |
| **Rich Text** | Lexical 0.52 |
| **Tables** | TanStack Table v9 |
| **Charts** | Recharts |
| **Maps** | Leaflet + react-leaflet |
| **Calendar** | FullCalendar (React adapter) |
| **DnD** | @dnd-kit |
| **Auth** | Authiris (identity service) + MSAL browser (Azure AD SSO) |
| **Error Tracking** | Sentry (Next.js SDK) |
| **Session Replay** | OpenReplay |
| **Notifications** | Sonner (toast) + STOMP WebSocket |
| **Testing** | Vitest + React Testing Library + MSW (unit), Playwright (E2E), Storybook 10 (component) |
| **CI/CD** | Azure DevOps Pipelines |
| **Container** | Docker + Kubernetes (dev & qat namespaces) |
| **Linting** | ESLint 10 (custom rule packs) + Prettier |
| **Versioning** | Changesets |

---

## 4. Application Architecture (`apps/avikto`)

### 4.1 Next.js App Router Structure

```
src/app/
├── (auth)/              # Unauthenticated flows
│   ├── login/
│   ├── sign-up/
│   ├── forgot-password/
│   ├── reset-password/
│   ├── verify-otp/
│   └── onboarding/
│
├── (public)/            # Public-facing customer-portal pages
│   ├── admissions/
│   ├── forms/
│   ├── inquiry/
│   ├── kb/              # Public knowledge base
│   ├── marketing/
│   ├── meet/
│   ├── customer-portal/
│   └── …
│
├── (protected)/         # Requires valid session
│   └── (dashboard)/
│       └── org/
│           └── [orgName]/   # Per-org workspace — all product modules live here
│               ├── home/
│               ├── cases/ (mycases/)
│               ├── contacts/  leads/  customers/  residents/
│               ├── crm-dashboard/
│               ├── marketing/
│               ├── analytics/  reports/
│               ├── automations/  workflows/  templates/
│               ├── knowledge/
│               ├── learning/
│               ├── scheduling/  appointments/
│               ├── tasks/  projects/
│               ├── inbox/  chats/  whatsapp/
│               ├── compliance/  insurance/
│               ├── admissions/  clinical-agreements/
│               ├── canvassing/  phone-banking/  outreach-events/
│               ├── operator-portal/  platform-admin/
│               ├── settings/
│               └── …
│
├── api/                 # Next.js API Route Handlers (server-side proxy)
│   ├── auth/            # Session cookie management
│   ├── config/          # App config endpoint
│   └── translate/       # Translation proxy
│
├── mcp/                 # MCP (Model Context Protocol) consent endpoint
└── oauth/               # OAuth callback handler
```

### 4.2 Source Directory Layers

```
src/
├── app/           # Next.js App Router — pages, layouts, API routes
├── modules/       # Feature modules (self-contained, contract-bounded)
├── components/    # Shared UI components (cross-module)
├── hooks/         # Shared React hooks
├── contexts/      # React context providers
├── providers/     # App-level providers (Auth, Theme, Query, etc.)
├── redux/         # Redux store, slices, RTK Query base API
├── overlays/      # Global drawers and modals (registered at app level)
├── data/          # Static config: themes, help docs, guided tours
├── utils/         # Domain utility functions
├── types/         # App-local TypeScript types
├── styles/        # Global CSS
├── assets/        # SVG icons, images
├── icons/         # Custom icon set
├── mocks/         # MSW request handlers (dev/test)
└── server/        # Server-only utilities
```

---

## 5. Module System

Each feature area is a **contract-bounded module**. UI structure lives in code (manifests); only facts (licenses, scopes) are remote data.

### Module Resolution Flow

```
┌─────────────────────┐    ┌────────────────────────┐    ┌────────────────────┐
│   Static Manifest   │    │    Org Licence Table    │    │   User Scopes      │
│  src/modules/*/     │    │  suite.org_module_      │    │  Authiris          │
│  manifest.tsx       │    │  license (backend DB)   │    │  getMyOrgPermissions│
└──────────┬──────────┘    └───────────┬────────────┘    └────────┬───────────┘
           │                           │                           │
           └───────────────────────────▼───────────────────────────┘
                              Module Resolution Engine
                           visibleModules = manifest ∩ licences ∩ scopes
                                           │
                              ┌────────────▼─────────────┐
                              │   Shell Navigation +      │
                              │   Route Tree Rendered     │
                              └──────────────────────────┘
```

### Module Catalog

| Domain | Modules |
|---|---|
| **Case Management** | `case-management`, `admissions`, `compliance`, `clinical-agreements` |
| **CRM** | `crm-core`, `crm-channels`, `crm-sales`, `crm-prospecting`, `crm-marketing`, `crm-orders`, `crm-insurance` |
| **Workforce** | `workforce-management`, `learning`, `scheduling` |
| **Outreach** | `field-canvassing`, `phone-banking`, `outreach-events` |
| **Customer** | `party-directory`, `party-journey`, `households`, `self-service-portal` |
| **Platform** | `automations`, `workflow-builder`, `decision-table`, `knowledge`, `tasks`, `solution-packs` |
| **Finance** | `inventory`, `asset-management` |

Each module exposes: `id`, `label`, `icon`, `requires[]`, `basePath`, `requiredScopes[]`, `nav[]`, `provides[]`, `settings[]`.

---

## 6. Authentication & Session Model

```
User ──► Avikto App ──► Authiris IdP
              │
              │  1. POST /login → idToken (identity, product-scoped)
              │  2. POST /api/auth/session → httpOnly cookie (server action)
              │  3. GET /user/product/{id}/organizations → orgs[]
              │  4. POST /access-token {organizationId} → accessToken (org-scoped)
              │  5. GET /user/.../organization/{orgId} → scopes[]
              │  6. GET /suite/licences?orgId → licensedModules[]
              │  7. Resolve: visibleModules = manifest ∩ licences ∩ scopes
              │
              └──► All API calls: Bearer accessToken + x-product-id + x-module headers
```

**Key design decisions:**
- Two tokens (idToken + accessToken), no refresh grant — session extended via re-auth modal
- One Authiris product registration covers all modules (no per-module registrations)
- `x-module` header enables gateway-level per-module license enforcement
- Sessions persist via Redux Persist to `localStorage`

---

## 7. Shared Packages

### `@avikto/ui` — Design System

Built on **shadcn/ui** (Radix UI primitives) with **Tailwind CSS v4**. Contains 60+ components (Button, DataTable, Dialog, Drawer, Form, Select, Calendar, etc.), all with Storybook stories and accessibility (a11y) tests.

- Import path: `@avikto/ui/components/<name>` (never from barrel exports)
- Tokens: CSS custom properties (`var(--…)`) — no hardcoded colors/spacing
- Themes: light, dark, high-contrast, and org-defined presets all supported

### `@avikto/api` — API Layer

RTK Query base-query factory that:
- Attaches `Bearer accessToken`, `x-product-id`, and `x-module` headers automatically
- Handles 401 → triggers re-auth modal flow
- Provides resilient retry logic (`resilientBaseQuery.ts`)

### `@avikto/analytics` — Event Tracking

Abstraction layer over analytics providers. Decouples business events from vendor SDKs.

### `@avikto/utils` — Shared Utilities

Date formatting (`date-fns` + temporal-polyfill), string operations, validation helpers, and other pure functions used across apps.

### `@avikto/types` — Shared Types

TypeScript contract types shared verbatim with the ConnectNx product (Authiris session, org, scope contracts).

---

## 8. State Management

```
┌──────────────────────────────────────────────────────┐
│                   Redux Store                        │
│                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │  features/  │  │  baseApi.ts  │  │  cache/    │  │
│  │  (slices)   │  │  RTK Query   │  │  persisted │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
│                                                      │
│  redux-persist → localStorage (user directory,       │
│                                 session, preferences)│
└──────────────────────────────────────────────────────┘

TanStack Query (server state) runs alongside RTK Query.
Both are invalidated on create / update / delete operations.
```

---

## 9. CI/CD & Infrastructure

### Pipeline Flow

```
PR Opened
   │
   ▼
pr-validation.yaml ──► lint → typecheck → unit tests → build
   │
   ▼ (merge to develop)
deploy.yaml ──► pnpm build → Docker image → push to ACR → K8s rollout
   │
   ├── Target: dev (auto)
   └── Target: qat (manual approval gate)

security.yaml (scheduled) ──► Trivy (dependency scan) + ZAP (DAST)
playwright.yaml            ──► Playwright E2E (run manually / on-demand)
```

### Docker

- `Dockerfile` — standard Next.js standalone output build
- `Dockerfile.prebuilt` — uses a pre-built `.next/` artifact (faster CI)

### Kubernetes

```
infra/kubernetes/config/
├── dev/   # Development namespace manifests
└── qat/   # QA/Test namespace manifests
```

---

## 10. Developer Conventions & Tooling

### Code Quality Gates

| Tool | Purpose |
|---|---|
| **ESLint 10** | Custom rule packs: `avikto-legacy-ui`, `avikto-styled`, `avikto-theme`, `avikto-ui-imports`, `avikto-design/*` |
| **Prettier** | Formatting — runs on commit via lint-staged |
| **TypeScript 7** | Strict type checking across the workspace |
| **Knip** | Dead code / unused export detection |
| **Commitlint** | Conventional commits enforced on `commit-msg` hook |
| **Husky** | Git hooks (`pre-commit` → lint-staged, `commit-msg` → commitlint) |
| **Changesets** | Versioning & changelog management |
| **check-us-english** | Enforces US English spelling in source files |

### Key Developer Rules

- **pnpm only** — `npm`, `yarn`, and `bun` are blocked by `scripts/only-pnpm.js`
- **Single version catalog** — all dependency versions declared once in `pnpm-workspace.yaml`, consumed as `catalog:` throughout
- **Branch from `develop`** — target `develop`; release branches are for certified production releases only
- **One PR per bug fix** — so each fix can be tested independently
- Run `pnpm lint`, `pnpm check-types`, `pnpm test:unit`, and `pnpm build` before opening a PR

### Design Conventions

- Forms → `AppForm` / `AppFormField` (react-hook-form + zod)
- Overlays for create/edit records → `CustomDrawer` (right-side, page not dimmed)
- Confirmations/short forms → `Dialog` (centered)
- Toasts → `toast` from `@/components/feedback/toast` (Sonner), one per action
- Loading → `Skeleton` (first load) / `Spin` / `Spinner` / `LoadingMark`
- Empty states → `EmptyState` (no data) vs. inline message (no results for filter)
- Dates → `@avikto/utils/date` with user timezone preference

---

## 11. Key Architectural Patterns

| Pattern | Implementation |
|---|---|
| **Module manifest system** | Each module = `manifest.tsx` (code), license = DB row (data) |
| **Contract-bounded modules** | `contract.ts` / `presentation.ts` per module — explicit public API |
| **Server / Client split** | Next.js Server Components for data fetching; Client Components for interactivity |
| **API proxy** | Next.js Route Handlers (`/api/*`) proxy backend calls, attach auth headers server-side |
| **Resilient data loading** | Error boundary + Retry button on failed loads; never auto-retry writes |
| **Dirty form guard** | Warn before leaving, disable Save until changed, block double-submit |
| **AI draft pattern** | AI output shown as editable preview; nothing saved until user accepts |
| **Responsive breakpoints** | 375 px / 768 px / 1280 px / 1920 px; tested at all four |
| **Accessibility** | Keyboard focus trap in overlays, `data-testid` on interactive elements, Storybook axe tests |
| **Multi-tenancy** | URL scheme `/{orgName}/...`; org-scoped access tokens; per-org module licensing |

---

## 12. Future Roadmap (Planned)

- **ConnectNx CRM** arrives as additional modules under `apps/avikto/src/modules/` (not a second app)
- **`apps/docs`** — Docusaurus docs site migration from standalone `AviktoDocs` repo
- **`apps/marketing`** — Astro marketing site migration from standalone `Avikto` repo
- **`packages/tokens`** — Design token package to be shared between product and marketing site
- **More verticals** — BEN/DETR government RFP and others, served via org-level configurability (no forking)

---

> **Architecture Decision Records:** Full rationale for every design decision lives in [`docs/architecture/`](../docs/architecture/README.md). Start at `09-execution-handoff.md` if picking this up cold.
