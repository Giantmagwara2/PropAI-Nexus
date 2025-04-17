import { TailSpin } from 'react-loader-spinner';

const Loader = () => (
  <div className="loader">
    <TailSpin height={50} width={50} color="#4fa94d" ariaLabel="loading" />
  </div>
);

export default Loader;
