import { Navigate, useRoutes } from 'react-router-dom';
// layouts
import DefaultLayout from './layouts/dashboard';
import SimpleLayout from './layouts/simple';
// pages
import RestaurantsPage from './pages/RestaurantPage';
import OrderPage from './pages/OrdersPage';
import LoginPage from './pages/LoginPage';
import SignUpPage from './pages/signupPage';
import Page404 from './pages/Page404';
import ProductsPage from './pages/ProductsPage';
import Checkout from './sections/checkouts/Checkout'
import NewReservation from './sections/reservation/new/NewReservation';
import ForgotPasswordPage from './pages/ForgotPasswordPage';
import ConfirmAccountPage from './pages/ConfirmAccountPage';
import UpdatePasswordPage from './pages/UpdatePasswordPage'
import ProductDetailContainer from './pages/ProductDetailPage';
import RestaurantsDetailsContainer from './pages/RestaurantDetailsPage';



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
          path: 'customer/products/details/:itemId',
          element: <ProductDetailContainer />
        },
        {
          path: 'customer/restaurants/:restaurantId',
          element: <RestaurantsDetailsContainer />
        },
        {
          path: 'customer/checkout/:productId',
          element: <Checkout />,
        },
        {
          path: 'customer/reservations',
          element: <RestaurantsPage />,
        },
        {
          path: "/customer/reservations/new/:restaurantId",
          element: <NewReservation />
        }
        ,

        {
          path: 'customer/orders',
          element: <OrderPage />
        },
        {
          path: 'customer/account',
          element: <OrderPage />
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
      path: 'auth/confirm-account',
      element : <ConfirmAccountPage/>
    },
    {
      path: 'auth/update-password',
      element: <UpdatePasswordPage />
    },
    {
      path: 'auth/forgot-password',
      element: <ForgotPasswordPage />
    },
    {
      element: <SimpleLayout />,
      children: [
        { path: '404', element: <Page404 /> },
      ],
    },
    {
      path: '*',
      element: <Navigate to="/404" />
    }
  ]);

  return routes;
}
