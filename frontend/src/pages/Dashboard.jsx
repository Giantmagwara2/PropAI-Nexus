// /frontend/src/pages/Dashboard.jsx
import React from 'react';
import { motion } from 'framer-motion';

const stats = [
  { label: 'Total Properties Analyzed', value: '1,240' },
  { label: 'Total Estimated Value', value: '$48.3M' },
  { label: 'Average Rental Yield', value: '6.4%' },
  { label: 'Active Predictions', value: '89' },
];

export default function Dashboard() {
  return (
    <div className="min-h-screen p-6 md:p-10 bg-gray-50 dark:bg-gray-900 transition-colors duration-300">
      
      {/* Title */}
      <section className="text-center mb-12">
        <h1 className="text-4xl md:text-5xl font-bold text-gray-800 dark:text-white mb-4">
          PropAI Nexus Dashboard
        </h1>
        <p className="text-gray-600 dark:text-gray-300">
          Your property prediction and rental insights in real-time.
        </p>
      </section>

      {/* Stats Section */}
      <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
        {stats.map((stat, index) => (
          <motion.div
            key={index}
            className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md hover:shadow-lg transition duration-300 text-center"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.2 }}
          >
            <h2 className="text-3xl font-bold text-blue-600 dark:text-blue-400">{stat.value}</h2>
            <p className="mt-2 text-gray-700 dark:text-gray-300">{stat.label}</p>
          </motion.div>
        ))}
      </section>

    </div>
  );
}
