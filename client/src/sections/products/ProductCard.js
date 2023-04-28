import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
// @mui
import { Box, Card, Typography, Stack, Rating, Button } from '@mui/material';
import { styled } from '@mui/material/styles';
// utils
import { fCurrency } from '../../utils/formatNumber';
// components
import Label from '../../components/label';

// ----------------------------------------------------------------------

const StyledProductImg = styled('img')({
  top: 0,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute',
});

// ----------------------------------------------------------------------

ShopProductCard.propTypes = {
  product: PropTypes.object,
};

export default function ShopProductCard({ product }) {
  const { name, avatar, price, description, rating, duration, id } = product;

  return (
    <Card>
      <Box sx={{ pt: '100%', position: 'relative' }}>
        {duration && (
          <Label
            variant="filled"
            color="info"
            sx={{
              zIndex: 9,
              top: 16,
              right: 16,
              position: 'absolute',
              textTransform: 'uppercase',
            }}
          >
            {`delivered ${duration} mins`}
          </Label>
        )}
        <StyledProductImg alt={name} src={avatar} />
      </Box>

      <Stack spacing={2} sx={{ p: 3 }}>
        <Link color="inherit" underline="hover">
          <Typography variant="subtitle2" noWrap>
            {name}
          </Typography>
        </Link>

        <Stack direction="column" alignItems="center" justifyContent="space-between">
          <Typography
              component="span"
              variant="body1"
              sx={{
                color: 'text.secondary',
                my: 0.5,

              }}
            >
            {description}
          </Typography> 
          <Typography variant="subtitle1" sx={{ my: 0.5 }}>
            {fCurrency(price)}
          </Typography>

          <Stack direction="column" alignItems="center" justifyContent="space-between" mb={0.2} mt={0.2}>
            <Rating variant="small" value={rating} disabled sx={{ mb: 2, mt: 2 }} />
            <Button variant="small" component={Link} to={`/customer/products/details/${id}`}
              sx={{ mb: 0.1, mt: 0.1 }}>
              view
            </Button>
          </Stack>
        </Stack>
      </Stack>
    </Card>
  );
}
