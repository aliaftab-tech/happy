import React from 'react';

interface FloatingHeartsProps {
  count?: number;
}

export const FloatingHearts: React.FC<FloatingHeartsProps> = ({ count = 12 }) => {
  const hearts = Array.from({ length: count }, (_, i) => ({
    id: i,
    left: `${(i * 19) % 95 + 2}%`,
    duration: 6 + (i % 5) * 2,
    delay: (i % 7) * 0.8,
    size: 14 + (i % 4) * 6,
    opacity: 0.15 + (i % 3) * 0.1,
  }));

  return (
    <div className="absolute inset-0 pointer-events-none overflow-hidden z-0">
      {hearts.map((h) => (
        <span
          key={h.id}
          className="absolute bottom-[-40px] text-pink-300 animate-float"
          style={{
            left: h.left,
            fontSize: `${h.size}px`,
            opacity: h.opacity,
            animationDuration: `${h.duration}s`,
            animationDelay: `${h.delay}s`,
            animationIterationCount: 'infinite',
            animationTimingFunction: 'ease-in-out',
          }}
        >
          ♥
        </span>
      ))}
    </div>
  );
};

export default FloatingHearts;
