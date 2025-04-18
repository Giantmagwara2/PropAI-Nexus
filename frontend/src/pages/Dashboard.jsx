import React from 'react';
import { motion } from 'framer-motion';
import useSWR from 'swr';
import { fetchWithApiKey } from '../lib/api'; // We'll create this small helper

// Define the fetcher function to use in SWR
const fetcher = (url) => fetchWithApiKey(url).then((res) => res.json());

export default function Dashboard() {
  const { data, error } = useSWR('/api/dashboard/metrics', fetcher, {
    refreshInterval: 10000, // Auto-refresh every 10 seconds
  });

  // Define the stats to display
  const stats = [
    { label: 'Total Properties Analyzed', value: data ? data.total_properties_analyzed : '...' },
    { label: 'Total Estimated Value', value: data ? `$${data.total_estimated_value.toLocaleString()}` : '...' },
    { label: 'Average Rental Yield', value: data ? `${data.average_rental_yield}%` : '...' },
    { label: 'Active Predictions', value: data ? data.active_predictions : '...' },
  ];

  // Handle error state
  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center text-center p-6">
        <div>
          <h1 className="text-3xl font-bold text-red-600 mb-4">Failed to load dashboard</h1>
          <p className="text-gray-600 dark:text-gray-300">Please refresh or try again later.</p>
        </div>
      </div>
    );
  }

  // Handle loading state
  if (!data) {
    return (
      <div className="min-h-screen flex items-center justify-center text-center p-6">
        <div>
          <h1 className="text-3xl font-bold text-blue-600 mb-4">Loading Dashboard...</h1>
          <p className="text-gray-600 dark:text-gray-300">Fetching real-time metrics...</p>
        </div>
      </div>
    );
  }

  // Render the dashboard with stats
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
