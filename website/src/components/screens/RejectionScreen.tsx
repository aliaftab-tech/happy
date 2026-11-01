import React from 'react';
import { motion } from 'framer-motion';
import { useApp } from '../../context';
import Images from '../../assets/images';
import PillButton from '../common/PillButton';

interface RejectionScreenProps {
  onRetry?: () => void;
}

export const RejectionScreen: React.FC<RejectionScreenProps> = ({ onRetry }) => {
  const { setScreen } = useApp();

  const handleRetry = () => {
    if (onRetry) onRetry();
    else setScreen('teaser');
  };

  return (
    <div 
      data-screen="rejection"
      className="flex-1 flex flex-col items-center justify-between py-12 px-6 text-center select-none"
    >
      <div className="w-full mt-4">
        <h1 className="sr-only">Why did you click No</h1>
        <motion.div
          animate={{
            rotate: [0, -2, 2, -1.5, 1.5, 0],
            scale: [1, 1.02, 0.99, 1.01, 1],
          }}
          transition={{
            duration: 2.8,
            repeat: Infinity,
            ease: 'easeInOut',
          }}
          className="w-full max-w-sm mx-auto"
          aria-hidden="true"
        >
          <svg viewBox="0 0 380 90" className="w-full h-auto overflow-visible">
            <defs>
              <path
                id="archedTextPath"
                d="M 20,78 Q 190,14 360,78"
                fill="none"
              />
            </defs>
            <text className="font-bubble fill-white text-[27px] font-bold tracking-wide drop-shadow-[0_4px_8px_rgba(0,0,0,0.5)]">
              <textPath href="#archedTextPath" startOffset="50%" textAnchor="middle">
                Why did you click No
              </textPath>
            </text>
          </svg>
        </motion.div>
      </div>

      <div className="my-auto py-6">
        <motion.img
          src={Images.pandaGunBear}
          alt="Panda pointing toy gun at bear"
          className="w-72 sm:w-80 h-auto max-h-64 object-contain mx-auto drop-shadow-2xl"
          animate={{
            y: [0, -6, 0],
          }}
          transition={{
            duration: 2,
            repeat: Infinity,
            ease: 'easeInOut',
          }}
        />
      </div>

      <div className="w-full flex items-center justify-center mb-6">
        <PillButton
          variant="primary"
          onClick={handleRetry}
          className="w-48 transform hover:scale-105 active:scale-95 transition-transform"
        >
          Try Again
        </PillButton>
      </div>
    </div>
  );
};

export default RejectionScreen;
