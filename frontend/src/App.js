// /frontend/src/App.js
import React from 'react';
import Home from './pages/Home';
import { ThemeProvider, useTheme } from './context/ThemeContext';
import NavBar from './components/NavBar'; // 👈 Import the NavBar

function AppContent() {
  const { theme } = useTheme();

  return (
    <div className={`min-h-screen transition-colors duration-300 ${theme === 'dark' ? 'bg-gray-900' : 'bg-gray-100'}`}>
      <NavBar /> {/* 👈 Use NavBar here */}
      
      <main className="p-4">
        <Home /> {/* Home contains Prediction + Rental Yield forms */}
      </main>
    </div>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <AppContent />
    </ThemeProvider>
  );
}
