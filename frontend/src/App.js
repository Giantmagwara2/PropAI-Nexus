import React from 'react';
import RentalYieldPrediction from './components/RentalYieldPrediction';
import MarketSentiment from './components/MarketSentiment';
import { ThemeProvider, useTheme } from './context/ThemeContext';

function App() {
  const { theme, toggleTheme } = useTheme();

  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900 transition-colors duration-300">
      <header className="p-4 flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-800 dark:text-gray-100">PropAI Nexus Dashboard</h1>
        <button
          onClick={toggleTheme}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        >
          Toggle {theme === 'light' ? 'Dark' : 'Light'} Mode
        </button>
      </header>
      <main className="p-4">
        <RentalYieldPrediction />
        <MarketSentiment />
      </main>
    </div>
  );
}

export default App;
