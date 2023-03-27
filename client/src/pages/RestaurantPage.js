import { Helmet } from 'react-helmet-async';
import { useState } from 'react';
// @mui
import { Grid, Button, Container, Stack, Typography } from '@mui/material';
// components
import { RestaurantPostCard, RestaurantPostsSort, RestaurantSearch ,ReservationCard } from '../sections/reservation';
// mock
import POSTS from '../_mock/blog';
import LoadingSpinner from '../sections/loadingSpinner/LoadingSpinner';

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
  console.log(api);
  const requestOptions = {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
  };

  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    fetch(api, requestOptions).then((response) => response.json())
      .then((data) => {
        console.log(data.restaurants);
        setRestaurants(data.restaurants);
      }).catch((error) => {
        console.log(error);
      });

  }, []);

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
                Top Cuisines near Legos
              </Typography>
              <Grid container spacing={3}>
                {POSTS.map((post, index) => (
                  <RestaurantPostCard key={post.id} post={post} index={index} />
                ))}
              </Grid>
              <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
                Experiences Trending near kigali
              </Typography>
              <Grid container spacing={3}>
                {POSTS.map((post, index) => (
                  <RestaurantPostCard key={post.id} post={post} index={index} />
                ))}
              </Grid>
            </>
            :
            <LoadingSpinner />
        }
      </Container>
    </>
  );
}
