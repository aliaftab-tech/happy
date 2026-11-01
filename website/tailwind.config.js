/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'bg-primary': '#810503',
        'bg-primary-dark': '#5c0201',
        'bg-secondary': '#ac5150',
        'card-surface': '#a7302c',
        'card-surface-hover': '#bd3834',
        'btn-primary': '#fc7272',
        'btn-accent': '#f9588e',
        'btn-hover': '#ff8585',
        'text-accent-pink': '#f06272',
        'paper-letter-bg': '#f7a1c4',
        'paper-letter-title': '#9b1836',
        'paper-letter-body': '#6d1123',
        'parchment-note-bg': '#faf3e8',
        'parchment-note-text': '#5a2424',
        'vinyl-body': '#111113',
        'vinyl-label-orange': '#e85d26',
        'candle-flame-gold': '#ffbe3b',
      },
      fontFamily: {
        calligraphic: ['"Great Vibes"', 'cursive'],
        dancing: ['"Dancing Script"', 'cursive'],
        marker: ['"Caveat"', 'cursive'],
        display: ['"Syncopate"', 'sans-serif'],
        serif: ['"Playfair Display"', 'serif'],
        bubble: ['"Fredoka"', 'sans-serif'],
        body: ['"Nunito"', 'sans-serif'],
      },
      boxShadow: {
        'pill': '0 4px 14px rgba(252, 114, 114, 0.35)',
        'polaroid': '0 6px 16px rgba(0, 0, 0, 0.3)',
      },
      borderRadius: {
        'squircle': '32px',
      }
    },
  },
  plugins: [],
}
