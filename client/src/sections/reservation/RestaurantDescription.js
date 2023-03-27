import Paper from '@mui/material/Paper';
import PropTypes from 'prop-types';
import RestaurantDetailsMenu from './DetailsMenu';


RestaurantDetailsDescription.propTypes = {
    description: PropTypes.string.isRequired,
    menus: PropTypes.array.isRequired,
}

function RestaurantDetailsDescription({ description, menus }) {

    return (
        <>
            <Paper elevation={8} sx={{ my: 3 }}>
                <RestaurantDetailsMenu description={description} menus={menus} />
            </Paper>
        </>

    )

};

export default RestaurantDetailsDescription;
