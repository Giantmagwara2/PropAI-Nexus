import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { notifyError, notifySuccess } from '../lib/toast';
import axios from 'axios';

export default function PredictionForm() {
  const { register, handleSubmit, formState: { errors }, reset } = useForm();
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null); // 🔥 New: store the prediction result

  const onSubmit = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post('/api/predictions/predict', {
        size: parseFloat(data.size),
        bedrooms: parseInt(data.bedrooms),
        bathrooms: parseInt(data.bathrooms),
        location: data.location,
        age: parseInt(data.age)
      });

      console.log('Property Value Prediction Response:', response.data);

      // 🔥 Update result and notify
      notifySuccess('Property value prediction successful!');
      setResult(response.data); 
      reset();
    } catch (error) {
      console.error('Property Value Prediction Error:', error);
      notifyError(error.response?.data?.detail || 'Property value prediction failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">

      {/* Property Value Prediction Form */}
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">

        {/* Property Size */}
        <div>
          <label className="block mb-1 font-medium">Property Size (sqft)</label>
          <input
            type="number"
            {...register('size', { required: 'Property size is required', min: { value: 10, message: 'Size must be realistic' } })}
            className="input"
            placeholder="e.g. 1500"
          />
          {errors.size && <p className="text-red-500 text-sm">{errors.size.message}</p>}
        </div>

        {/* Bedrooms */}
        <div>
          <label className="block mb-1 font-medium">Number of Bedrooms</label>
          <input
            type="number"
            {...register('bedrooms', { required: 'Bedrooms are required', min: { value: 0, message: 'Must be 0 or more' } })}
            className="input"
            placeholder="e.g. 3"
          />
          {errors.bedrooms && <p className="text-red-500 text-sm">{errors.bedrooms.message}</p>}
        </div>

        {/* Bathrooms */}
        <div>
          <label className="block mb-1 font-medium">Number of Bathrooms</label>
          <input
            type="number"
            {...register('bathrooms', { required: 'Bathrooms are required', min: { value: 0, message: 'Must be 0 or more' } })}
            className="input"
            placeholder="e.g. 2"
          />
          {errors.bathrooms && <p className="text-red-500 text-sm">{errors.bathrooms.message}</p>}
        </div>

        {/* Location */}
        <div>
          <label className="block mb-1 font-medium">Location</label>
          <input
            type="text"
            {...register('location', { required: 'Location is required' })}
            className="input"
            placeholder="e.g. Los Angeles, CA"
          />
          {errors.location && <p className="text-red-500 text-sm">{errors.location.message}</p>}
        </div>

        {/* Property Age */}
        <div>
          <label className="block mb-1 font-medium">Property Age (years)</label>
          <input
            type="number"
            {...register('age', { required: 'Age is required', min: { value: 0, message: 'Age cannot be negative' } })}
            className="input"
            placeholder="e.g. 5"
          />
          {errors.age && <p className="text-red-500 text-sm">{errors.age.message}</p>}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="btn-primary w-full disabled:opacity-50"
          disabled={loading}
        >
          {loading ? 'Predicting...' : 'Predict Property Value'}
        </button>
      </form>

      {/* 🎯 Result Banner */}
      {result && (
        <div className="mt-6 p-6 bg-green-100 dark:bg-green-900 rounded-xl shadow-inner animate-fade-in transition">
          <h3 className="text-xl font-bold text-green-700 dark:text-green-300 mb-2">
            Property Value Prediction
          </h3>
          <p className="text-gray-700 dark:text-gray-200">
            <span className="font-semibold">Location:</span> {result.location}
          </p>
          <p className="text-gray-700 dark:text-gray-200">
            <span className="font-semibold">Estimated Value:</span> <span className="text-blue-600 dark:text-blue-400 font-bold">${result.predicted_value?.toLocaleString()}</span>
          </p>
        </div>
      )}
      
    </div>
  );
}
