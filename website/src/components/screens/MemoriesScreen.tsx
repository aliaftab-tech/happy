import React from 'react';
import { useApp } from '../../context';
import { MemoryPhotos } from '../../assets/memories';
import { ArrowLeft } from 'lucide-react';

interface MemoriesScreenProps {
  onBack?: () => void;
}

// SVG Metal Paperclip Component
const MetalPaperclip = ({ className = '' }: { className?: string }) => (
  <svg
    viewBox="0 0 24 24"
    className={`w-5 h-8 text-neutral-300 drop-shadow-md select-none pointer-events-none ${className}`}
    fill="none"
    stroke="currentColor"
    strokeWidth="2.2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48" />
  </svg>
);

export const MemoriesScreen: React.FC<MemoriesScreenProps> = ({ onBack }) => {
  const { setScreen } = useApp();

  const handleBack = () => {
    if (onBack) onBack();
    else setScreen('menu');
  };

  const polaroids = [
    {
      src: MemoryPhotos[0],
      caption: 'My Beautiful Wife Iman ♥',
      rotate: '-rotate-2',
      washi: true,
      sticker: '💕',
      stickerPos: '-top-2 -right-2',
      paperclip: false,
      paperclipPos: '',
    },
    {
      src: MemoryPhotos[1],
      caption: 'Pure Happiness Together ✨',
      rotate: 'rotate-3',
      washi: false,
      sticker: null,
      stickerPos: '',
      paperclip: true,
      paperclipPos: '-top-3 left-3',
    },
    {
      src: MemoryPhotos[2],
      caption: 'Forever My Queen 👑',
      rotate: '-rotate-1',
      washi: true,
      sticker: '💖',
      stickerPos: '-top-2 -right-1',
      paperclip: false,
      paperclipPos: '',
    },
    {
      src: MemoryPhotos[3],
      caption: 'Your Smile is My Home 🏡',
      rotate: 'rotate-2',
      washi: false,
      sticker: '🎈',
      stickerPos: '-bottom-2 -right-2',
      paperclip: true,
      paperclipPos: '-top-3 right-4',
    },
    {
      src: MemoryPhotos[4],
      caption: 'Unforgettable Moments 🌷',
      rotate: '-rotate-3',
      washi: true,
      sticker: '🌸',
      stickerPos: '-bottom-2 -left-2',
      paperclip: false,
      paperclipPos: '',
    },
    {
      src: MemoryPhotos[5],
      caption: 'Special Days With You 🤍',
      rotate: 'rotate-1',
      washi: false,
      sticker: '📷',
      stickerPos: '-top-3 -left-2',
      paperclip: true,
      paperclipPos: '-top-3 right-3',
    },
    {
      src: MemoryPhotos[6],
      caption: 'Every Second With You 💫',
      rotate: '-rotate-2',
      washi: true,
      sticker: '✨',
      stickerPos: '-bottom-1 -right-1',
      paperclip: false,
      paperclipPos: '',
    },
    {
      src: MemoryPhotos[7],
      caption: 'My Favorite Person 🌟',
      rotate: 'rotate-3',
      washi: false,
      sticker: '🌹',
      stickerPos: '-top-2 -right-2',
      paperclip: true,
      paperclipPos: '-top-3 left-4',
    },
    {
      src: MemoryPhotos[8],
      caption: 'Endless Love & Care 💓',
      rotate: '-rotate-1',
      washi: true,
      sticker: '🎀',
      stickerPos: '-bottom-2 -right-1',
      paperclip: false,
      paperclipPos: '',
    },
    {
      src: MemoryPhotos[9],
      caption: 'Always By Your Side 💍',
      rotate: 'rotate-2',
      washi: false,
      sticker: '🕊️',
      stickerPos: '-top-3 left-2',
      paperclip: true,
      paperclipPos: '-top-3 right-3',
    },
    {
      src: MemoryPhotos[10] || MemoryPhotos[0],
      caption: 'Forever & Always, Iman Fatima ♥',
      rotate: '-rotate-2',
      washi: true,
      sticker: '❤️',
      stickerPos: '-bottom-2 -left-2',
      paperclip: false,
      paperclipPos: '',
    },
  ];

  return (
    <div
      data-screen="memories"
      className="flex-1 flex flex-col py-6 px-4 text-center overflow-y-auto"
    >
      {/* Header */}
      <div className="w-full flex items-center justify-between mb-4">
        <button
          type="button"
          onClick={handleBack}
          className="w-10 h-10 rounded-full bg-btn-accent text-white flex items-center justify-center hover:opacity-90 active:scale-95 shadow-md border border-pink-300/40"
          aria-label="Back to menu"
        >
          <ArrowLeft size={20} />
        </button>
        <h1 className="font-calligraphic text-3xl sm:text-4xl text-white tracking-wide flex-1 text-center pr-10">
          Captured Memories
        </h1>
      </div>

      <p className="font-serif italic text-pink-200 text-sm mb-3">
        Every picture holds a thousand memories with you, Iman Fatima 💕
      </p>

      {/* Asymmetrical Scrapbook Polaroid Collage */}
      <div className="grid grid-cols-2 gap-4 py-3">
        {polaroids.map((p, idx) => (
          <div
            key={idx}
            className={`relative bg-white p-2 pb-4 rounded-lg shadow-polaroid transform transition-all duration-300 hover:scale-105 hover:z-10 ${p.rotate} flex flex-col justify-between`}
          >
            {/* Washi Tape Strip */}
            {p.washi && (
              <div
                className="absolute -top-2.5 left-1/2 -translate-x-1/2 w-12 h-5 rounded-xs opacity-85 shadow-xs z-10"
                style={{
                  background:
                    'repeating-linear-gradient(45deg, #f7a1c4, #f7a1c4 4px, #fbcfe8 4px, #fbcfe8 8px)',
                }}
              />
            )}

            {/* Metal Paperclip Accent */}
            {p.paperclip && (
              <div className={`absolute z-20 ${p.paperclipPos}`}>
                <MetalPaperclip />
              </div>
            )}

            {/* Flower / Camera / Heart Sticker */}
            {p.sticker && (
              <span
                className={`absolute z-20 text-lg select-none drop-shadow-sm ${p.stickerPos}`}
              >
                {p.sticker}
              </span>
            )}

            <div className="w-full aspect-[3/4] overflow-hidden rounded shadow-inner bg-neutral-100 flex items-center justify-center">
              <img
                src={p.src}
                alt={p.caption}
                className="w-full h-full object-cover rounded"
                loading="lazy"
              />
            </div>

            <p className="mt-2 font-serif text-[11px] sm:text-xs font-semibold text-neutral-700 tracking-tight leading-tight">
              {p.caption}
            </p>
          </div>
        ))}
      </div>

      {/* Romantic Memory Quote & Circular Vignette */}
      <div className="w-full my-6 flex flex-col items-center">
        {/* Cute Bunny Sticker */}
        <div className="text-3xl mb-2 animate-bounce">🐰✨</div>

        {/* Romantic Memory Quote */}
        <p className="font-serif text-lg sm:text-xl text-pink-100 max-w-[290px] leading-relaxed mx-auto drop-shadow font-medium">
          “Memories are the only things that time can't erase. I love you, Iman Fatima.” 💕
        </p>

        {/* Circular couple portrait vignette photo */}
        <div className="relative my-4 w-56 h-56 max-w-[220px] max-h-[220px] rounded-full p-1 bg-white/20 shadow-2xl backdrop-blur-xs flex items-center justify-center">
          <img
            src={MemoryPhotos[0]}
            alt="Iman Fatima & Me"
            className="w-full h-full object-cover rounded-full shadow-inner"
          />
          {/* Floating hearts around vignette */}
          <div className="absolute -bottom-1 -right-1 text-2xl animate-pulse">
            💖
          </div>
          <div className="absolute top-1 -left-2 text-xl">🌷</div>
        </div>

        {/* Circular pink Back arrow button at the bottom of the scrolled gallery */}
        <div className="mt-4 mb-3">
          <button
            type="button"
            onClick={handleBack}
            className="w-12 h-12 rounded-full bg-btn-accent hover:bg-btn-primary text-white flex items-center justify-center transition-all duration-200 active:scale-95 shadow-lg border border-pink-300/40"
            aria-label="Back to menu"
          >
            <ArrowLeft size={22} />
          </button>
        </div>
      </div>
    </div>
  );
};

export default MemoriesScreen;
