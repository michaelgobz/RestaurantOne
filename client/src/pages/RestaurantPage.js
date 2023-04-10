import { Helmet } from 'react-helmet-async';
import { useState, useEffect } from 'react';
// @mui
import { Grid, Container, Stack, Typography } from '@mui/material';
// components
import { RestaurantPostCard, RestaurantPostsSort } from '../sections/reservation';
// mock
import {LoadingSpinner} from '../sections/loadingspinner';

// ----------------------------------------------------------------------



// ----------------------------------------------------------------------

const SORT_OPTIONS = [
  { value: 'latest', label: 'Latest' },
  { value: 'popular', label: 'Popular' },
  { value: 'oldest', label: 'Oldest' },
];

// ----------------------------------------------------------------------

export default function RestaurantsPage() {

  const api = `${process.env.REACT_APP_API}/dashboard/restaurants`;

  const [restaurants, setRestaurants] = useState();

  useEffect(() => {

    // request options
    const requestOptions = {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' },
    };

    fetch(api, requestOptions).then((response) => response.json())
      .then((data) => {
        console.log(data.restaurants);
        setRestaurants(data.restaurants);
      }).catch((error) => {
        console.log(error);
      });

  }, [api]);

  return (
    <>
      <Helmet>
        <title> Find a spot | Open Restaurants </title>
      </Helmet>

      <Container>
        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
          <Typography variant="h4" gutterBottom>
           Find your Table for any Treat
          </Typography>
        </Stack>
        {
          restaurants ?

            <>
              <Stack mb={5} direction="row" alignItems="center" justifyContent="space-between">
                <RestaurantPostsSort options={SORT_OPTIONS} />
              </Stack>

              <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
                Top Cuisines 
              </Typography>

              <Grid container spacing={3}>
                {restaurants.map((restaurant) => (
                  <RestaurantPostCard key={restaurant.id} restaurant={restaurant} />
                ))}
              </Grid>

            </>
            :
            <LoadingSpinner text='loading Places ...'/>
        }
      </Container>
    </>
  );
}
