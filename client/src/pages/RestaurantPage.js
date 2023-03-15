import { Helmet } from 'react-helmet-async';
// @mui
import { Grid, Button, Container, Stack, Typography } from '@mui/material';
// components
import Iconify from '../components/iconify';
import { RestaurantPostCard, RestaurantPostsSort, RestaurantSearch } from '../sections/@default/reservation';
// mock
import POSTS from '../_mock/blog';

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
        <title> Restaurants | Open Restaurants </title>
      </Helmet>

      <Container>
        <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
          <Typography variant="h4" gutterBottom>
            Restaurants
          </Typography>
          <Button variant="contained" startIcon={<Iconify icon="eva:plus-fill" />}>
            New Reservation
          </Button>
        </Stack>

        <Stack mb={5} direction="row" alignItems="center" justifyContent="space-between">
          <RestaurantSearch posts={POSTS} />
          <RestaurantPostsSort options={SORT_OPTIONS} />
        </Stack>

        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
          5 Star
        </Typography>
        <Grid container spacing={3}>
          {POSTS.map((post, index) => (
            <RestaurantPostCard key={post.id} post={post} index={index} />
          ))}
        </Grid>
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
          Kampala
        </Typography>
        <Grid container spacing={3}>
          {POSTS.map((post, index) => (
            <RestaurantPostCard key={post.id} post={post} index={index} />
          ))}
        </Grid>
        <Typography variant="h4" sx={{ mb: 5, mt: 5 }}>
          Lome'
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
