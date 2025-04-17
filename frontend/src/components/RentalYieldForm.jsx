import React from 'react';
import { useForm } from 'react-hook-form';
import { notifyError, notifySuccess } from '../lib/toast';

export default function RentalYieldForm() {
  const { register, handleSubmit, formState: { errors }, reset } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    notifySuccess('Rental yield prediction submitted successfully!');
    reset();
  };

  return (
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
      <button type="submit" className="btn-primary w-full">
        Predict Rental Yield
      </button>
    </form>
  );
}
