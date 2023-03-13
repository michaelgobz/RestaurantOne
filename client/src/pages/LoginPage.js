import { Helmet } from 'react-helmet-async';
// @mui
import { styled, useTheme } from '@mui/material/styles';
import { Link, Container, Typography, Divider, Stack, Button } from '@mui/material';
// hooks
import useResponsive from '../hooks/useResponsive';
// components
import Iconify from '../components/iconify';
// sections
import { LoginForm } from '../sections/auth/login';
import { handleGoogleLogin, handleGithubLogin, handleTwitterLogin } from '../utils/authHandlers';


// ----------------------------------------------------------------------

const StyledRoot = styled('div')(({ theme }) => ({
  [theme.breakpoints.up('md')]: {
    display: 'flex',
  },
}));

const StyledSection = styled('div')(({ theme }) => ({
  width: '100%',
  maxWidth: 480,
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  boxShadow: theme.customShadows.card,
  backgroundColor: theme.palette.background.default,
}));

const StyledContent = styled('div')(({ theme }) => ({
  maxWidth: 480,
  margin: 'auto',
  minHeight: '100vh',
  display: 'flex',
  justifyContent: 'center',
  flexDirection: 'column',
  padding: theme.spacing(12, 0),
}));

const signup = '/auth /signup'


// ----------------------------------------------------------------------

