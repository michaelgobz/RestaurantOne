import Paper from '@mui/material/Paper';
import ProductDetailsMenu from './ProductDetailsMenu';

function ProductDetailsDescription() {

  return (
    <>
      <Paper elevation={10} sx={{
        my: 3,
      }}>
        < ProductDetailsMenu />
      </Paper>
    </>

  )

};

export default ProductDetailsDescription;