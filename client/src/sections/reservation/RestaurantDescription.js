import Paper from '@mui/material/Paper';
import RestaurantDetailsMenu from './DetailsMenu';

//should take in restaurant details as props

const RestaurantDetails = () => (
    <>
        <Paper elevation={8} sx={{ my: 3 }}>
            <RestaurantDetailsMenu />
        </Paper>
    </>

);

export default RestaurantDetails;
