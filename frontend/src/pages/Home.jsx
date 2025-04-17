// /frontend/src/pages/Home.jsx
import React from 'react';
import PredictionForm from '../components/PredictionForm';
import RentalYieldForm from '../components/RentalYieldForm';

export default function Home() {
  return (
    <div className="min-h-screen p-6 md:p-10 bg-gray-50 dark:bg-gray-900 transition-colors duration-300">
      
      {/* Hero Section */}
      <section className="text-center mb-12">
        <h2 className="text-sm md:text-lg text-blue-600 dark:text-blue-400 font-semibold mb-2 uppercase tracking-wider">
          AI-Powered Real Estate Insights
        </h2>
        <h1 className="text-4xl md:text-5xl font-extrabold text-gray-800 dark:text-white mb-4 leading-tight">
          Property Prediction Platform
        </h1>
        <p className="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto text-base md:text-lg">
          Get instant property value and rental yield estimates powered by advanced AI models. 
          Make smarter investment decisions today!
        </p>
      </section>

      {/* Prediction Forms */}
      <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Property Value Prediction */}
        <div className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
          <h3 className="text-2xl font-bold text-center text-gray-800 dark:text-white mb-6">
            Property Value Prediction
          </h3>
          <PredictionForm />
        </div>

        {/* Rental Yield Prediction */}
        <div className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg hover:shadow-2xl transition-shadow duration-300">
          <h3 className="text-2xl font-bold text-center text-gray-800 dark:text-white mb-6">
            Rental Yield Prediction
          </h3>
          <RentalYieldForm />
        </div>
      </section>

    </div>
  );
}
