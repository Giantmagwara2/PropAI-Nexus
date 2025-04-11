// /frontend/src/components/RentalYieldPrediction.js
import React, { useState } from 'react';
import usePrediction from '../hooks/usePrediction';
import Loader from './Loader';

export default function RentalYieldPrediction() {
  const { data, loading, error, fetchPrediction } = usePrediction('/api/rental-yield/');
  const [formData, setFormData] = useState({
    size: 0,
    bedrooms: 0,
    bathrooms: 0,
    location: "",
    age: 0,
    country: "US",
    currency: "USD"
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handlePredict = () => {
    fetchPrediction(formData);
  };

  return (
    <div className="bg-white dark:bg-gray-800 shadow-md rounded-xl p-6">
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">Rental Yield Predictor</h2>
      <input name="size" type="number" onChange={handleChange} placeholder="Size" className="mb-2 p-2 w-full rounded" />
      <input name="bedrooms" type="number" onChange={handleChange} placeholder="Bedrooms" className="mb-2 p-2 w-full rounded" />
      <input name="bathrooms" type="number" onChange={handleChange} placeholder="Bathrooms" className="mb-2 p-2 w-full rounded" />
      <input name="location" type="text" onChange={handleChange} placeholder="Location" className="mb-2 p-2 w-full rounded" />
      <input name="age" type="number" onChange={handleChange} placeholder="Age" className="mb-2 p-2 w-full rounded" />
      <button onClick={handlePredict} className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        Predict Rental Yield
      </button>
      {loading && <Loader />}
      {error && <p className="text-red-500 mt-4">{error}</p>}
      {data && (
        <div className="mt-4 text-green-500 text-lg font-semibold">
          Predicted Rental Yield: {data.predicted_rental_yield_percent}%
        </div>
      )}
    </div>
  );
}
