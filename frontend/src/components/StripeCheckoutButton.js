import React from 'react';
import { loadStripe } from '@stripe/stripe-js';

const stripePromise = loadStripe(process.env.REACT_APP_STRIPE_PUBLIC_KEY);

export default function StripeCheckoutButton({ amount, description }) {
  const handleClick = async () => {
    const stripe = await stripePromise;
    const response = await fetch('/api/payments/create-checkout-session/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'x-api-key': process.env.REACT_APP_API_KEY },
      body: JSON.stringify({ amount, description })
    });
    const session = await response.json();
    const result = await stripe.redirectToCheckout({
      sessionId: session.id,
    });
    if (result.error) {
      console.error(result.error.message);
    }
  };

  return (
    <button onClick={handleClick} className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition">
      Pay ${amount / 100} for {description}
    </button>
  );
}
