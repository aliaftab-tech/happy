# Project: Romantic Birthday Surprise Interactive Web Application

## Architecture
- **Framework**: Vite + React 19 + TypeScript inside `d:\happy birthday\website`.
- **Styling**: Tailwind CSS v3 with semantic color tokens (`#810503` crimson burgundy, `#fc7272` coral pill, `#a7302c` terracotta squircle, `#f7a1c4` stationery pink, etc.) and custom font utilities.
- **Typography**: Google Fonts imports (`Playfair Display`, `Great Vibes`, `Syncopate`, `Fredoka`, `Caveat`, `Nunito`).
- **State Management & Routing**: Centralized declarative state machine via React Context (`activeScreen`: 'whatsapp' | 'gift' | 'teaser' | 'rejection' | 'menu' | 'cake' | 'memories' | 'letter' | 'finale') with `framer-motion` `AnimatePresence` for smooth animated screen transitions.
- **Media & Effects**: HTML5 Audio controller bound to interactive spinning vinyl record player; `canvas-confetti` for celebratory particle burst.
- **Viewport**: Mobile-first 9:16 layout centered on desktop with ambient burgundy vignette glow; native touch-friendly layout on mobile devices.

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | WhatsApp Chat Link Preview | Simulated messaging bubble preview with gift graphic, domain `dua-digitals.my.canva.site`, and "I made a gift for you" copy | M2 | Frame 001 |
| 2 | Gift Box Opener | Centered 3D sky-blue gift box tied with pink polka-dot ribbon and "Click to open it" tap prompt | M2 | Frames 003-004 |
| 3 | Surprise Gatekeeper Screen | "Do you want to see your Surprise" headline with typewriter effect, Peach & Goma cuddle illustration, "Yes Sure" & "No Thanks" buttons | M2 | Frames 005-006 |
| 4 | Rejection Tease Branch | "Why did you click No" arched heading with animated gun panda pointing at scared bear, and "Try Again" return button | M2 | Frames 007-009 |
| 5 | 2×2 Main Hub Menu | "THESE ARE FOR YOU CUTIE" 3-line kinetic typography with 4 squircle cards (Cake, Camera, Bottle, Gift) | M2 | Frames 015-017 |
| 6 | Interactive Wish Cake | "MAKE A WISH MY LOVE" heading with flowers, 2-tier white/pink cake with 3 flickering candles, and "Blow" action button | M3 | Frames 018-020 |
| 7 | Birthday Celebration Reveal | Candle blow animation, full-screen particle confetti blast, luxury drip cake with macarons reveal, balloons, and pinned deckled greeting note | M3 | Frames 021-023 |
| 8 | Comfort Food Bakery Feast | "Let's eat CAKE!" 70s retro bubble font, Peach & Goma bear and panda eating strawberry shortcake slices, and "I Am Full" return button | M3 | Frames 024-026 |
| 9 | Scrapbook Polaroid Gallery | "Captured Memories" cursive heading, asymmetrical Polaroid photo collage with washi tape, metal paperclip, flower and camera stickers | M4 | Frames 027-032 |
| 10 | Romantic Memory Quote & Vignette | "Memories are the only things that time can't erase." quote, circular couple vignette, and pink circular Back arrow button | M4 | Frames 033-034 |
| 11 | Spinning Vinyl Record Player | Realistic black vinyl record with orange label, "Play this while you are reading" curved arrow, play/pause rotation synced with audio | M4 | Frames 037-038 |
| 12 | Special Birthday Love Letter | Pastel pink stationery card with verbatim 3-paragraph birthday letter, stickers, and coral "Back" pill button | M4 | Frames 038-042 |
| 13 | "I Love You" Teddy Bear Finale | Calligraphic "I love you" title, floating envelope with red heart seal, cream teddy bear with heart, and floating balloons | M4 | Frames 045-047 |
| 14 | Finale Navigation | Outlined vector Home icon button (`🏠`) navigating back to Main Hub or Welcome | M4 | Frame 047 |
| 15 | Kinetic Typography & Micro-interactions | Letter-by-letter typewriter reveals on headings, pill button hover lift / tap compress, card hover scales | M2 | Frames 005, 015 |
| 16 | Audio Soundtrack & Sound Effects | Looping romantic soundtrack (`bgm.mp3`) with play/pause sync, audio context safety, and candle blow sound effect | M4 | MP4 audio & bgm.mp3 |
| 17 | Responsive Shell & Ambient Backdrop | Mobile-first 9:16 portrait viewport shell with desktop ambient burgundy vignette glow | M1 | Frames 001-047 |
| 18 | Curated Graphic Asset Pipeline | 20 curated PNG graphic assets and audio bundled into `src/assets/` | M1 | Explorer 1 Asset Pack |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Foundation & Core Scaffold | Vite + React 19 + Tailwind setup, design tokens, Google fonts, Mobile Shell, AppStateContext, asset staging | none | IN_PROGRESS |
| M2 | Intro, Teaser & Navigation Hub | WhatsApp preview, Gift opener, Surprise teaser, Rejection tease, and 2×2 Main Hub Menu | M1 | PLANNED |
| M3 | Wish Cake, Celebration & Bakery Feast | Candle blowing, confetti blast, celebration drip cake reveal, deckled note, and Peach & Goma cake feast | M2 | PLANNED |
| M4 | Scrapbook Memories, Love Letter & Finale | Polaroid gallery, spinning vinyl player, verbatim love letter, "I love you" finale, audio system integration | M2 | PLANNED |
| M5 | Final E2E Test Suite & Coverage Hardening | 100% pass of E2E test suite (Tiers 1-4), Playwright browser screenshot automation, visual diff against reference frames, adversarial Tier 5 hardening | M3, M4, TEST_READY | PLANNED |

