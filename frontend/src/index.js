import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { ThemeProvider } from './context/ThemeContext';
import './index.css'; // Ensure this imports Tailwind CSS or your custom styles
import './i18n';
import { initGA, logPageView } from './analytics';
initGA();
logPageView();
// also hook into React Router to log on each route change



ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider>
      <App />
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
