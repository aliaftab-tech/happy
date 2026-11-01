# E2E Test Infra: Romantic Birthday Surprise Web Application

## Test Philosophy
- Opaque-box, requirement-driven. No dependency on implementation design.
- Methodology: Category-Partition + BVA + Pairwise + Workload Testing across Tiers 1-4.
- Derived strictly from `d:\happy birthday\.agents\teamwork\ORIGINAL_REQUEST.md` and reference video ground truth.

## Feature Inventory
| # | Feature | Source (requirement) | Tier 1 | Tier 2 | Tier 3 |
|---|---------|---------------------|:------:|:------:|:------:|
| 1 | WhatsApp Chat Link Preview | ORIGINAL_REQUEST §R1 & Frame 001 | 5 | 5 | ✓ |
| 2 | Gift Box Opener Screen | ORIGINAL_REQUEST §R1 & Frame 003 | 5 | 5 | ✓ |
| 3 | Surprise Teaser Question | ORIGINAL_REQUEST §R1 & Frame 005 | 5 | 5 | ✓ |
| 4 | Rejection Tease Branch ("Why did you click No") | ORIGINAL_REQUEST §R1 & Frame 007 | 5 | 5 | ✓ |
| 5 | 2×2 Main Hub Menu ("THESE ARE FOR YOU CUTIE") | ORIGINAL_REQUEST §R1 & Frame 015 | 5 | 5 | ✓ |
| 6 | Interactive Wish Cake (Candle Wishing) | ORIGINAL_REQUEST §R1 & Frame 018 | 5 | 5 | ✓ |
| 7 | Birthday Celebration & Confetti Reveal | ORIGINAL_REQUEST §R1 & Frame 021 | 5 | 5 | ✓ |
| 8 | Comfort Food Bakery Feast ("Let's eat CAKE!") | ORIGINAL_REQUEST §R1 & Frame 024 | 5 | 5 | ✓ |
| 9 | Scrapbook Memories Polaroid Gallery | ORIGINAL_REQUEST §R1 & Frame 027 | 5 | 5 | ✓ |
| 10 | Romantic Memory Quote & Vignette | ORIGINAL_REQUEST §R1 & Frame 033 | 5 | 5 | ✓ |
| 11 | Spinning Vinyl Audio Player | ORIGINAL_REQUEST §R1 & Frame 037 | 5 | 5 | ✓ |
| 12 | Special Birthday Love Letter (Verbatim) | ORIGINAL_REQUEST §R1 & Frame 038 | 5 | 5 | ✓ |
| 13 | "I Love You" Teddy Bear Finale | ORIGINAL_REQUEST §R1 & Frame 045 | 5 | 5 | ✓ |
| 14 | Finale Navigation (Home Button) | ORIGINAL_REQUEST §R1 & Frame 047 | 5 | 5 | ✓ |
| 15 | Kinetic Typography & Micro-interactions | ORIGINAL_REQUEST §R1 & Frames 005, 015 | 5 | 5 | ✓ |
| 16 | Audio Soundtrack & Sound Effects | ORIGINAL_REQUEST §R1 & Audio Stream | 5 | 5 | ✓ |
| 17 | Responsive Shell & Ambient Desktop Backdrop | ORIGINAL_REQUEST §R1 & Frames 001-047 | 5 | 5 | ✓ |
| 18 | Graphic Asset Pipeline & Visual Fidelity | ORIGINAL_REQUEST §R1 & R3 | 5 | 5 | ✓ |

## Test Architecture
- **Test Runner**: Node/Python automated test harness executing Playwright/headless browser tests.
- **Pass/Fail Semantics**: All test assertions must pass with exit code 0; browser console must have zero unhandled errors.
- **Screenshots & Visual Regression**: Captures 390×844 and 720×1280 mobile viewport screenshots of each state and compares against benchmark frames in `d:\happy birthday\video_frames`.

## Real-World Application Scenarios (Tier 4)
| # | Scenario | Features Exercised | Complexity |
|---|----------|--------------------|------------|
| 1 | Full Happy Path Walkthrough | WhatsApp -> Gift -> Teaser ("Yes") -> Menu -> Cake (Wish & Feast) -> Gallery -> Letter (with Vinyl music) -> Finale -> Home | High |
| 2 | Playful Rejection & Recovery | Teaser -> "No Thanks" -> Rejection Screen (Gun Panda) -> "Try Again" -> Teaser -> "Yes Sure" -> Menu | Medium |
| 3 | Audio & Vinyl Spin Toggle State Cycle | Letter Screen -> Start Vinyl audio -> Scroll letter -> Pause vinyl -> Resume audio -> Return to Menu | Medium |
| 4 | Rapid Inter-Screen Switching & Breadcrumbs | Menu -> Cake -> I Am Full -> Menu -> Memories -> Back -> Menu -> Letter -> Back -> Menu | Medium |
| 5 | Candle Blow & Particle Celebration Sequence | Cake Screen -> Candle flame flicker -> Click "Blow" -> Particles explosion -> Drip cake & Macarons reveal -> Scroll feast | High |

## Coverage Thresholds
- Tier 1: ≥5 per feature (18 features × 5 = 90 tests)
- Tier 2: ≥5 per feature (18 features × 5 = 90 tests)
- Tier 3: Pairwise combinations of all major screen transitions and states (≥18 tests)
- Tier 4: ≥5 realistic user walkthrough application scenarios
- **Total Minimum Test Count: ≥203 test cases**
