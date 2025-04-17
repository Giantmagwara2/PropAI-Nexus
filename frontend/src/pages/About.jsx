import React from 'react';

export default function About() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 dark:bg-gray-900 transition-colors duration-300 p-6">
      <h1 className="text-4xl font-bold text-blue-600 dark:text-blue-400 mb-4">About PropAI Nexus</h1>
      <p className="text-gray-700 dark:text-gray-300 text-center max-w-2xl">
        PropAI Nexus empowers real estate investors by delivering AI-driven property predictions.
        Our mission is to make data-driven investing accessible, fast, and intuitive.
      </p>
    </div>
  );
}
