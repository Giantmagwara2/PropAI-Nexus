// /frontend/src/pages/Home.jsx
import React from 'react';
import { motion, useScroll, useTransform } from 'framer-motion';
import { WavyContainer, WavyBackground } from 'react-wavy-transitions';
import Confetti from 'react-confetti';
import PredictionForm from '../components/PredictionForm';
import RentalYieldForm from '../components/RentalYieldForm';
import ScrollButton from '../components/ScrollButton'; // 👈🏽 Add at the top
import { useTheme } from '../context/ThemeContext';

export default function Home() {
  const { scrollY } = useScroll();
  const yOffset = useTransform(scrollY, [0, 500], [0, -100]);

  return (
    <motion.div 
      className="min-h-screen p-6 md:p-10 bg-gray-50 dark:bg-gray-900 transition-colors duration-300"
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8, ease: 'easeOut' }}
    >
      {/* Sparkles Confetti */}
      <div className="fixed top-0 left-0 w-full h-48 pointer-events-none z-10">
        <Confetti
          width={window.innerWidth}
          height={200}
          numberOfPieces={50}
          gravity={0.05}
          recycle={true}
          colors={['#3B82F6', '#60A5FA', '#93C5FD', '#BFDBFE']}
          initialVelocityX={{ min: -2, max: 2 }}
          initialVelocityY={{ min: -3, max: 0 }}
          opacity={0.7}
        />
      </div>

      {/* Hero Section */}
      <section className="relative overflow-hidden text-center mb-0">
        
        {/* Parallax Background */}
        <motion.div 
          className="absolute inset-0 bg-gradient-to-br from-blue-100 to-blue-300 dark:from-blue-800 dark:to-blue-900 opacity-20 pointer-events-none rounded-3xl blur-3xl"
          style={{ y: yOffset }}
        />

        <motion.h2 className="text-sm md:text-lg text-blue-600 dark:text-blue-400 font-semibold mb-2 uppercase tracking-wider relative"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.2, duration: 0.6 }}
        >
          AI-Powered Real Estate Insights
        </motion.h2>

        <motion.h1 className="text-4xl md:text-5xl font-extrabold text-gray-800 dark:text-white mb-4 leading-tight relative"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4, duration: 0.8 }}
        >
          Property Prediction Platform
        </motion.h1>

        <motion.p className="text-gray-600 dark:text-gray-300 max-w-2xl mx-auto text-base md:text-lg relative"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.6, duration: 1 }}
        >
          Get instant property value and rental yield estimates powered by advanced AI models.
          Make smarter investment decisions today!
        </motion.p>

      </section>

      {/* Section Separator */}
      <WavyContainer height="150px" bgColor="#F9FAFB" waveColor="#3B82F6">
        <WavyBackground />
      </WavyContainer>

      {/* Forms Section */}
      <section className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-8">
        
        <motion.div 
          className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg hover:scale-105 hover:shadow-2xl transition duration-300 cursor-pointer"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, ease: 'easeOut' }}
          viewport={{ once: true, amount: 0.3 }}
        >
          <h3 className="text-2xl font-bold text-center text-gray-800 dark:text-white mb-6">
            Property Value Prediction
          </h3>
          <PredictionForm />
        </motion.div>

        <motion.div 
          className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg hover:scale-105 hover:shadow-2xl transition duration-300 cursor-pointer"
          initial={{ opacity: 0, y: 50 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.8, ease: 'easeOut' }}
          viewport={{ once: true, amount: 0.3 }}
        >
          <h3 className="text-2xl font-bold text-center text-gray-800 dark:text-white mb-6">
            Rental Yield Prediction
          </h3>
          <RentalYieldForm />
        </motion.div>

      </section>

    <ScrollButton />

    </motion.div>
  );
}
