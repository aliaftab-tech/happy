import React from 'react';
import { useApp } from '../../context';
import Images from '../../assets/images';
import PillButton from '../common/PillButton';

interface LoveLetterScreenProps {
  onBack?: () => void;
  onToggleVinyl?: () => void;
}

export const LoveLetterScreen: React.FC<LoveLetterScreenProps> = ({
  onBack,
  onToggleVinyl,
}) => {
  const { setScreen, isPlayingMusic, toggleMusic } = useApp();

  const handleBack = () => {
    if (onBack) onBack();
    else setScreen('menu');
  };

  const handleToggle = () => {
    if (onToggleVinyl) onToggleVinyl();
    else toggleMusic();
  };

  return (
    <div
      data-screen="letter"
      className="flex-1 flex flex-col py-6 px-4 text-center overflow-y-auto"
    >
      <h1 className="font-marker text-2xl text-white mb-2">
        I wrote something special for you
      </h1>

      {/* Vinyl record player widget & Envelope (Frames 037 - 038) */}
      <div className="flex items-center justify-center gap-6 my-2">
        <img
          src={Images.letterEnvelope}
          alt="Letter Envelope"
          className="w-16 h-auto object-contain transform -rotate-6 hover:rotate-0 transition-transform"
        />

        <div className="flex flex-col items-center">
          <button
            type="button"
            onClick={handleToggle}
            className="group relative cursor-pointer focus:outline-none"
            aria-label={isPlayingMusic ? 'Pause Music' : 'Play Music'}
          >
            <img
              src={Images.vinylRecord}
              alt="Vinyl record"
              className={`w-24 h-24 object-contain rounded-full shadow-xl transition-transform ${
                isPlayingMusic
                  ? 'animate-spin [animation-duration:4s]'
                  : 'group-hover:scale-105'
              }`}
            />
          </button>
        </div>
      </div>

      {/* Curved pink doodle arrow pointing to vinyl record */}
      <div className="flex items-center justify-center gap-2 my-1">
        <span className="font-marker text-xs sm:text-sm text-pink-200">
          Play this while you are reading
        </span>
        <svg
          viewBox="0 0 60 40"
          className="w-10 h-7 text-pink-400 select-none overflow-visible"
          fill="none"
          stroke="currentColor"
          strokeWidth="2.5"
          strokeLinecap="round"
          strokeLinejoin="round"
        >
          {/* Curved doodle loop and arrow pointing up-right toward vinyl */}
          <path d="M 5 28 C 15 35, 25 35, 35 22 C 40 15, 48 10, 55 8" />
          <path d="M 46 6 L 56 8 L 52 18" />
        </svg>
      </div>

      {/* Stationery Love Letter Card with Stickers (Frames 038 - 042) */}
      <div className="relative bg-paper-letter-bg text-paper-letter-body rounded-2xl p-5 my-3 text-left shadow-2xl border border-pink-300/50 font-serif leading-relaxed text-sm">
        {/* Top-Left Sticker: Kawaii bunny with cosmic halo ring */}
        <div className="absolute -top-3.5 -left-3 text-2xl select-none filter drop-shadow">
          🐰🪐
        </div>

        {/* Top-Right Sticker: Pink tulip flower */}
        <div className="absolute -top-3 -right-2 text-2xl select-none filter drop-shadow">
          🌷
        </div>

        {/* Header with Pink Ribbon Bow */}
        <div className="relative flex items-center justify-center mb-3">
          <h2 className="font-serif text-lg font-bold text-paper-letter-title text-center tracking-wide">
            HAPPY BIRTHDAY TO MY WIFE IMAN FATIMA
          </h2>
          <span className="ml-2 text-lg select-none">🎀</span>
        </div>

        {/* Floating smiling star sticker on left */}
        <div className="relative">
          <span className="absolute -left-3 top-1 text-base select-none animate-pulse">
            ⭐
          </span>
          <p className="mb-3 pl-2">
            Today is all about celebrating the most special person in my life — you, my beloved wife Iman Fatima. I hope this birthday brings you endless happiness, beautiful memories, and all the success and peace your heart desires. You deserve every smile, every blessing, and all the love this world has to offer.
          </p>
        </div>

        <p className="mb-3">
          Thank you for being my wife and such an amazing, loving partner. Your presence makes every day warmer, your smile brightens my whole world, and having you by my side is my greatest blessing. No matter how busy life gets, I hope you never forget how deeply loved and treasured you are.
        </p>

        <p className="mb-3">
          May this new chapter of your life be filled with tranquility, laughter, beautiful moments, and eternal happiness together. Keep shining, keep smiling, and never stop being the wonderful soul you are. 🌷
        </p>

        <div className="text-center font-bold text-xs text-paper-letter-title mt-4 pt-2 border-t border-pink-300/40">
          <p>HAPPY BIRTHDAY ONCE AGAIN, IMAN FATIMA.</p>
          <p className="mt-1">MAY YOUR DAY BE AS BEAUTIFUL AS YOUR HEART. 🎈 💌</p>
        </div>
      </div>

      {/* Back button */}
      <div className="w-full flex items-center justify-center mt-2 mb-4">
        <PillButton variant="accent" onClick={handleBack} className="w-44">
          Back
        </PillButton>
      </div>
    </div>
  );
};

export default LoveLetterScreen;
