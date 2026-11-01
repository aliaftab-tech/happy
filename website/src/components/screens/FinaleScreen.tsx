import React from 'react';
import { useApp } from '../../context';
import Images from '../../assets/images';
import { Home } from 'lucide-react';

interface FinaleScreenProps {
  onHome?: () => void;
}

export const FinaleScreen: React.FC<FinaleScreenProps> = ({ onHome }) => {
  const { setScreen } = useApp();

  const handleHome = () => {
    if (onHome) onHome();
    else setScreen('menu');
  };

  return (
    <div
      data-screen="finale"
      className="flex-1 flex flex-col items-center justify-between py-8 px-6 text-center overflow-y-auto"
    >
      {/* Top Floating Envelope with Red Heart Wax Seal (Frames 045 - 047) */}
      <div className="w-full flex items-center justify-center mt-2 mb-1">
        <div className="relative animate-bounce [animation-duration:3s]">
          <img
            src={Images.letterEnvelope}
            alt="Letter Envelope with Heart Wax Seal"
            className="w-28 h-auto object-contain drop-shadow-lg transform -rotate-3 hover:rotate-0 transition-transform"
          />
        </div>
      </div>

      {/* Calligraphic "I love you" Title */}
      <div className="w-full my-2">
        <h1 className="font-calligraphic text-5xl sm:text-6xl text-white tracking-wider drop-shadow-md">
          I love you
        </h1>
        <p className="font-serif text-2xl sm:text-3xl text-pink-200 mt-1 drop-shadow-md font-semibold tracking-wide">
          Iman Fatima ♥
        </p>
      </div>

      {/* Centerpiece: Teddy Bear with Heart & Floating Balloons on Sides */}
      <div className="relative my-auto py-4 w-full flex items-center justify-center">
        {/* Left Floating Heart Balloon Bouquet */}
        <div className="absolute left-4 top-2 text-3xl animate-float">
          🎈
        </div>
        <div className="absolute left-8 bottom-4 text-xl opacity-80 animate-float [animation-delay:1.5s]">
          💖
        </div>

        {/* Right Floating Heart Balloon Bouquet */}
        <div className="absolute right-4 top-4 text-3xl animate-float [animation-delay:1s]">
          🎈
        </div>
        <div className="absolute right-8 bottom-2 text-xl opacity-80 animate-float [animation-delay:2.5s]">
          💕
        </div>

        {/* Teddy Bear Holding Heart */}
        <div className="flex flex-col items-center">
          <img
            src={Images.teddyBearHeart}
            alt="Teddy bear with heart"
            className="w-56 h-auto max-h-56 object-contain mx-auto drop-shadow-2xl animate-pulse [animation-duration:2.5s]"
          />
          <p className="mt-3 font-serif text-lg sm:text-xl text-pink-200 drop-shadow font-medium">
            Always & Forever Mine, Iman Fatima ♥
          </p>
        </div>
      </div>

      {/* Outlined Vector Home Icon Button Centered at Bottom */}
      <div className="w-full flex items-center justify-center mb-4">
        <button
          type="button"
          onClick={handleHome}
          className="w-14 h-14 rounded-full bg-white/20 hover:bg-white/30 text-white flex items-center justify-center transition-all duration-200 border border-white/40 shadow-lg active:scale-95 cursor-pointer focus:outline-none"
          aria-label="Back to main menu"
        >
          <Home size={26} />
        </button>
      </div>
    </div>
  );
};

export default FinaleScreen;