export default function LoginPage() {

  const mdUp = useResponsive('up', 'md');
  const theme = useTheme();
  const PRIMARY_MAIN = theme.palette.primary.main;
  const url = window.location.host + signup;


  return (
    <>
      <Helmet>
        <title> Login | RestaurantOne </title>
      </Helmet>

      <StyledRoot>
  
      {mdUp && (
          <StyledSection>
            <Typography variant="h3" sx={{ px: 5, mt: 10, mb: 5 }}>
              Hi, Welcome Back
            </Typography>
            <svg version="1.0" xmlns="http://www.w3.org/2000/svg"
 width="300pt" height="200pt" viewBox="0 0 512 512"
 preserveAspectRatio="xMidYMid meet">

<g transform="translate(0.000000,500.000000) scale(0.100000,-0.100000)"
fill={PRIMARY_MAIN} stroke="none">
<path d="M2465 4628 c-285 -32 -625 -156 -862 -315 -404 -270 -687 -649 -826
-1110 l-25 -83 61 0 62 0 33 103 c201 626 751 1121 1394 1257 228 48 538 52
753 10 601 -118 1114 -519 1363 -1066 133 -293 178 -519 169 -849 -6 -205 -21
-311 -66 -462 -17 -57 -21 -97 -21 -212 l0 -141 -59 0 -59 0 -48 -82 c-114
-195 -306 -413 -480 -545 -679 -517 -1608 -521 -2289 -10 -175 131 -388 373
-501 569 -36 63 -42 68 -74 68 l-35 1 37 19 c186 98 560 143 1006 121 125 -6
385 -27 577 -46 537 -53 553 -54 822 -65 517 -20 737 21 869 162 82 87 126
227 90 283 -33 50 -66 26 -77 -54 -21 -151 -123 -251 -301 -295 -112 -28 -221
-36 -483 -36 -249 0 -422 12 -985 69 -540 55 -1005 54 -1253 -4 -140 -32 -327
-114 -327 -142 0 -7 -9 -13 -20 -13 -18 0 -16 -6 17 -67 307 -569 850 -953
1479 -1048 134 -20 453 -20 593 0 819 120 1484 741 1664 1555 152 684 -66
1401 -572 1882 -327 312 -729 499 -1173 547 -114 13 -339 12 -453 -1z"/>
<path d="M2520 4364 c-665 -81 -1223 -517 -1450 -1135 -35 -93 -36 -109 -12
-109 13 0 25 21 46 82 86 241 222 453 412 640 111 109 190 171 314 245 487
292 1112 320 1615 70 405 -200 705 -534 857 -954 23 -65 34 -83 49 -83 25 0
24 4 -11 101 -217 589 -718 1010 -1335 1125 -87 16 -405 28 -485 18z"/>
<path d="M2465 4131 c-54 -24 -108 -87 -124 -143 -12 -41 -17 -46 -47 -51
-110 -18 -174 -136 -130 -240 18 -44 47 -67 108 -88 l53 -18 0 -90 c0 -77 2
-90 15 -85 99 43 265 56 385 31 l69 -14 -28 22 c-52 41 -134 59 -243 52 -54
-3 -108 -9 -120 -13 -22 -6 -23 -3 -23 43 0 28 -5 64 -11 82 -9 27 -16 31 -45
31 -76 0 -124 47 -124 122 0 57 27 92 85 113 l40 13 14 -41 c8 -23 21 -51 29
-62 l14 -20 -7 20 c-14 39 -17 111 -6 153 14 52 71 118 119 138 51 21 164 18
210 -5 68 -35 112 -104 112 -175 l0 -34 74 -4 c90 -4 125 -25 144 -85 28 -87
-23 -163 -110 -163 -21 0 -38 2 -38 4 0 1 5 17 11 34 7 22 7 36 0 49 -10 17
-10 17 -11 -1 0 -31 -49 -94 -94 -122 -38 -23 -39 -24 -11 -18 17 3 38 8 48
11 15 4 17 -3 17 -51 0 -31 5 -56 10 -56 6 0 10 12 10 28 0 60 9 72 54 72 52
0 120 31 141 64 45 68 41 168 -9 224 -35 40 -70 57 -137 67 -43 6 -46 9 -57
50 -16 59 -68 124 -122 151 -59 31 -203 33 -265 5z"/>
<path d="M1390 3183 c-54 -9 -91 -26 -110 -50 -42 -54 -9 -127 48 -107 20 7
27 16 27 34 0 22 -4 25 -32 22 -27 -3 -33 0 -33 16 0 25 29 50 68 58 18 4 33
5 34 3 1 -2 4 -85 7 -184 l6 -180 35 0 35 0 3 176 c3 182 8 207 44 194 19 -7
38 -48 38 -79 0 -28 -19 -86 -28 -86 -4 0 -13 -4 -20 -9 -11 -6 -1 -33 43
-121 69 -138 89 -160 147 -160 24 0 50 5 58 10 13 9 13 10 -1 10 -25 0 -63 49
-108 136 -23 45 -50 90 -60 100 -18 18 -17 20 11 44 63 54 41 147 -40 170 -36
10 -122 11 -172 3z"/>
<path d="M2231 3109 c-12 -16 -33 -34 -47 -39 -27 -10 -33 -30 -9 -30 12 0 15
-19 15 -113 0 -75 4 -117 12 -125 19 -19 82 -15 101 6 21 23 22 39 2 22 -27
-23 -35 0 -35 106 0 98 1 104 21 104 11 0 29 5 40 10 23 13 26 50 3 50 -11 0
-14 -6 -9 -20 5 -17 2 -20 -24 -20 -29 0 -31 2 -31 40 0 48 -9 50 -39 9z"/>
<path d="M3780 3115 c-7 -13 -28 -31 -46 -40 -35 -17 -45 -35 -19 -35 12 0 15
-19 15 -109 0 -86 3 -113 16 -125 23 -24 77 -20 102 7 27 29 29 47 3 23 -33
-30 -41 -11 -41 100 l0 104 28 0 c34 0 49 10 54 35 2 12 -3 21 -15 23 -15 3
-18 0 -12 -17 5 -18 2 -21 -24 -21 -29 0 -31 2 -31 40 0 46 -11 51 -30 15z"/>
<path d="M1790 3048 c-52 -26 -80 -73 -80 -131 0 -77 48 -127 122 -127 44 0
108 30 108 50 0 7 -9 5 -22 -4 -31 -22 -52 -20 -87 10 -47 39 -41 63 24 102
68 41 81 62 57 91 -27 32 -70 36 -122 9z m58 -20 c22 -22 14 -57 -18 -73 -41
-21 -43 -20 -35 23 10 56 29 74 53 50z"/>
<path d="M2003 3056 c-36 -16 -51 -53 -34 -84 5 -10 26 -38 46 -62 43 -52 44
-83 2 -88 -16 -2 -35 2 -43 9 -8 6 -17 9 -20 7 -12 -13 51 -48 87 -48 53 0 69
9 84 44 17 40 6 67 -50 127 -48 51 -51 79 -9 79 26 0 30 -10 12 -28 -9 -9 -7
-13 5 -18 21 -8 37 3 37 25 0 40 -65 60 -117 37z"/>
<path d="M2410 3052 c-28 -14 -35 -23 -35 -47 0 -24 5 -31 23 -33 28 -4 42 26
18 40 -9 5 -14 13 -11 19 9 14 61 11 75 -6 21 -26 6 -49 -49 -77 -64 -31 -81
-50 -81 -93 0 -57 66 -86 117 -50 18 13 22 13 33 0 14 -17 53 -20 81 -5 22 12
26 32 4 24 -13 -5 -15 8 -15 86 0 104 -8 126 -55 146 -45 18 -63 18 -105 -4z
m80 -156 c0 -52 -23 -84 -46 -65 -17 14 -18 81 -2 97 7 7 20 12 30 12 15 0 18
-8 18 -44z"/>
<path d="M2633 3045 c-17 -15 -21 -23 -10 -19 15 6 17 -3 17 -87 0 -55 5 -104
13 -119 17 -33 70 -39 107 -12 26 20 27 20 38 1 16 -25 63 -25 93 1 22 19 22
20 4 18 -19 -3 -20 4 -23 110 -3 107 -4 113 -26 123 -18 8 -31 7 -55 -5 -31
-16 -44 -41 -16 -30 13 5 15 -8 15 -85 0 -79 -2 -92 -19 -101 -38 -20 -41 -13
-41 94 0 97 -2 106 -22 120 -30 22 -42 20 -75 -9z"/>
<path d="M2960 3063 c-8 -2 -21 -7 -29 -9 -11 -4 -11 -7 2 -17 13 -10 17 -34
19 -127 l3 -115 35 0 35 0 3 98 c3 92 4 98 28 114 20 13 30 14 44 5 23 -14 35
10 20 39 -14 25 -23 24 -56 -4 l-27 -23 -23 23 c-24 24 -28 25 -54 16z"/>
<path d="M3200 3052 c-28 -14 -35 -23 -35 -47 0 -24 5 -31 23 -33 28 -4 42 26
18 40 -9 5 -14 13 -11 19 9 14 61 11 75 -6 21 -26 6 -49 -49 -77 -64 -31 -81
-50 -81 -93 0 -57 66 -86 117 -50 18 13 22 13 33 0 14 -17 53 -20 81 -5 22 12
26 32 4 24 -13 -5 -15 8 -15 86 0 104 -8 126 -55 146 -45 18 -63 18 -105 -4z
m80 -156 c0 -52 -23 -84 -46 -65 -17 14 -18 81 -2 97 7 7 20 12 30 12 15 0 18
-8 18 -44z"/>
<path d="M3434 3060 c-12 -5 -25 -13 -28 -19 -4 -7 -1 -8 8 -5 14 5 16 -9 16
-104 0 -61 3 -117 6 -126 4 -10 18 -16 40 -16 40 0 43 7 47 135 2 88 3 90 26
90 33 0 44 -39 37 -135 -4 -53 -12 -83 -26 -102 -21 -28 -21 -28 -1 -28 31 0
86 55 99 98 13 42 14 122 3 161 -3 13 -19 34 -34 45 l-28 21 -40 -22 c-40 -22
-40 -22 -60 -2 -21 21 -33 22 -65 9z"/>
<path d="M2203 2401 c-57 -41 -78 -90 -78 -182 0 -66 4 -81 28 -118 33 -49 76
-71 142 -71 77 0 132 41 160 119 44 124 -24 271 -125 271 -57 0 -82 -27 -78
-87 3 -51 27 -78 50 -55 9 9 7 16 -10 32 -26 24 -28 52 -6 74 20 21 30 20 53
-3 26 -26 34 -72 30 -180 -3 -72 -8 -95 -25 -118 -46 -61 -105 -30 -125 66
-15 75 -5 194 21 238 32 54 23 58 -37 14z"/>
<path d="M2540 2303 c-8 -2 -21 -7 -29 -9 -11 -4 -11 -7 2 -17 13 -10 17 -34
19 -127 l3 -115 35 0 35 0 5 104 c4 86 8 106 23 115 30 18 47 -17 47 -98 0
-84 -14 -142 -38 -155 -30 -18 14 -13 49 5 42 21 69 83 69 162 0 130 -61 179
-134 106 -9 -8 -16 -11 -16 -5 0 14 -29 41 -43 40 -7 0 -19 -3 -27 -6z"/>
<path d="M2882 2290 c-70 -32 -101 -123 -66 -196 20 -42 59 -64 111 -64 39 0
103 31 103 50 0 7 -9 5 -22 -4 -33 -23 -56 -20 -89 13 -43 43 -38 61 31 100
81 47 92 88 28 110 -41 14 -46 14 -96 -9z m62 -26 c13 -33 5 -54 -24 -69 -39
-20 -40 -20 -33 18 11 62 42 90 57 51z"/>
<path d="M3160 2191 c0 -6 5 -13 10 -16 6 -3 10 1 10 9 0 9 -4 16 -10 16 -5 0
-10 -4 -10 -9z"/>
<path d="M3296 2175 c-16 -9 -35 -24 -43 -34 -7 -10 -55 -39 -107 -65 -89 -43
-136 -82 -136 -112 0 -23 18 -16 72 27 29 22 78 54 110 70 49 25 66 28 110 24
58 -6 91 6 114 41 11 16 12 23 1 38 -18 24 -85 31 -121 11z m84 -49 c-8 -8
-28 -17 -45 -20 l-30 -6 32 12 c17 7 35 16 39 21 4 4 10 7 13 7 3 0 -1 -6 -9
-14z"/>
<path d="M3462 2153 c2 -10 10 -18 18 -18 8 0 16 8 18 18 2 12 -3 17 -18 17
-15 0 -20 -5 -18 -17z"/>
<path d="M4421 2122 c-5 -9 -12 -35 -16 -57 -18 -95 -95 -192 -190 -236 -70
-34 -51 -38 30 -8 75 28 165 112 205 191 30 62 35 83 24 112 -8 21 -41 20 -53
-2z"/>
<path d="M3573 2116 c-23 -8 -63 -25 -89 -40 -25 -14 -62 -26 -82 -26 -33 0
-122 -45 -122 -62 0 -12 8 -10 36 8 13 9 27 14 30 12 3 -3 -11 -15 -31 -26
-48 -29 -45 -47 5 -22 54 28 63 25 15 -5 -25 -16 -33 -25 -22 -25 29 0 96 38
114 66 21 33 81 59 189 81 80 17 104 33 68 47 -24 9 -64 6 -111 -8z"/>
<path d="M1415 2044 c-103 -16 -233 -52 -320 -88 -76 -32 -53 -33 45 -2 109
35 251 56 423 64 162 8 207 24 96 36 -85 8 -139 6 -244 -10z"/>
<path d="M3230 2035 c0 -9 5 -15 11 -13 6 2 11 8 11 13 0 5 -5 11 -11 13 -6 2
-11 -4 -11 -13z"/>
<path d="M1221 1723 c49 -83 168 -233 254 -318 240 -242 539 -403 881 -476 98
-22 133 -24 354 -23 215 0 257 3 345 22 474 106 864 378 1128 790 l27 42 -24
0 c-19 0 -35 -17 -79 -82 -308 -462 -837 -740 -1407 -740 -369 0 -730 120
-1015 336 -155 118 -304 276 -399 424 -30 48 -45 62 -64 62 l-24 0 23 -37z"/>
<path d="M2472 1706 c-18 -39 -27 -46 -59 -51 -69 -12 -69 -13 -29 -54 38 -39
38 -39 28 -87 -6 -27 -8 -51 -6 -53 3 -3 25 6 50 19 l45 25 50 -27 50 -27 -5
30 c-3 16 -8 41 -11 57 -5 22 1 34 30 62 43 41 44 50 6 50 -50 0 -76 16 -96
59 -10 23 -21 41 -25 41 -3 0 -16 -20 -28 -44z"/>
<path d="M2149 1581 c-10 -33 -17 -40 -52 -51 l-41 -12 32 -27 c27 -22 32 -33
32 -70 l0 -43 35 27 c36 26 36 27 77 10 38 -15 40 -15 34 2 -19 48 -18 72 4
100 l22 28 -41 3 c-33 3 -44 9 -61 38 -12 18 -23 34 -25 34 -2 0 -9 -17 -16
-39z"/>
<path d="M2811 1584 c-20 -29 -29 -34 -63 -34 l-39 0 21 -31 c22 -29 23 -55 5
-101 -7 -17 -4 -17 35 -3 42 15 44 14 76 -10 l34 -26 0 44 c0 37 5 47 32 67
l32 24 -41 17 c-32 13 -43 24 -48 48 -9 43 -17 44 -44 5z"/>
</g>
</svg>
          </StyledSection>
        )}

        <Container maxWidth="sm">
          <StyledContent>
            <Typography variant="h4" gutterBottom>
              Sign in to RestaurantOne
            </Typography>

            <Typography variant="body2" sx={{ mb: 5 }}>
              Don’t have an account? {''}
              <Link href={url} variant="subtitle2">Get started</Link>
            </Typography>

            <Stack direction="row" spacing={2}>
              <Button fullWidth size="large" color="inherit" variant="outlined" onClick={handleGoogleLogin}>
                <Iconify icon="eva:google-fill" color="#DF3E30" width={22} height={22} />
              </Button>

              <Button fullWidth size="large" color="inherit" variant="outlined" onClick={handleGithubLogin}>
                <Iconify icon="eva:github-fill" color="#1877F2" width={22} height={22} />
              </Button>

              <Button fullWidth size="large" color="inherit" variant="outlined" onClick={handleTwitterLogin}>
                <Iconify icon="eva:twitter-fill" color="#1C9CEA" width={22} height={22} />
              </Button>
            </Stack>

            <Divider sx={{ my: 3 }}>
              <Typography variant="body2" sx={{ color: 'text.secondary' }}>
                OR
              </Typography>
            </Divider>

            <LoginForm />
          </StyledContent>
        </Container>
      </StyledRoot>
    </>
  );
}
