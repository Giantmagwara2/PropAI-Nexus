import axios from 'axios';

// Set up axios instance
const apiClient = axios.create({
  baseURL: process.env.REACT_APP_API_BASE_URL, // Make sure to set this in .env
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.REACT_APP_API_KEY}`, // Use your real API key
  },
});

// Property prediction API call
export const predictPropertyValue = async (propertyData) => {
  try {
    const response = await apiClient.post('/api/predictions/property', propertyData);
    return response.data;
  } catch (error) {
    console.error('Error predicting property value:', error);
    throw error;
  }
};

// Rental yield prediction API call
export const predictRentalYield = async (propertyData) => {
  try {
    const response = await apiClient.post('/api/rental/rental-yield', propertyData);
    return response.data;
  } catch (error) {
    console.error('Error predicting rental yield:', error);
    throw error;
  }
};
