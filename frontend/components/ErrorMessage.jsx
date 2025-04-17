import { useTranslation } from 'react-i18next';

const ErrorMessage = () => {
  const { t } = useTranslation();
  return <div>{t('error.internal_server_error')}</div>;
};

export default ErrorMessage;
