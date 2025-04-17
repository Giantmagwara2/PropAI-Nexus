// /frontend/src/components/NavBar.js
import React from 'react';
import { useTheme } from '../context/ThemeContext';

export default function NavBar() {
  const { theme, toggleTheme } = useTheme();

  return (
    <nav className="w-full flex justify-between items-center px-6 py-4 bg-white dark:bg-gray-800 shadow-md dark:shadow-gray-700 transition-colors">
      <div className="flex items-center space-x-4">
        <span className="text-2xl font-bold text-blue-600">PropAI Nexus</span>
        <div className="hidden md:flex space-x-6 ml-8">
          <a href="#" className="text-gray-700 dark:text-gray-200 hover:text-blue-600 transition">Dashboard</a>
          <a href="#" className="text-gray-700 dark:text-gray-200 hover:text-blue-600 transition">Properties</a>
          <a href="#" className="text-gray-700 dark:text-gray-200 hover:text-blue-600 transition">Insights</a>
          <a href="#" className="text-gray-700 dark:text-gray-200 hover:text-blue-600 transition">Settings</a>
        </div>
      </div>

      <button
        onClick={toggleTheme}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Toggle {theme === 'light' ? 'Dark' : 'Light'} Mode
      </button>
    </nav>
  );
}
