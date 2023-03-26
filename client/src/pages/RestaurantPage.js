import { Helmet } from 'react-helmet-async';
// @mui
import { Grid, Button, Container, Stack, Typography } from '@mui/material';
// components
import { RestaurantPostCard, RestaurantPostsSort, RestaurantSearch ,ReservationCard } from '../sections/reservation';
// mock
import POSTS from '../_mock/blog';

// ----------------------------------------------------------------------

const api = `${process.env.REACT_APP_API}/dashboard/restaurants`;
console.log(api);
const requestOptions = {
  method: 'GET',
  headers: { 'Content-Type': 'application/json' },
};

fetch(api, requestOptions).then((response) => response.json())
  .then((data) => {
    console.log(data);
  }).catch((error) => {
    console.log(error);
  });


// ----------------------------------------------------------------------

const SORT_OPTIONS = [
  { value: 'latest', label: 'Latest' },
  { value: 'popular', label: 'Popular' },
  { value: 'oldest', label: 'Oldest' },
];

// ----------------------------------------------------------------------

export default function RestaurantsPage() {
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

        <Stack mb={5} direction="row" alignItems="center" justifyContent="space-between">
          <RestaurantSearch posts={POSTS} />
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
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
          Popular Restaurants Lome'
        </Typography>
        <Grid container spacing={3}>
          {POSTS.map((post, index) => (
            <RestaurantPostCard key={post.id} post={post} index={index} />
          ))}
        </Grid>
      </Container>
    </>
  );
}
