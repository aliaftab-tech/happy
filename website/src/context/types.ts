import React from 'react';

export type ScreenType =
  | 'whatsapp'
  | 'gift'
  | 'teaser'
  | 'rejection'
  | 'menu'
  | 'cake'
  | 'memories'
  | 'letter'
  | 'finale';

export interface AppContextType {
  activeScreen: ScreenType;
  setScreen: (screen: ScreenType) => void;
  isCandleBlown: boolean;
  blowCandles: () => void;
  resetCandles: () => void;
  isPlayingMusic: boolean;
  toggleMusic: () => void;
  playMusic: () => Promise<void>;
  pauseMusic: () => void;
  audioRef: React.RefObject<HTMLAudioElement | null>;
}

export const AppContext = React.createContext<AppContextType | undefined>(undefined);
