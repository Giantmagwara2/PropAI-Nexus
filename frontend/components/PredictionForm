import React, { useState } from 'react';
import usePrediction from '../hooks/usePrediction';
import Loader from './Loader';
import { notifySuccess, notifyError } from '../utils/toast';

export default function PredictionForm() {
  const { data, loading, error, fetchPrediction } = usePrediction('/api/predict/');
  const [formData, setFormData] = useState({ size:0, bedrooms:0, bathrooms:0, location:'', age:0, country:'US', currency:'USD' });

  const handlePredict = async () => {
    try {
      await fetchPrediction(formData);
      notifySuccess('Prediction successful');
    } catch {
      notifyError('Prediction failed');
    }
  };

  return (
    <div>
      {/* Inputs omitted for brevity */}
      <button onClick={handlePredict} disabled={loading}>
        {loading ? 'Predicting…' : 'Predict'}
      </button>
      {loading && <Loader />}
      {error && notifyError(error)}
    </div>
  );
}
