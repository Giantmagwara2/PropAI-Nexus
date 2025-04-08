import React, { useState } from 'react';
import axios from 'axios';

export default function RentalYieldPrediction() {
  const [formData, setFormData] = useState({});
  const [yieldResult, setYieldResult] = useState(null);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const predictYield = async () => {
    try {
      const response = await axios.post('/api/predict/rental-yield', formData);
      setYieldResult(response.data.predicted_rental_yield);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="bg-white dark:bg-gray-800 shadow-md rounded-xl p-6">
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">Rental Yield Predictor</h2>
      <input name="feature1" onChange={handleChange} className="mb-2 p-2 w-full rounded" placeholder="Feature 1..." />
      <input name="feature2" onChange={handleChange} className="mb-2 p-2 w-full rounded" placeholder="Feature 2..." />
      <button onClick={predictYield} className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        Predict Yield
      </button>

      {yieldResult && (
        <div className="mt-4 text-green-500 text-lg font-semibold">
          Predicted Rental Yield: {yieldResult}%
        </div>
      )}
    </div>
  );
}
