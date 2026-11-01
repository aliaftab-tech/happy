import React from 'react';
import { AnimatePresence, motion } from 'framer-motion';
import { AppProvider, useApp } from './context';
import MobileContainer from './components/common/MobileContainer';
import FloatingHearts from './components/common/FloatingHearts';

// Screens
import WhatsAppPreview from './components/screens/WhatsAppPreview';
import GiftOpener from './components/screens/GiftOpener';
import SurpriseTeaser from './components/screens/SurpriseTeaser';
import RejectionScreen from './components/screens/RejectionScreen';
import MainMenuHub from './components/screens/MainMenuHub';
import WishCakeScreen from './components/screens/WishCakeScreen';
import MemoriesScreen from './components/screens/MemoriesScreen';
import LoveLetterScreen from './components/screens/LoveLetterScreen';
import FinaleScreen from './components/screens/FinaleScreen';

const ScreenRenderer: React.FC = () => {
  const { activeScreen } = useApp();

  const renderActiveScreen = () => {
    switch (activeScreen) {
      case 'whatsapp':
        return <WhatsAppPreview />;
      case 'gift':
        return <GiftOpener />;
      case 'teaser':
        return <SurpriseTeaser />;
      case 'rejection':
        return <RejectionScreen />;
      case 'menu':
        return <MainMenuHub />;
      case 'cake':
        return <WishCakeScreen />;
      case 'memories':
        return <MemoriesScreen />;
      case 'letter':
        return <LoveLetterScreen />;
      case 'finale':
        return <FinaleScreen />;
      default:
        return <GiftOpener />;
    }
  };

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={activeScreen}
        initial={{ opacity: 0, y: 8 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -8 }}
        transition={{ duration: 0.25, ease: 'easeInOut' }}
        className="flex-1 flex flex-col relative z-10 w-full"
      >
        {renderActiveScreen()}
      </motion.div>
    </AnimatePresence>
  );
};

const AppContent: React.FC = () => {
  const { isPlayingMusic, toggleMusic, playMusic } = useApp();

  // Auto-play background song across entire website on page open and first touch
  React.useEffect(() => {
    // Try to auto-play immediately when page loads
    void playMusic();

    const handleFirstInteraction = () => {
      void playMusic();
    };

    window.addEventListener('click', handleFirstInteraction, { once: true });
    window.addEventListener('touchstart', handleFirstInteraction, { once: true });

    return () => {
      window.removeEventListener('click', handleFirstInteraction);
      window.removeEventListener('touchstart', handleFirstInteraction);
    };
  }, [playMusic]);

  return (
    <MobileContainer>
      {/* Floating Music Toggle Button in Top-Right Corner */}
      <button
        type="button"
        onClick={toggleMusic}
        className="absolute top-4 right-4 z-50 w-10 h-10 rounded-full bg-black/40 backdrop-blur-md border border-white/20 text-white flex items-center justify-center shadow-lg hover:scale-110 active:scale-95 transition-all"
        title={isPlayingMusic ? 'Pause Music' : 'Play Background Music'}
        aria-label={isPlayingMusic ? 'Pause Music' : 'Play Music'}
      >
        {isPlayingMusic ? (
          <span className="text-base animate-spin [animation-duration:3s]">💿</span>
        ) : (
          <span className="text-base opacity-70">🔇</span>
        )}
      </button>

      <FloatingHearts count={10} />
      <ScreenRenderer />
    </MobileContainer>
  );
};

export const App: React.FC = () => {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
};

export default App;
