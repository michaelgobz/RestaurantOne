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
// context
import GoBackButton from '../../utils/GoBackButton';
import RestaurantDetailsDescription from "./RestaurantDescription";


RestaurantDetails.propTypes = {
    Restaurant: PropTypes.shape({
        id: PropTypes.string.isRequired,
        name: PropTypes.string.isRequired,
        description: PropTypes.object.isRequired,
        avatar: PropTypes.string.isRequired,
        customers: PropTypes.number.isRequired,
        menus: PropTypes.array.isRequired,
    })
}


export default function RestaurantDetails({ Restaurant }) {

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
                        <CardMedia component='img' image={`/assets/images/products/product_${5}.jpg`} alt={Restaurant} />
                    </Card>
                    <Box
                        display='flex'
                        justifyContent='space-between'
                        mt={1}
                        alignContent='center'
                    >
                        <GoBackButton sx={{ my: 5 }} />

                        <Typography component='h5' variant='h6' textAlign='center'
                            sx={{ my: 5 }}
                        >
                            ${Restaurant.customers}
                        </Typography>
                    </Box>
                </Grid>

                <Grid item xs={12} sm={6} md={8}>

                    <Typography component='body6' align='center' sx={{
                        my: 5,
                        textAlign: 'center',
                        fontSize: '1.5rem',
                    }} gutterBottom>
                        {Restaurant.name}
                    </Typography>
                    <Divider sx={{ my: 5 }} />

                    <RestaurantDetailsDescription sx={{ my: 5 }}
                        description={Restaurant.description} menus={Restaurant.menus} />

                    <Divider sx={{ mb: 2 }} />

                    <Box display='flex' justifyContent={'center'} my>
                        <Button
                            variant='contained'
                            startIcon={<AssignmentTurnedInIcon />}
                            component={Link}
                            to={`/customer/reservations/new/${Restaurant.id}`}
                        >
                            Reserve
                        </Button>

                    </Box>
                </Grid>
            </Grid>
        </>
    )

}