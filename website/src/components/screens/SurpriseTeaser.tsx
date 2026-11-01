import React from 'react';
import { useApp } from '../../context';
import Images from '../../assets/images';
import PillButton from '../common/PillButton';
import TypewriterText from '../common/TypewriterText';

interface SurpriseTeaserProps {
  onAccept?: () => void;
  onReject?: () => void;
}

export const SurpriseTeaser: React.FC<SurpriseTeaserProps> = ({
  onAccept,
  onReject,
}) => {
  const { setScreen } = useApp();

  const handleAccept = () => {
    if (onAccept) onAccept();
    else setScreen('menu');
  };

  const handleReject = () => {
    if (onReject) onReject();
    else setScreen('rejection');
  };

  return (
    <div 
      data-screen="teaser"
      className="flex-1 flex flex-col items-center justify-between py-12 px-6 text-center"
    >
      <div className="w-full mt-4 px-2">
        <h1 className="font-serif text-2xl sm:text-3xl font-normal text-white tracking-wide leading-snug drop-shadow-md break-words">
          <TypewriterText text="Do you want to see your Surprise, Iman Fatima?" cursor delay={0.12} />
        </h1>
      </div>

      <div className="my-auto py-4">
        <img
          src={Images.catsCuddle}
          alt="Peach and Goma cuddle"
          className="w-64 h-auto max-h-60 object-contain mx-auto drop-shadow-2xl transition-transform duration-300 hover:scale-105"
        />
      </div>

      <div className="w-full flex items-center justify-center gap-4 mb-4">
        <PillButton
          variant="primary"
          onClick={handleAccept}
          className="flex-1 max-w-[170px] transform hover:scale-105 active:scale-95 transition-transform"
        >
          Yes Sure
        </PillButton>
        <PillButton
          variant="primary"
          onClick={handleReject}
          className="flex-1 max-w-[170px] transform hover:scale-105 active:scale-95 transition-transform"
        >
          No Thanks
        </PillButton>
      </div>
    </div>
  );
};

export default SurpriseTeaser;
