import ReactGA from 'react-ga';

export const initGA = () => {
  ReactGA.initialize('UA-XXXXXXX-X');
};
export const logPageView = () => {
  ReactGA.pageview(window.location.pathname + window.location.search);
};
export const logEvent = (category, action) => {
  ReactGA.event({ category, action });
};
