import React from 'react';
import { useForm } from 'react-hook-form';
import { notifyError, notifySuccess } from '../lib/toast';

export default function PredictionForm() {
  const { register, handleSubmit, formState: { errors }, reset } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    notifySuccess('Property prediction submitted successfully!');
    reset();
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {/* Size */}
      <div>
        <label className="block mb-1 font-medium">Property Size (sqft)</label>
        <input
          type="number"
          {...register('size', { required: 'Size is required', min: { value: 1, message: 'Size must be positive' } })}
          className="input"
        />
        {errors.size && <p className="text-red-500 text-sm">{errors.size.message}</p>}
      </div>

      {/* Bedrooms */}
      <div>
        <label className="block mb-1 font-medium">Bedrooms</label>
        <input
          type="number"
          {...register('bedrooms', { required: 'Bedrooms required', min: { value: 1, message: 'Must have at least 1 bedroom' } })}
          className="input"
        />
        {errors.bedrooms && <p className="text-red-500 text-sm">{errors.bedrooms.message}</p>}
      </div>

      {/* Bathrooms */}
      <div>
        <label className="block mb-1 font-medium">Bathrooms</label>
        <input
          type="number"
          {...register('bathrooms', { required: 'Bathrooms required', min: { value: 1, message: 'Must have at least 1 bathroom' } })}
          className="input"
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
        />
        {errors.location && <p className="text-red-500 text-sm">{errors.location.message}</p>}
      </div>

      {/* Age */}
      <div>
        <label className="block mb-1 font-medium">Property Age (years)</label>
        <input
          type="number"
          {...register('age', { required: 'Age is required', min: { value: 0, message: 'Age cannot be negative' } })}
          className="input"
        />
        {errors.age && <p className="text-red-500 text-sm">{errors.age.message}</p>}
      </div>

      {/* Submit Button */}
      <button type="submit" className="btn-primary w-full">
        Predict Property Value
      </button>
    </form>
  );
}
