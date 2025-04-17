import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion } from 'framer-motion';

export default function NavBar() {
  const location = useLocation();

  const navLinks = [
    { name: 'Home', path: '/' },
    { name: 'Dashboard', path: '/dashboard' },
    { name: 'About', path: '/about' },
    { name: 'Contact', path: '/contact' }
  ];

  return (
    <nav className="bg-white dark:bg-gray-900 shadow-md transition-all duration-300">
      <div className="max-w-7xl mx-auto px-4 md:px-8 py-4 flex justify-between items-center">
        
        {/* Logo / Brand */}
        <Link to="/" className="text-2xl font-extrabold text-blue-600 dark:text-blue-400 tracking-wide">
          PropAI Nexus
        </Link>

        {/* Navigation Links */}
        <div className="flex items-center gap-8">
          {navLinks.map(link => (
            <motion.div
              key={link.path}
              whileHover={{ scale: 1.08 }}
              whileTap={{ scale: 0.95 }}
              className="relative"
            >
              <Link
                to={link.path}
                className={`text-md font-semibold ${
                  location.pathname === link.path
                    ? 'text-blue-600 dark:text-blue-400 underline underline-offset-4'
                    : 'text-gray-700 dark:text-gray-300'
                } hover:text-blue-500 dark:hover:text-blue-300 transition-colors duration-200`}
              >
                {link.name}
              </Link>
            </motion.div>
          ))}
        </div>

      </div>
    </nav>
  );
}
