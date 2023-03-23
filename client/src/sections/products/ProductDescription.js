import Paper from '@mui/material/Paper';
import RestaurantDetailsMenu from '../reservation/DetailsMenu';

function RestaurantDetails() {

  return (
    <>
      <Paper elevation={8} sx={{ my: 3 }}>
        <RestaurantDetailsMenu />
      </Paper>
    </>

  )

};

export default RestaurantDetails;