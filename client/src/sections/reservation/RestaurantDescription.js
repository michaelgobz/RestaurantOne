import Paper from '@mui/material/Paper';
import RestaurantDetailsMenu from './DetailsMenu';

function RestaurantDetailsDescription() {

    return (
        <>
            <Paper elevation={8} sx={{ my: 3 }}>
                <RestaurantDetailsMenu />
            </Paper>
        </>

    )

};

export default RestaurantDetailsDescription;
