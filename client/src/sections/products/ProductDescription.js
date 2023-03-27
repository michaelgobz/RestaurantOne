import PropTypes from 'prop-types';
import Paper from '@mui/material/Paper';
import ProductDetailsMenu from './ProductDetailsMenu';


ProductDetailsDescription.propTypes = {
  data: PropTypes.shape({
    description: PropTypes.object.isRequired,
    duration: PropTypes.number.isRequired,
    rating: PropTypes.number.isRequired,
    foods: PropTypes.string.isRequired,
    category: PropTypes.string.isRequired,
  })
};

function ProductDetailsDescription({ data }) {

  return (
    <>
      <Paper elevation={10} sx={{
        my: 3,
      }}>
        < ProductDetailsMenu data={data} />
      </Paper>
    </>

  )

};

export default ProductDetailsDescription;