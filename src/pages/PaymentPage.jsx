import React from 'react';
import StripeContainer from '../components/Payments/StripeContainer';

const PaymentPage = () => {
  return (
    <div className="payment-page">
      <h2>Complete Your Payment</h2>
      <StripeContainer />
    </div>
  );
};

export default PaymentPage;
