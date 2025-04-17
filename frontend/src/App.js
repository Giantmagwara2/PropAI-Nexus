// /frontend/src/App.js
import React from 'react';
import Home from './pages/Home';
import { ThemeProvider, useTheme } from './context/ThemeContext';
import NavBar from './components/NavBar';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

function AppContent() {
  const { theme } = useTheme();

  return (
    <div className={`min-h-screen transition-colors duration-300 ${theme === 'dark' ? 'bg-gray-900' : 'bg-gray-100'}`}>
      <NavBar /> {/* Use the new NavBar */}
      
      <main className="p-4">
        <Home />
      </main>

      {/* Toast Container with Dynamic Dark/Light Mode Styling */}
      <ToastContainer
        position="top-right"
        autoClose={4000}
        hideProgressBar={false}
        newestOnTop
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme={theme === 'dark' ? 'dark' : 'light'}
        toastStyle={{
          borderRadius: '10px',
          background: theme === 'dark' ? '#1f2937' : '#ffffff',
          color: theme === 'dark' ? '#f9fafb' : '#1f2937',
          border: '1px solid #3b82f6',
          boxShadow: '0 4px 12px rgba(0, 0, 0, 0.15)'
        }}
      />
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
