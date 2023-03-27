import { useState, useContext, useEffect } from "react";
import PropTypes from "prop-types";
import { Link } from 'react-router-dom';
// mui components
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Divider from '@mui/material/Divider';
import Box from '@mui/material/Box';
import AssignmentTurnedInIcon from '@mui/icons-material/AssignmentTurnedIn';
// custom components
import SnackBar from '../snackbar/SnackBar';
// context
import { CartContext } from '../../contexts/CartContext';
import ItemCount from './ProductItemCount';
import GoBackButton from '../../utils/GoBackButton';
import ProductDetailsDescription from "./ProductDescription";

ProductDetails.propTypes = {
  Product: PropTypes.shape({
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
    price: PropTypes.number.isRequired,
    description: PropTypes.object.isRequired,
    avatar: PropTypes.string.isRequired,
    duration: PropTypes.number.isRequired,
    category: PropTypes.string.isRequired,
    foods: PropTypes.string.isRequired,
    rating: PropTypes.number.isRequired,
  })
};



export default function ProductDetails({ Product }) {

  // const { addItemToCart, isInCart } = useContext(CartContext);
  const { name, price, description, duration, avatar, rating, foods, category, id } = Product;
  const { showSnackbar, setShowSnackbar } = useState(false)
  const [data, setData] = useState({});

  useEffect(() => {
    setData({ description, duration, rating, foods, category })
  }, [])


  return (
    <>
      <Grid
        container
        mt={5}
        className='animate__animated animate__fadeIn'
        spacing={3}
      >
        <Grid
          item
          sm={6}
          md={4}
          className='animate__animated animate__fadeInLeft'
        >
          <Card raised>
            <CardMedia component='img' image={`/assets/images/products/product_${1}.jpg`} alt={'id'} />
          </Card>
          <Box
            display='flex'
            justifyContent='space-between'
            mt={1}
            alignContent='center'
          >
            <GoBackButton sx={{ my: 5 }} />

            <Typography component='h5' variant='h6' textAlign='center' sx={{ my: 5 }}>
              {price}
            </Typography>
          </Box>
        </Grid>

        <Grid item xs={8} sm={6} md={8}>
          <Typography component='body6' align='center' sx={{
            my: 5,
            textAlign: 'center',
            fontSize: '1.5rem',
          }} gutterBottom>
            {name}
          </Typography>
          <Divider sx={{ my: 5 }} />

          <ProductDetailsDescription data={data} />
          <Divider sx={{ mb: 2 }} />

          <Box display='flex' justifyContent={'center'} my>

              <Button
              variant='contained'
              startIcon={<AssignmentTurnedInIcon />}
              component={Link}
              sx={{ my: 5 }}
              to={`/customer/checkout/${id}`}
              >
              Add to cart
            </Button>
          </Box>
        </Grid>
      </Grid>
      {showSnackbar && (
        <SnackBar message={'Added item '} severity={'success'} />
      )}
    </>
  )

}