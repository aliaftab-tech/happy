import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { useApp } from '../../context';
import Images from '../../assets/images';

export const GiftOpener: React.FC = () => {
  const { setScreen, playMusic } = useApp();
  const [isOpening, setIsOpening] = useState(false);

  const handleOpen = () => {
    setIsOpening(true);
    void playMusic();
    setTimeout(() => {
      setScreen('teaser');
    }, 450);
  };

  return (
    <div 
      data-screen="gift"
      className="flex-1 flex flex-col items-center justify-center p-6 text-center select-none cursor-pointer"
      onClick={handleOpen}
    >
      <div className="mb-6">
        <p className="font-calligraphic text-3xl sm:text-4xl text-pink-200 drop-shadow-md">
          A Gift For My Wife
        </p>
        <p className="font-serif text-xl sm:text-2xl text-white font-semibold mt-1 tracking-wide">
          Iman Fatima ♥
        </p>
      </div>

      <motion.div 
        animate={isOpening ? { scale: [1, 1.25, 0.9], rotate: [0, -8, 8, 0], opacity: [1, 1, 0.8] } : {}}
        transition={{ duration: 0.45 }}
        className="relative group transition-transform duration-300 hover:scale-105 active:scale-95"
      >
        <img
          src={Images.introGiftBox}
          alt="Birthday Surprise Gift Box for Iman Fatima"
          className="w-64 h-64 sm:w-72 sm:h-72 object-contain drop-shadow-[0_20px_35px_rgba(0,0,0,0.6)]"
        />
      </motion.div>

      <p className="mt-8 font-serif text-2xl font-light tracking-wide text-white drop-shadow-md animate-pulse">
        Click to open it 🎁
      </p>
    </div>
  );
};

export default GiftOpener;
