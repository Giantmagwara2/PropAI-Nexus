import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import en from './en.json';
import fr from './fr.json';
import './i18n';


i18n
.use(initReactI18next)
.init({
  resources: { en:{translation:en}, fr:{translation:fr} },
  lng: navigator.language.split('-')[0] || 'en',  // auto-detect
  fallbackLng: 'en',
  interpolation: { escapeValue: false }
  });

export default i18n;
