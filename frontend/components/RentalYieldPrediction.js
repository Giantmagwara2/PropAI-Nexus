// /frontend/src/components/RentalYieldPrediction.js
import React, { useState } from 'react';
import usePrediction from '../hooks/usePrediction';
import Loader from './Loader';

export default function RentalYieldPrediction() {
  const { data, loading, error, fetchPrediction } = usePrediction(process.env.REACT_APP_RENTAL_YIELD_API || '/api/rental-yield/');
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
    if (formData.size <= 0 || formData.bedrooms <= 0 || formData.bathrooms <= 0) {
      alert("Size, bedrooms, and bathrooms must be positive numbers.");
      return;
    }
    if (!formData.location) {
      alert("Location is required.");
      return;
    }
    fetchPrediction(formData);
  };

  return (
    <div className="bg-white dark:bg-gray-800 shadow-md rounded-xl p-6">
      <h2 className="text-xl font-bold text-gray-900 dark:text-white mb-4">Rental Yield Predictor</h2>
      <input name="size" type="number" onChange={handleChange} placeholder="Size" aria-label="Property size in square feet" className="mb-2 p-2 w-full rounded" />
      <input name="bedrooms" type="number" onChange={handleChange} placeholder="Bedrooms" aria-label="Number of bedrooms" className="mb-2 p-2 w-full rounded" />
      <input name="bathrooms" type="number" onChange={handleChange} placeholder="Bathrooms" aria-label="Number of bathrooms" className="mb-2 p-2 w-full rounded" />
      <input name="location" type="text" onChange={handleChange} placeholder="Location" aria-label="Property location" className="mb-2 p-2 w-full rounded" />
      <input name="age" type="number" onChange={handleChange} placeholder="Age" aria-label="Property age in years" className="mb-2 p-2 w-full rounded" />
      <select name="country" onChange={handleChange} value={formData.country} className="mb-2 p-2 w-full rounded">
        <option value="US">United States</option>
        <option value="CA">Canada</option>
        <option value="UK">United Kingdom</option>
      </select>
      <select name="currency" onChange={handleChange} value={formData.currency} className="mb-2 p-2 w-full rounded">
        <option value="USD">USD</option>
        <option value="CAD">CAD</option>
        <option value="GBP">GBP</option>
      </select>
      <button
        onClick={handlePredict}
        disabled={loading}
        className={`bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition ${loading ? "opacity-50 cursor-not-allowed" : ""}`}
      >
        {loading ? "Predicting..." : "Predict Rental Yield"}
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