## Interface Contracts
### AppStateContext ↔ Screens
- `activeScreen`: `'whatsapp' | 'gift' | 'teaser' | 'rejection' | 'menu' | 'cake' | 'memories' | 'letter' | 'finale'`
- `setScreen(screen: ScreenType): void`
- `isCandleBlown: boolean`, `blowCandles(): void`
- `isPlayingMusic: boolean`, `toggleMusic(): void`
- `audioRef`: React.RefObject<HTMLAudioElement>

### Component Event Handlers
- `SurpriseTeaser`: `onAccept() => setScreen('menu')`, `onReject() => setScreen('rejection')`
- `Rejection`: `onRetry() => setScreen('teaser')`
- `MainMenuHub`: `onSelectCard(cardId: 'cake' | 'memories' | 'letter' | 'finale') => setScreen(cardId)`
- `WishCake`: `onBlow() => triggerCelebration()`, `onDone() => setScreen('menu')`
- `MemoriesGallery`: `onBack() => setScreen('menu')`
- `LoveLetter`: `onBack() => setScreen('menu')`, `onToggleVinyl() => toggleMusic()`
- `Finale`: `onHome() => setScreen('menu')`

## Code Layout
```
d:\happy birthday\website\
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── postcss.config.js
├── public\
│   └── favicon.ico
├── src\
│   ├── main.tsx
│   ├── App.tsx
│   ├── index.css
│   ├── assets\
│   │   ├── images\          # 20 curated PNG assets
│   │   └── audio\           # bgm.mp3 & blow sound
│   ├── context\
│   │   └── AppContext.tsx   # Global screen & audio state
│   ├── components\
│   │   ├── common\
│   │   │   ├── MobileContainer.tsx   # 9:16 mobile frame with desktop backdrop
│   │   │   ├── PillButton.tsx        # Reusable coral/candy pink pill button
│   │   │   └── FloatingHearts.tsx    # Ambient heart particle background
│   │   └── screens\
│   │       ├── WhatsAppPreview.tsx   # Screen 0
│   │       ├── GiftOpener.tsx        # Screen 1
│   │       ├── SurpriseTeaser.tsx    # Screen 2
│   │       ├── RejectionScreen.tsx   # Screen 2-Alt
│   │       ├── MainMenuHub.tsx       # Screen 3
│   │       ├── WishCakeScreen.tsx    # Screen 4A
│   │       ├── MemoriesScreen.tsx    # Screen 4B
│   │       ├── LoveLetterScreen.tsx  # Screen 4C
│   │       └── FinaleScreen.tsx      # Screen 4D
└── scripts\
    ├── extract_reference_frames.py
    └── verify_visual_fidelity.py
```
