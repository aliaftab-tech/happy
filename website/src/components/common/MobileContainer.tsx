import React from 'react';

interface MobileContainerProps {
  children: React.ReactNode;
  className?: string;
}

export const MobileContainer: React.FC<MobileContainerProps> = ({
  children,
  className = '',
}) => {
  return (
    <div className="min-h-screen min-h-[100dvh] w-full bg-[#3d0101] flex items-center justify-center p-0 sm:p-4 md:p-6 relative overflow-x-hidden selection:bg-btn-primary selection:text-white">
      {/* Ambient desktop vignette background effects */}
      <div 
        className="fixed inset-0 pointer-events-none opacity-60 hidden sm:block"
        style={{
          background: 'radial-gradient(circle at 50% 50%, rgba(129, 5, 3, 0.5) 0%, rgba(61, 1, 1, 0.95) 100%)',
        }}
      />
      <div className="fixed -top-40 -left-40 w-96 h-96 bg-[#810503] rounded-full blur-3xl opacity-30 pointer-events-none hidden sm:block" />
      <div className="fixed -bottom-40 -right-40 w-96 h-96 bg-[#a7302c] rounded-full blur-3xl opacity-20 pointer-events-none hidden sm:block" />

      {/* 9:16 Centered Mobile Frame */}
      <main
        className={`w-full max-w-[440px] min-h-[100dvh] bg-bg-primary text-white relative z-10 sm:rounded-[36px] sm:shadow-[0_25px_60px_-15px_rgba(0,0,0,0.7)] sm:border sm:border-white/10 flex flex-col overflow-x-hidden overflow-y-auto ${className}`}
        style={{
          boxShadow: '0 0 50px rgba(0, 0, 0, 0.6), inset 0 0 2px rgba(255, 255, 255, 0.1)',
        }}
      >
        {children}
      </main>
    </div>
  );
};

export default MobileContainer;
