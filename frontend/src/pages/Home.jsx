// /frontend/src/pages/Home.jsx
import React from 'react';
import PredictionForm from '../components/PredictionForm';
import RentalYieldForm from '../components/RentalYieldForm';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-4xl font-bold text-center mb-10 text-blue-700">Property Prediction Platform</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div>
          <PredictionForm />
        </div>
        <div>
          <RentalYieldForm />
        </div>
      </div>
    </div>
  );
}
