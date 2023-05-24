import { useLocation, Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth.js';

const RequireAuth = () => {
  const isAuth = useAuth();
  const location = useLocation();
  console.log('auth is ' + isAuth);

  return isAuth ? (
    <Outlet />
  ) : (
    <Navigate to='/register' state={{ from: location }} replace />
  );
};
export default RequireAuth;
