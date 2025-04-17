import React from 'react';

export default function Contact() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 dark:bg-gray-900 transition-colors duration-300 p-6">
      <h1 className="text-4xl font-bold text-blue-600 dark:text-blue-400 mb-4">Contact Us</h1>
      <p className="text-gray-700 dark:text-gray-300 text-center max-w-md mb-8">
        Have questions or feedback? We'd love to hear from you. 🚀
      </p>
      <button className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded transition">
        Send Email
      </button>
    </div>
  );
}
