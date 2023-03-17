import { Helmet } from 'react-helmet-async';
import { useState } from 'react';
// @mui
import { Container, Stack, Typography } from '@mui/material';
// components
import { ProductSort, ProductList, ProductFilterSidebar } from '../sections/@default/products';
// mock
// we should provide an array of product categories
import PRODUCTS from '../_mock/products';
import ProductCartPopover from '../sections/@default/products/ProductCartPopover';

// ----------------------------------------------------------------------

export default function ProductsPage() {
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

        <ProductList products={PRODUCTS} />
        <Typography variant="h4" sx={{ mb: 5 , mt: 5}}>
          Coco Tails
        </Typography>
        <ProductList products={PRODUCTS} />
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
        Take Away
        </Typography>
        <ProductList products={PRODUCTS} />
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
        Barques 
        </Typography>
        <ProductList products={PRODUCTS} />
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
        Burgers
        </Typography>
        <ProductList products={PRODUCTS} />
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
        Cakes
        </Typography>
        <ProductList products={PRODUCTS} />
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
        Ice cream
        </Typography>
        <ProductList products={PRODUCTS} />
        <ProductCartPopover />
      </Container>
    </>
  );
}
