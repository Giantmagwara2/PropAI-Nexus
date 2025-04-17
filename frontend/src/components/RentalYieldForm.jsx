import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { notifyError, notifySuccess } from '../lib/toast';
import axios from 'axios';

export default function RentalYieldForm() {
  const { register, handleSubmit, formState: { errors }, reset } = useForm();
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null); // 💥 New state for the prediction result!

  const onSubmit = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post('/api/rental/predict', {
        property_value: parseFloat(data.property_value),
        monthly_rent: parseFloat(data.monthly_rent),
        location: data.location
      });

      console.log('Rental Yield Prediction Response:', response.data);

      // 💥 Show success toast + update result
      notifySuccess('Rental yield prediction successful!');
      setResult(response.data); 
      reset();
    } catch (error) {
      console.error('Rental Yield Prediction Error:', error);
      notifyError(error.response?.data?.detail || 'Rental yield prediction failed.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      
      {/* Rental Yield Prediction Form */}
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">

        {/* Property Value */}
        <div>
          <label className="block mb-1 font-medium">Property Value (USD)</label>
          <input
            type="number"
            {...register('property_value', { 
              required: 'Property value is required',
              min: { value: 1, message: 'Value must be greater than 0' }
            })}
            className="input"
            placeholder="e.g. 250000"
          />
          {errors.property_value && <p className="text-red-500 text-sm">{errors.property_value.message}</p>}
        </div>

        {/* Monthly Rent */}
        <div>
          <label className="block mb-1 font-medium">Monthly Rent (USD)</label>
          <input
            type="number"
            {...register('monthly_rent', { 
              required: 'Monthly rent is required',
              min: { value: 1, message: 'Rent must be greater than 0' }
            })}
            className="input"
            placeholder="e.g. 2000"
          />
          {errors.monthly_rent && <p className="text-red-500 text-sm">{errors.monthly_rent.message}</p>}
        </div>

        {/* Location */}
        <div>
          <label className="block mb-1 font-medium">Location</label>
          <input
            type="text"
            {...register('location', { 
              required: 'Location is required',
              minLength: { value: 2, message: 'Location name too short' }
            })}
            className="input"
            placeholder="e.g. New York, NY"
          />
          {errors.location && <p className="text-red-500 text-sm">{errors.location.message}</p>}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="btn-primary w-full disabled:opacity-50"
          disabled={loading}
        >
          {loading ? 'Predicting...' : 'Predict Rental Yield'}
        </button>
      </form>

      {/* 🎯 Result Banner */}
      {result && (
        <div className="mt-6 p-6 bg-blue-100 dark:bg-blue-900 rounded-xl shadow-inner animate-fade-in transition">
          <h3 className="text-xl font-bold text-blue-700 dark:text-blue-300 mb-2">
            Rental Yield Prediction
          </h3>
          <p className="text-gray-700 dark:text-gray-200">
            <span className="font-semibold">Location:</span> {result.location}
          </p>
          <p className="text-gray-700 dark:text-gray-200">
            <span className="font-semibold">Estimated Rental Yield:</span> <span className="text-green-600 dark:text-green-400 font-bold">{result.rental_yield}%</span>
          </p>
        </div>
      )}
      
    </div>
  );
}
