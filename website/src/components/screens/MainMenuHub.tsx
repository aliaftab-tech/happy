import React from 'react';
import { motion } from 'framer-motion';
import { useApp } from '../../context';
import Images from '../../assets/images';
import TypewriterText from '../common/TypewriterText';

interface MainMenuHubProps {
  onSelectCard?: (cardId: 'cake' | 'memories' | 'letter' | 'finale') => void;
}

export const MainMenuHub: React.FC<MainMenuHubProps> = ({ onSelectCard }) => {
  const { setScreen } = useApp();

  const handleSelect = (cardId: 'cake' | 'memories' | 'letter' | 'finale') => {
    if (onSelectCard) onSelectCard(cardId);
    else setScreen(cardId);
  };

  const menuCards = [
    {
      id: 'cake' as const,
      title: 'Make a Wish',
      icon: Images.hubCardCake,
      alt: 'Birthday Wish Cake',
    },
    {
      id: 'memories' as const,
      title: 'Captured Memories',
      icon: Images.hubCardCamera,
      alt: 'Camera Memories',
    },
    {
      id: 'letter' as const,
      title: 'Special Letter',
      icon: Images.hubCardBottle,
      alt: 'Bottle with Message',
    },
    {
      id: 'finale' as const,
      title: 'Love Note',
      icon: Images.hubCardGift,
      alt: 'Gift Surprise',
    },
  ];

  return (
    <div 
      data-screen="menu"
      className="flex-1 flex flex-col items-center justify-between py-10 px-6 text-center select-none"
    >
      {/* 3-line kinetic reveal heading */}
      <div className="w-full mt-2 font-display uppercase tracking-widest text-white leading-tight">
        <h1 className="sr-only">THESE ARE FOR YOU IMAN FATIMA</h1>
        <h2 className="text-xl sm:text-2xl font-bold">
          <TypewriterText text="THESE ARE" delay={0.1} />
        </h2>
        <h2 className="text-xl sm:text-2xl font-bold mt-1">
          <TypewriterText text="FOR YOU" delay={0.45} />
        </h2>
        <h2 className="text-2xl sm:text-3xl font-extrabold text-btn-primary mt-1">
          <TypewriterText text="IMAN FATIMA" delay={0.8} />
        </h2>
      </div>

      {/* 2x2 Squircle Card Grid */}
      <div className="w-full grid grid-cols-2 gap-4 my-auto max-w-[340px]">
        {menuCards.map((card, index) => (
          <motion.button
            key={card.id}
            data-card={card.id}
            type="button"
            onClick={() => handleSelect(card.id)}
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 + index * 0.1, duration: 0.3 }}
            whileHover={{ y: -5, scale: 1.03, transition: { duration: 0.15 } }}
            whileTap={{ scale: 0.95 }}
            className="aspect-square bg-card-surface hover:bg-card-surface-hover rounded-squircle flex flex-col items-center justify-center p-4 border-t border-white/10 shadow-lg group cursor-pointer"
          >
            <div className="w-20 h-20 flex items-center justify-center mb-1 group-hover:scale-110 transition-transform duration-300">
              <img
                src={card.icon}
                alt={card.alt}
                className="max-w-full max-h-full object-contain drop-shadow"
              />
            </div>
            <span className="font-bubble text-xs sm:text-sm text-white/90">
              {card.title}
            </span>
          </motion.button>
        ))}
      </div>

      <p className="text-white/60 text-xs font-body mb-2">Tap any card to open</p>
    </div>
  );
};

export default MainMenuHub;
