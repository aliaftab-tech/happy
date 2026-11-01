import React, { useRef } from 'react';
import confetti from 'canvas-confetti';
import { useApp } from '../../context';
import Images from '../../assets/images';
import PillButton from '../common/PillButton';

interface WishCakeScreenProps {
  onBlow?: () => void;
  onDone?: () => void;
}

export const WishCakeScreen: React.FC<WishCakeScreenProps> = ({
  onBlow,
  onDone,
}) => {
  const { setScreen, isCandleBlown, blowCandles } = useApp();
  const feastRef = useRef<HTMLDivElement>(null);

  const handleBlow = () => {
    blowCandles();

    // Full-screen celebratory confetti particle burst
    confetti({
      particleCount: 90,
      spread: 70,
      origin: { y: 0.6 },
      colors: ['#fc7272', '#f9588e', '#ffbe3b', '#ffffff', '#ac5150'],
    });

    // Multi-angle secondary bursts for festival effect
    setTimeout(() => {
      confetti({
        particleCount: 50,
        angle: 60,
        spread: 55,
        origin: { x: 0.1, y: 0.7 },
        colors: ['#fc7272', '#ffbe3b', '#ffffff'],
      });
      confetti({
        particleCount: 50,
        angle: 120,
        spread: 55,
        origin: { x: 0.9, y: 0.7 },
        colors: ['#f9588e', '#ffbe3b', '#ffffff'],
      });
    }, 250);

    // Candle blow gentle whoosh audio effect via Web Audio API
    try {
      const AudioCtx =
        window.AudioContext ||
        (window as unknown as { webkitAudioContext: typeof AudioContext })
          .webkitAudioContext;
      if (AudioCtx) {
        const ctx = new AudioCtx();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(320, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(70, ctx.currentTime + 0.3);
        gain.gain.setValueAtTime(0.25, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.3);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.32);
      }
    } catch {
      // Audio context fallback
    }

    if (onBlow) onBlow();
  };

  const handleDone = () => {
    if (onDone) onDone();
    else setScreen('menu');
  };

  return (
    <div
      data-screen="cake"
      className="flex-1 flex flex-col items-center justify-between py-6 px-4 text-center overflow-y-auto"
    >
      {!isCandleBlown ? (
        <>
          <div className="w-full mt-2">
            <h1 className="font-serif text-2xl sm:text-3xl text-white tracking-wide flex items-center justify-center gap-2">
              <span>🌸</span> MAKE A WISH MY LOVE <span>🌸</span>
            </h1>
          </div>

          <div className="my-auto py-4 relative flex flex-col items-center">
            {/* Cake with authentic candle flames */}
            <div className="relative inline-block">
              <img
                src={Images.wishCakeLit}
                alt="Lit Birthday Cake"
                className="w-72 h-auto max-h-72 object-contain mx-auto drop-shadow-2xl select-none transition-transform hover:scale-105"
              />
            </div>
          </div>

          <div className="w-full flex items-center justify-center mb-6">
            <PillButton
              variant="primary"
              onClick={handleBlow}
              className="w-48 text-lg font-medium"
            >
              Blow
            </PillButton>
          </div>
        </>
      ) : (
        /* Celebration Reveal & Bakery Feast (Frames 021 - 026) */
        <div className="w-full flex flex-col items-center">
          {/* Header Frame 021-023 */}
          <div className="relative w-full pt-2 pb-4 text-center">
            <div className="absolute top-0 right-4 text-2xl animate-bounce">
              🐼❤️
            </div>
            <h1 className="font-calligraphic text-4xl sm:text-5xl text-white tracking-wide drop-shadow-md">
              Happy Birthday
            </h1>
            <div className="font-display text-xs sm:text-sm tracking-widest text-[#f06272] mt-1 font-semibold uppercase">
              MY LOVE
            </div>
          </div>

          {/* Celebration Luxury Cake with Side Balloons */}
          <div className="relative my-2 w-full flex items-center justify-center">
            {/* Left Balloon Bouquet */}
            <div className="absolute left-2 top-2 text-2xl sm:text-3xl animate-bounce">
              🎈
            </div>
            {/* Right Balloon Bouquet */}
            <div className="absolute right-2 top-2 text-2xl sm:text-3xl animate-bounce [animation-delay:500ms]">
              🎈
            </div>

            <img
              src={Images.birthdayCakeFancy}
              alt="Celebration Cake"
              className="w-56 h-auto max-h-56 object-contain mx-auto drop-shadow-2xl transition-transform hover:scale-105"
            />
          </div>

          {/* Pinned Deckled Greeting Note (Frame 021-023) */}
          <div className="relative my-4 w-11/12 max-w-[340px] bg-parchment-note-bg text-parchment-note-text rounded-lg p-5 shadow-xl border border-amber-200/60 transform -rotate-1">
            {/* Pink Washi Tape Pinning at Top */}
            <div
              className="absolute -top-3 left-1/2 -translate-x-1/2 w-16 h-6 rounded-sm opacity-90 shadow-sm"
              style={{
                background:
                  'repeating-linear-gradient(45deg, #fc7272, #fc7272 6px, #f9588e 6px, #f9588e 12px)',
              }}
            />

            <div className="font-serif text-center text-sm sm:text-base leading-relaxed tracking-wide font-medium pt-1">
              <p className="text-base sm:text-lg">Today is your day</p>
              <p className="italic my-1 text-lg sm:text-xl text-[#9b1836] font-bold">
                Dear Iman Fatima
              </p>
              <p>Have an amazing</p>
              <p>year ahead</p>
            </div>

            {/* Accents: Flower sticker on bottom left, pink stamp on bottom right */}
            <div className="absolute -bottom-2 -left-2 text-xl select-none">
              🌷🌸
            </div>
            <div className="absolute -bottom-2 -right-2 w-6 h-7 bg-pink-200 border border-pink-400 rounded-sm flex items-center justify-center text-[10px] text-pink-700 font-bold shadow-sm">
              🎂
            </div>
          </div>

          {/* Comfort Food Bakery Feast Section (Frames 024-026) */}
          <div
            ref={feastRef}
            className="w-full mt-6 pt-6 pb-8 px-4 rounded-3xl bg-secondary/90 backdrop-blur-sm border border-pink-400/20 shadow-2xl flex flex-col items-center"
          >
            {/* 70s retro bubble font heading: "Let's eat CAKE!" 🍰 in pink #fa75a2 */}
            <div className="text-center my-2">
              <h2 className="font-bubble text-3xl sm:text-4xl text-[#fa75a2] tracking-wider drop-shadow-sm flex items-center justify-center gap-2 font-bold">
                Let's eat CAKE! 🍰
              </h2>
            </div>

            {/* Illustration: Peach & Goma eating strawberry shortcake */}
            <div className="my-3 py-2">
              <img
                src={Images.bearPandaEatingCake}
                alt="Peach and Goma eating cake"
                className="w-64 h-auto max-h-48 object-contain mx-auto drop-shadow-lg"
              />
            </div>

            {/* Action button: "I Am Full" */}
            <div className="w-full flex items-center justify-center mt-4">
              <PillButton
                variant="accent"
                onClick={handleDone}
                className="w-48 text-base shadow-pill"
              >
                I Am Full
              </PillButton>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default WishCakeScreen;
