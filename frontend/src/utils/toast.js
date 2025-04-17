// /frontend/src/utils/toast.js
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

/**
 * Success toast
 */
export const notifySuccess = (message) => {
  toast.success(message, {
    position: 'top-right',
    autoClose: 5000, // Adjust auto-close time
    hideProgressBar: false, // Optionally display progress bar
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: 'colored', // Add custom theme if desired
  });
};

/**
 * Error toast
 */
export const notifyError = (message) => {
  toast.error(message, {
    position: 'top-right',
    autoClose: 5000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: 'colored',
  });
};

/**
 * Info toast
 */
export const notifyInfo = (message) => {
  toast.info(message, {
    position: 'top-right',
    autoClose: 5000,
    hideProgressBar: false,
    closeOnClick: true,
    pauseOnHover: true,
    draggable: true,
    progress: undefined,
    theme: 'colored',
  });
};
