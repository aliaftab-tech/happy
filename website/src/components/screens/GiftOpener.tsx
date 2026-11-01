import React from 'react';
import { useApp } from '../../context';
import Images from '../../assets/images';

export const GiftOpener: React.FC = () => {
  const { setScreen } = useApp();

  return (
    <div 
      data-screen="gift"
      className="flex-1 flex flex-col items-center justify-center p-6 text-center select-none cursor-pointer"
      onClick={() => setScreen('teaser')}
    >
      <div className="relative group transition-transform duration-300 hover:scale-105 active:scale-95">
        <img
          src={Images.introGiftBox}
          alt="Birthday Surprise Gift Box"
          className="w-64 h-64 sm:w-72 sm:h-72 object-contain drop-shadow-[0_20px_30px_rgba(0,0,0,0.5)]"
        />
      </div>

      <p className="mt-8 font-serif text-2xl font-light tracking-wide text-white drop-shadow-md animate-pulse">
        Click to open it
      </p>
    </div>
  );
};

export default GiftOpener;
