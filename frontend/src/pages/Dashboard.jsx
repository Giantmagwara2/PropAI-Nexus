import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import axios from 'axios';
import { notifyError } from '../lib/toast';

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchStats() {
      try {
        const response = await axios.get('/api/dashboard/metrics');
        setStats(response.data);
      } catch (error) {
        console.error('Dashboard metrics fetch error:', error);
        notifyError('Failed to load dashboard metrics.');
      } finally {
        setLoading(false);
      }
    }

    fetchStats();
  }, []);

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
      {loading ? (
        <div className="text-center text-gray-600 dark:text-gray-300">
          Loading metrics...
        </div>
      ) : stats ? (
        <section className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
          {/* Total Properties */}
          <motion.div
            className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md hover:shadow-lg text-center"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
          >
            <h2 className="text-3xl font-bold text-blue-600 dark:text-blue-400">
              {stats.total_properties?.toLocaleString() || 0}
            </h2>
            <p className="mt-2 text-gray-700 dark:text-gray-300">
              Total Properties Analyzed
            </p>
          </motion.div>

          {/* Total Estimated Value */}
          <motion.div
            className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md hover:shadow-lg text-center"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <h2 className="text-3xl font-bold text-blue-600 dark:text-blue-400">
              ${stats.total_estimated_value?.toLocaleString() || 0}
            </h2>
            <p className="mt-2 text-gray-700 dark:text-gray-300">
              Total Estimated Value
            </p>
          </motion.div>

          {/* Average Rental Yield */}
          <motion.div
            className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md hover:shadow-lg text-center"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.3 }}
          >
            <h2 className="text-3xl font-bold text-blue-600 dark:text-blue-400">
              {stats.average_rental_yield?.toFixed(2) || 0}%
            </h2>
            <p className="mt-2 text-gray-700 dark:text-gray-300">
              Average Rental Yield
            </p>
          </motion.div>

          {/* Active Predictions */}
          <motion.div
            className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-md hover:shadow-lg text-center"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
          >
            <h2 className="text-3xl font-bold text-blue-600 dark:text-blue-400">
              {stats.active_predictions?.toLocaleString() || 0}
            </h2>
            <p className="mt-2 text-gray-700 dark:text-gray-300">
              Active Predictions
            </p>
          </motion.div>
        </section>
      ) : (
        <div className="text-center text-red-500">No data available.</div>
      )}
    </div>
  );
}
