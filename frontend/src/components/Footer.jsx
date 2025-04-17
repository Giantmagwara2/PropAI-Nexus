import React from 'react';

export default function Footer() {
  return (
    <footer className="bg-white dark:bg-gray-800 mt-12 py-4">
      <div className="max-w-7xl mx-auto text-center text-gray-600 dark:text-gray-400 text-sm">
        © {new Date().getFullYear()} PropAI Nexus. All rights reserved.
      </div>
    </footer>
  );
}
