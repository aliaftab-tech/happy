import React from 'react';
import { useApp } from '../../context';
import Images from '../../assets/images';

export const WhatsAppPreview: React.FC = () => {
  const { setScreen } = useApp();

  return (
    <div
      data-screen="whatsapp"
      className="flex-1 flex flex-col justify-between cursor-pointer select-none bg-[#0b141a] text-white min-h-[100dvh]"
      onClick={() => setScreen('gift')}
    >
      {/* Top Phone Status Bar */}
      <div className="w-full px-5 pt-3 pb-1 flex items-center justify-between text-xs text-gray-300 font-medium">
        <span>2:30</span>
        <div className="flex items-center gap-1.5">
          <svg className="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
            <path d="M12 3c-4.97 0-9 4.03-9 9 0 2.12.74 4.07 1.97 5.61L4.35 21l3.54-.93C9.35 20.61 10.63 21 12 21c4.97 0 9-4.03 9-9s-4.03-9-9-9zm0 16.5c-1.25 0-2.45-.34-3.5-.98l-.25-.15-2.6.68.7-2.53-.16-.26C5.55 15.21 5.25 13.65 5.25 12c0-3.72 3.03-6.75 6.75-6.75s6.75 3.03 6.75 6.75-3.03 6.75-6.75 6.75z" />
          </svg>
          <svg className="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24">
            <path d="M12 4C7.31 4 3.07 5.9 0 8.98L12 21 24 8.98C20.93 5.9 16.69 4 12 4z" />
          </svg>
          <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
            <path d="M17 5v14a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h1V1h4v2h1a2 2 0 0 1 2 2z" />
          </svg>
        </div>
      </div>

      {/* Simulated WhatsApp Contact Header */}
      <div className="w-full bg-[#1f2c34] px-3 py-2.5 flex items-center justify-between border-b border-white/5 shadow-md">
        <div className="flex items-center gap-2.5">
          <span className="text-gray-300 text-lg">←</span>
          <div className="w-9 h-9 rounded-full bg-gradient-to-tr from-btn-accent to-btn-primary flex items-center justify-center text-sm shadow">
            ❤️
          </div>
          <div className="flex flex-col text-left">
            <span className="font-semibold text-sm leading-tight text-gray-100">My Cutie ❤️</span>
            <span className="text-[11px] text-[#25d366] leading-tight font-medium">online</span>
          </div>
        </div>
        <div className="flex items-center gap-4 text-gray-300 pr-1">
          <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
            <path d="M17 10.5V7c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1v10c0 .55.45 1 1 1h12c.55 0 1-.45 1-1v-3.5l4 4v-11l-4 4z" />
          </svg>
          <svg className="w-4 h-4 fill-current" viewBox="0 0 24 24">
            <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 0 0-1.01.24l-2.2 2.2a15.05 15.05 0 0 1-6.59-6.59l2.2-2.21a.96.96 0 0 0 .25-1.01A11.36 11.36 0 0 1 8.5 3.99c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.5c0-.56-.45-1.01-.99-1.01z" />
          </svg>
          <span className="text-gray-300 text-lg leading-none font-bold">⋮</span>
        </div>
      </div>

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col justify-center items-center px-4 py-3 relative">
        {/* Date Divider Badge */}
        <div className="mb-4 bg-[#182229] px-3 py-1 rounded-lg text-[11px] text-gray-400 font-medium tracking-wide shadow-sm uppercase">
          Today
        </div>

        {/* Message Bubble with Speech Bubble Tail */}
        <div className="w-full max-w-sm relative group transition-transform hover:scale-[1.01] active:scale-[0.99]">
          {/* Speech Bubble Tail */}
          <div 
            className="absolute -top-1.5 -left-1.5 w-4 h-4 bg-[#1f2c34]" 
            style={{ clipPath: 'polygon(100% 0, 0 0, 100% 100%)' }}
            aria-hidden="true"
          />

          <div className="w-full bg-[#1f2c34] rounded-2xl rounded-tl-sm overflow-hidden shadow-2xl border border-white/10 p-1.5">
            {/* Embedded Link Preview Card */}
            <div className="rounded-xl overflow-hidden bg-[#111b21] border border-white/5">
              <div className="bg-[#810503] p-4 text-center relative overflow-hidden">
                <p className="font-dancing text-2xl text-white drop-shadow">
                  I made a gift for you
                </p>
                <img
                  src={Images.introGiftBox}
                  alt="Gift Box"
                  className="w-32 h-32 mx-auto my-2 object-contain drop-shadow-[0_10px_20px_rgba(0,0,0,0.5)] transform group-hover:scale-105 transition-transform duration-300"
                />
              </div>
              <div className="p-3.5 bg-[#182229]">
                <h3 className="font-bold text-white text-base">Gift</h3>
                <p className="text-gray-300 text-xs mt-1 leading-relaxed">
                  Discover a special gift made just for you. Click to open and enjoy the surprise crafted with care. Experience the joy now.
                </p>
                <p className="text-gray-400 text-[11px] mt-2 flex items-center gap-1.5">
                  <span>🔗</span>
                  <span className="text-sky-400 underline underline-offset-2 font-mono">
                    dua-digitals.my.canva.site
                  </span>
                </p>
              </div>
            </div>

            {/* Bubble Timestamp and Blue Double Check Ticks */}
            <div className="flex items-center justify-end gap-1 px-2 pt-1 text-[11px] text-gray-400">
              <span>2:30 PM</span>
              <span className="text-[#53bdeb] font-bold text-xs" title="Read">✓✓</span>
            </div>
          </div>
        </div>

        <p className="text-gray-400 text-xs mt-5 animate-pulse flex items-center gap-1.5">
          <span>👆</span> Tap anywhere to open message
        </p>
      </div>

      {/* Simulated WhatsApp Bottom Input Bar */}
      <div className="w-full bg-[#1f2c34] px-3 py-2 flex items-center gap-2 border-t border-white/5">
        <div className="flex-1 bg-[#2a3942] rounded-full px-4 py-2 flex items-center justify-between text-gray-400 text-sm">
          <div className="flex items-center gap-2">
            <span>😊</span>
            <span className="text-gray-400 text-xs font-normal">Message...</span>
          </div>
          <div className="flex items-center gap-2.5">
            <span>📎</span>
            <span>📷</span>
          </div>
        </div>
        <div className="w-10 h-10 rounded-full bg-[#00a884] flex items-center justify-center text-white shadow-md text-sm">
          🎙️
        </div>
      </div>
    </div>
  );
};

export default WhatsAppPreview;
