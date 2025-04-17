import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

/**
 * Success toast
 */
export const notifySuccess = (message) => {
  toast.success(message, { position: 'top-right' });
};

/**
 * Error toast
 */
export const notifyError = (message) => {
  toast.error(message, { position: 'top-right' });
};

/**
 * Info toast
 */
export const notifyInfo = (message) => {
  toast.info(message, { position: 'top-right' });
};
