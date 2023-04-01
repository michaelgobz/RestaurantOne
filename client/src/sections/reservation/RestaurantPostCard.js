import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';
// @mui
import { alpha, styled } from '@mui/material/styles';
import { Box, Card, Grid, Typography, CardContent, Rating, Button, Stack } from '@mui/material';
// utils
import { fShortenNumber } from '../../utils/formatNumber';
//
import SvgColor from '../../components/svg-color';
import Iconify from '../../components/iconify';


// ----------------------------------------------------------------------

const StyledCardMedia = styled('div')({
  position: 'relative',
  paddingTop: 'calc(100% * 3 / 4)',
});

const StyledTitle = styled(Link)({
  height: 44,
  overflow: 'hidden',
  WebkitLineClamp: 2,
  display: '-webkit-box',
  WebkitBoxOrient: 'vertical',
});


const StyledInfo = styled('div')(({ theme }) => ({
  display: 'flex',
  flexWrap: 'wrap',
  justifyContent: 'flex-end',
  marginTop: theme.spacing(3),
  color: theme.palette.text.disabled,
}));

const StyledCover = styled('img')({
  top: 0,
  width: '100%',
  height: '100%',
  objectFit: 'cover',
  position: 'absolute',
});

// ----------------------------------------------------------------------

RestaurantPostCard.propTypes = {
  restaurant: PropTypes.object.isRequired,
};

export default function RestaurantPostCard({ restaurant }) {

  const { avatar, name, location, description } = restaurant;


  const POST_INFO = [
    { number: 1, icon: 'eva:message-circle-fill' },
    { number: 3, icon: 'eva:eye-fill' },
    { number: 5, icon: 'eva:share-fill' },
  ];

  return (
    <Grid item xs={12} sm={6} md={3}>
      <Card sx={{ position: 'relative' }}>
        <StyledCardMedia
          sx={{
            bgcolor: (theme) => alpha(theme.palette.grey[900], 0.72),
            pt: 'calc(100% * 3 / 4)',

          }}
        >
          <SvgColor
            color="paper"
            src="/assets/icons/shape-avatar.svg"
            sx={{
              width: 80,
              height: 36,
              zIndex: 9,
              bottom: -15,
              position: 'absolute',
              color: 'background.paper',
            }}
          />

          <StyledCover alt={name} src={avatar} />
        </StyledCardMedia>

        <CardContent
          sx={{
            pt: 4,
          }}
        >
          <Typography gutterBottom variant="caption" sx={{ color: 'text.disabled', display: 'block' }}>
            {location}
          </Typography>

          <StyledTitle
            color="inherit"
            variant="subtitle2"
            underline="hover"
          >
            {name}
          </StyledTitle>

          <StyledTitle
            color="inherit"
            variant="subtitle2"
            underline="hover"
          >
            {description}
          </StyledTitle>

          <StyledInfo>
            {POST_INFO.map((info, index) => (
              <Box
                key={index}
                sx={{
                  display: 'flex',
                  alignItems: 'center',
                  ml: index === 0 ? 0 : 1.5,

                }}
              >
                <Iconify icon={info.icon} sx={{ width: 16, height: 16, mr: 0.5 }} />
                <Typography variant="caption">{fShortenNumber(info.number)}</Typography>
              </Box>
            ))}
          </StyledInfo>

<Stack direction="row" alignItems="center" justifyContent="space-between" mb={2} mt={2}>
         <Rating name="disabled" value={3} disabled  sx={{ mb: 2, mt: 2 }} />
            <Button variant="small"
              component={Link}
              to={`/customer/restaurants/${restaurant.id}`}
            sx={{ mb: 2, mt: 2 }}>
              view
          </Button>
</Stack>
        </CardContent>
      </Card>
    </Grid>
  );
}
