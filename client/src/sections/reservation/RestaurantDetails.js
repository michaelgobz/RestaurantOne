import { useState, useContext } from "react";
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
import { CartContext } from '../../contexts/CartContext';
import GoBackButton from '../../utils/GoBackButton';



ProductDetails.propTypes = {
    Product: PropTypes.shape({
        id: PropTypes.string.isRequired,
        title: PropTypes.string.isRequired,
        price: PropTypes.number.isRequired,
        description: PropTypes.object.isRequired,
        imgPath: PropTypes.string.isRequired,
        stock: PropTypes.number.isRequired,
    }).isRequired
}


export default function RestaurantDetails() {

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
                        <CardMedia component='img' image={'imgPath'} alt={'id'} />
                    </Card>
                    <Box
                        display='flex'
                        justifyContent='space-between'
                        mt={1}
                        alignContent='center'
                    >
                        <GoBackButton />

                        <Typography component='h5' variant='h6' textAlign='center'>
                            ${price}
                        </Typography>
                    </Box>
                </Grid>

                <Grid item xs={12} sm={6} md={8}>
                    <Divider />

                    <RestaurantDetails />

                    <Divider sx={{ mb: 2 }} />

                    <Box display='flex' justifyContent={'center'} my>
                        <Button
                            variant='contained'
                            color='error'
                            startIcon={<AssignmentTurnedInIcon />}
                            component={Link}
                            to='/customer/reservation/new'
                        >
                            Reserve
                        </Button>

                    </Box>
                </Grid>
            </Grid>
        </>
    )

}