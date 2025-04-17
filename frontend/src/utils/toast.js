// /frontend/src/utils/toast.js
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

/**
 * Success toast
 */
export const notifySuccess = (message) => {
  toast.success(message, {
    position: 'top-right',
    style: {
      backgroundColor: '#16a34a', // Tailwind green-600
      color: '#ffffff',
      borderRadius: '8px',
      border: '1px solid #22c55e', // Tailwind green-500
    },
  });
};

/**
 * Error toast
 */
export const notifyError = (message) => {
  toast.error(message, {
    position: 'top-right',
    style: {
      backgroundColor: '#dc2626', // Tailwind red-600
      color: '#ffffff',
      borderRadius: '8px',
      border: '1px solid #ef4444', // Tailwind red-500
    },
  });
};

/**
 * Info toast
 */
export const notifyInfo = (message) => {
  toast.info(message, {
    position: 'top-right',
    style: {
      backgroundColor: '#2563eb', // Tailwind blue-600
      color: '#ffffff',
      borderRadius: '8px',
      border: '1px solid #3b82f6', // Tailwind blue-500
    },
  });
};
