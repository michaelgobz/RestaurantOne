import { Navigate, useRoutes } from 'react-router-dom';
// layouts
import DashboardLayout from './layouts/dashboard';
import SimpleLayout from './layouts/simple';
//
import BlogPage from './pages/BlogPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/signupPage';
import Page404 from './pages/Page404';
import ProductsPage from './pages/ProductsPage';
import DashboardAppPage from './pages/DashboardAppPage';

// ----------------------------------------------------------------------

export default function Router() {
  const routes = useRoutes([
    {
      path: '/customer',
      element: <DashboardLayout />,
      children: [
        {
          element: <Navigate to="/customer/products" />,
          index: true
        },
        {
          path: 'checkout',
          element: <DashboardAppPage />,
          children:
            [
              {
                path: 'new/:id',
                element: <ProductsPage />
              }
            ]
        },
        {
          path: 'reservations', element: <UserPage />,
          children:
            [
              { path: 'new/:id', element: <ProductsPage /> }
            ]
        },
        {
          path: 'orders', element: <BlogPage />
        },
        {
          path: 'Account', element: <UserPage />
        }
      ],
    },
    {
      path: 'auth/login',
      element: <LoginPage />,
    },
    {
      path: 'auth/signup',
      element: <SignUpPage />
    },
    {
      path: 'products',
      element: <ProductsPage />,
    },
    {
      element: <SimpleLayout />,
      children: [
        { path: '404', element: <Page404 /> },
        { path: '*', element: <Navigate to="/404" /> },
      ],
    },
    {
      path: '*',
      element: <Navigate to="/404" replace />,
    },
  ]);

  return routes;
}
