// /frontend/src/components/RentalYieldForm.jsx
import React, { useState } from 'react';
import usePrediction from '../hooks/usePrediction';
import Loader from './Loader';
import { notifySuccess, notifyError } from '../utils/toast';

export default function RentalYieldForm() {
  const { data, loading, error, fetchPrediction } = usePrediction('/api/rental/yield');
  const [formData, setFormData] = useState({
    size: 0,
    bedrooms: 0,
    bathrooms: 0,
    location: '',
    age: 0,
    country: 'US',
    currency: 'USD',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handlePredict = async () => {
    try {
      await fetchPrediction(formData);
      notifySuccess('Rental yield prediction successful!');
    } catch {
      notifyError('Rental yield prediction failed!');
    }
  };

  return (
    <div className="max-w-md mx-auto p-6 bg-white rounded shadow-md mt-8">
      <h2 className="text-2xl font-bold mb-4">Predict Rental Yield</h2>

      <div className="space-y-4">
        <input type="number" name="size" placeholder="Size (sq ft)" value={formData.size} onChange={handleChange} className="input" />
        <input type="number" name="bedrooms" placeholder="Bedrooms" value={formData.bedrooms} onChange={handleChange} className="input" />
        <input type="number" name="bathrooms" placeholder="Bathrooms" value={formData.bathrooms} onChange={handleChange} className="input" />
        <input type="text" name="location" placeholder="Location" value={formData.location} onChange={handleChange} className="input" />
        <input type="number" name="age" placeholder="Property Age" value={formData.age} onChange={handleChange} className="input" />
        <input type="text" name="country" placeholder="Country (e.g., US)" value={formData.country} onChange={handleChange} className="input" />
        <input type="text" name="currency" placeholder="Currency (e.g., USD)" value={formData.currency} onChange={handleChange} className="input" />

        <button onClick={handlePredict} disabled={loading} className="btn-primary w-full">
          {loading ? 'Predicting…' : 'Predict'}
        </button>

        {loading && <Loader />}

        {data && (
          <div className="mt-4 text-center">
            <p className="text-lg font-semibold">
              Predicted Rental Yield: {data.predicted_rental_yield_percent}%
            </p>
          </div>
        )}

        {error && notifyError(error)}
      </div>
    </div>
  );
}
