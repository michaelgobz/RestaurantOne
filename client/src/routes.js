import { Navigate, useRoutes } from 'react-router-dom';
// layouts
import DefaultLayout from './layouts/dashboard';
import SimpleLayout from './layouts/simple';
// pages
import RestaurantsPage from './pages/RestaurantPage';
import UserPage from './pages/UserPage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/signupPage';
import Page404 from './pages/Page404';
import ProductsPage from './pages/ProductsPage';
import CartCheckout from './pages/CheckoutsPage'

// ----------------------------------------------------------------------

export default function Router() {
  const routes = useRoutes([
    {
      path: '/',
      element: <DefaultLayout />,
      children: [
        {
          element: <Navigate to="customer/products" />,
          index: true
        },
        {
          path: 'customer/products',
          element: <ProductsPage />
        },
        {
          path: 'customer/checkout',
          element: <CartCheckout />,
          children:
            [
              {
                path: 'new/:id',
                element: <ProductsPage />
              }
            ]
        },
        {
          path: 'customer/reservations',
          element: <RestaurantsPage />,
          children:
            [
              {
                path: 'new/:id',
                element: <UserPage />
              }
            ]
        },
        {
          path: 'customer/orders',
          element: <UserPage />
        },
        {
          path: 'customer/account',
          element: <UserPage />
        },
      ],
    },
    {
      path: 'auth/signup',
      element: <SignUpPage />
    },
    {
      path: 'auth/login',
      element: <LoginPage />
    },
    {
      element: <SimpleLayout />,
      children: [
        { path: '404', element: <Page404 /> },
      ],
    },
  ]);

  return routes;
}
