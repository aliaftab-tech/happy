import React from 'react';

interface PillButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'accent' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
}

export const PillButton: React.FC<PillButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children,
  className = '',
  disabled,
  ...props
}) => {
  const baseStyles =
    'rounded-full font-bubble font-semibold transition-all duration-200 cursor-pointer flex items-center justify-center select-none text-white shadow-pill disabled:opacity-50 disabled:cursor-not-allowed';

  const sizeStyles = {
    sm: 'px-6 py-2.5 text-base min-h-[44px]',
    md: 'px-8 py-3 text-lg min-h-[56px]',
    lg: 'px-10 py-3.5 text-xl min-h-[64px]',
  }[size];

  const variantStyles = {
    primary: 'bg-btn-primary hover:bg-btn-hover active:scale-95 shadow-[0_4px_14px_rgba(252,114,114,0.4)]',
    accent: 'bg-btn-accent hover:opacity-90 active:scale-95 shadow-[0_4px_14px_rgba(249,88,142,0.4)]',
    outline: 'border-2 border-white/80 hover:bg-white/10 active:scale-95',
  }[variant];

  return (
    <button
      className={`${baseStyles} ${sizeStyles} ${variantStyles} ${className}`}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};

export default PillButton;
