import React, { useState, useRef, useEffect, useCallback } from 'react';
import AudioAssets from '../assets/audio';
import type { ScreenType } from './types';
import { AppContext } from './types';
export { AppContext } from './types';

export const AppProvider: React.FC<{ children: React.ReactNode; initialScreen?: ScreenType }> = ({
  children,
  initialScreen = 'gift',
}) => {
  const [activeScreen, setActiveScreen] = useState<ScreenType>(initialScreen);
  const [isCandleBlown, setIsCandleBlown] = useState<boolean>(false);
  const [isPlayingMusic, setIsPlayingMusic] = useState<boolean>(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);

  const setScreen = useCallback((screen: ScreenType) => {
    setActiveScreen(screen);
  }, []);

  const blowCandles = useCallback(() => {
    setIsCandleBlown(true);
  }, []);

  const resetCandles = useCallback(() => {
    setIsCandleBlown(false);
  }, []);

  const playMusic = useCallback(async () => {
    if (audioRef.current) {
      try {
        await audioRef.current.play();
        setIsPlayingMusic(true);
      } catch (err) {
        console.warn('Audio playback was prevented by browser policy:', err);
        setIsPlayingMusic(false);
      }
    }
  }, []);

  const pauseMusic = useCallback(() => {
    if (audioRef.current) {
      audioRef.current.pause();
      setIsPlayingMusic(false);
    }
  }, []);

  const toggleMusic = useCallback(() => {
    if (isPlayingMusic) {
      pauseMusic();
    } else {
      void playMusic();
    }
  }, [isPlayingMusic, pauseMusic, playMusic]);

  // Handle audio events
  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;

    const handlePlay = () => setIsPlayingMusic(true);
    const handlePause = () => setIsPlayingMusic(false);
    const handleEnded = () => setIsPlayingMusic(false);

    audio.addEventListener('play', handlePlay);
    audio.addEventListener('pause', handlePause);
    audio.addEventListener('ended', handleEnded);

    return () => {
      audio.removeEventListener('play', handlePlay);
      audio.removeEventListener('pause', handlePause);
      audio.removeEventListener('ended', handleEnded);
    };
  }, []);

  return (
    <AppContext.Provider
      value={{
        activeScreen,
        setScreen,
        isCandleBlown,
        blowCandles,
        resetCandles,
        isPlayingMusic,
        toggleMusic,
        playMusic,
        pauseMusic,
        audioRef,
      }}
    >
      {children}
      {/* Background soundtrack audio element */}
      <audio
        ref={audioRef}
        src={AudioAssets.bgm}
        preload="auto"
        loop
        className="hidden"
      />
    </AppContext.Provider>
  );
};

export default AppContext;
