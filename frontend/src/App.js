// /frontend/src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, useTheme } from './context/ThemeContext';
import { ToastContainer } from 'react-toastify';
import NavBar from './components/NavBar';
import ScrollToTop from './components/ScrollToTop';
import { AnimatePresence } from 'framer-motion';

import Home from './pages/Home';
import Dashboard from './pages/Dashboard';
import About from './pages/About';
import Contact from './pages/Contact';

import 'react-toastify/dist/ReactToastify.css';

function AppContent() {
  const { theme } = useTheme();

  return (
    <div className={`min-h-screen transition-colors duration-300 ${theme === 'dark' ? 'bg-gray-900' : 'bg-gray-100'}`}>
      <Router>
        <ScrollToTop />
        <NavBar />
        <AnimatePresence mode="wait">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
          </Routes>
        </AnimatePresence>
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
      </Router>
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
