import React from 'react';
import { motion, type Variants } from 'framer-motion';

export interface TypewriterTextProps {
  text: string;
  className?: string;
  delay?: number;
  staggerDuration?: number;
  cursor?: boolean;
  onComplete?: () => void;
}

export const TypewriterText: React.FC<TypewriterTextProps> = ({
  text,
  className = '',
  delay = 0.1,
  staggerDuration = 0.035,
  cursor = false,
  onComplete,
}) => {
  const characters = Array.from(text);

  const containerVariants: Variants = {
    hidden: {},
    visible: {
      transition: {
        staggerChildren: staggerDuration,
        delayChildren: delay,
      },
    },
  };

  const charVariants: Variants = {
    hidden: {
      opacity: 0,
      y: 4,
      display: 'inline-block',
    },
    visible: {
      opacity: 1,
      y: 0,
      display: 'inline-block',
      transition: {
        type: 'spring',
        damping: 15,
        stiffness: 250,
      },
    },
  };

  return (
    <motion.span
      className={`inline-block ${className}`}
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      onAnimationComplete={onComplete}
      aria-label={text}
    >
      <span className="sr-only">{text}</span>
      {characters.map((char, index) => (
        <motion.span
          key={`${char}-${index}`}
          variants={charVariants}
          aria-hidden="true"
        >
          {char === ' ' ? '\u00A0' : char}
        </motion.span>
      ))}
      {cursor && (
        <motion.span
          initial={{ opacity: 0 }}
          animate={{ opacity: [0, 1, 0] }}
          transition={{ repeat: Infinity, duration: 0.8, ease: 'linear' }}
          className="inline-block ml-0.5 font-normal text-btn-primary"
          aria-hidden="true"
        >
          |
        </motion.span>
      )}
    </motion.span>
  );
};

export default TypewriterText;
