import { Helmet } from 'react-helmet-async';
import { useEffect, useState } from 'react';
// @mui
import { Container, Stack, Typography } from '@mui/material';
import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';
// components
import { ProductSort, ProductList, ProductFilterSidebar } from '../sections/products';
// mock
// we should provide an array of product categories
import PRODUCTS from '../_mock/products';


// ----------------------------------------------------------------------


export default function ProductsPage() {

  // get the data 
  const api = `${process.env.REACT_APP_API}/dashboard/menus`;
  console.log(api);
  // menus state
  const [menus, setMenus] = useState();
  // request options
  const requestOptions = {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
  };

  useEffect(() => {
    // fetch the data
    fetch(api, requestOptions).then((response) => response.json())
      .then((data) => {
        console.log(data.menus);
        setMenus(data.menus);
      }).catch((error) => {
        console.log(error);
      });
  }, []);
  sessionStorage.setItem('signup', 'true')
  const [openFilter, setOpenFilter] = useState(false);

  const handleOpenFilter = () => {
    setOpenFilter(true);
  };

  const handleCloseFilter = () => {
    setOpenFilter(false);
  };

  return (
    <>
      <Helmet>
        <title> Your Cravings | Open Restaurant </title>
      </Helmet>
      {
        menus ?
          <Container>

            <Typography variant="h4" sx={{ mb: 5 }}>
              Your Cravings Solved
            </Typography>
            <Stack direction="row" flexWrap="wrap-reverse" alignItems="center" justifyContent="flex-end" sx={{ mb: 5 }}>
              <Stack direction="row" spacing={1} flexShrink={0} sx={{ my: 1 }}>
                <ProductFilterSidebar
                  openFilter={openFilter}
                  onOpenFilter={handleOpenFilter}
                  onCloseFilter={handleCloseFilter}
                />
                <ProductSort />
              </Stack>
            </Stack>
            {
              menus.map((menu) => (
                <>
                  <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
                    {menu.name}
                  </Typography>
                  <ProductList products={menu.items} />
                </>
              ))
            }
          </Container>
          :
          <LoadingSpinner />
      }
    </>
  );
}
