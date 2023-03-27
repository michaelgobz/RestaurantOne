import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { alpha } from '@mui/material/styles';
import { Box, Divider, Typography, Stack, MenuItem, Avatar, IconButton, Popover } from '@mui/material';
// mocks_
import SnackBar from '../../../sections/snackbar/SnackBar';
import account from '../../../_mock/account';

// ----------------------------------------------------------------------

const MENU_OPTIONS = [
  {
    label: 'Orders',
    icon: 'eva:order-list-fill',
    path: '/customer/orders'
  },
  {
    label: 'Reservations',
    icon: 'eva:calendar-fill',
    path: '/customer/reservations'
  },
  {
    label: 'Account',
    icon: 'eva:person-fill',
    path: '/account/me'
  },
  {
    label: 'Reviews',
    icon: 'eva:review-fill',
    path: '/customer/reviews'
  },
];
const AUTH_OPTIONS = [
  {
    label: 'Login',
    path: '/auth/login'
  },
  {
    label: 'Logout',
    path: '/auth/login'
  }
]

const MENU_OPTIONS_AUTH = [

]

const SNACK_BAR_OPTIONS = [
  {
    label: 'Login Successful',
    severity: 'success'
  },
  {
    label: 'Logout Successful',
    severity: 'success'
  },
  {
    label: 'Login Failed',
    severity: 'error'
  },
  {
    label: 'Logout Failed',
    severity: 'error'
  }

]

// ----------------------------------------------------------------------

export default function AccountPopover() {

  const [user, setUser] = useState({})

  const api = `${process.env.REACT_APP_API}/me/account/profile`
  const requestOptions = {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${sessionStorage.getItem('token')}`,
    },
  }
  // get user from session storage
  useEffect(() => {
    fetch(api, requestOptions).then((response) => response.json().then((data) => {
      if (response.status === 200) {
        console.log(api)
        console.log(data.user)
        setUser(data.user)
      } else {
        console.log('some error has happened')
      }
    })).catch((error) => {
      console.log(error);
    }).finally(() => {
      console.log('user', user)
    });
  }, []);

  const navigator = useNavigate()

  const [open, setOpen,] = useState(null);
  const [showComponent, setShowComponent] = useState(false)

  const handleOpen = (event) => {
    setOpen(event.currentTarget);
  };

  const handleClose = () => {
    setOpen(null);
  };

  const HandleNavigateAuth = (path) => {
    console.log(path)
    navigator(path)
    handleClose()
  }

  const ShowSnackBar = () => {
    setShowComponent(true)
    console.log('show snackbar')
  }
  const HandleAuth = () => {

    if (sessionStorage.getItem('auth') === 'true') {
      navigator('auth/lo')
      handleClose()

    } else {
      navigator('auth/login')
      handleClose()
    }

  }

  return (
    <>
      <IconButton
        onClick={handleOpen}
        sx={{
          p: 0,
          ...(open && {
            '&:before': {
              zIndex: 1,
              content: "''",
              width: '100%',
              height: '100%',
              borderRadius: '50%',
              position: 'absolute',
              bgcolor: (theme) => alpha(theme.palette.grey[900], 0.8),
            },
          }),
        }}
      >
        <Avatar src={account.photoURL} alt="photoURL" />
      </IconButton>

      <Popover
        open={Boolean(open)}
        anchorEl={open}
        onClose={handleClose}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
        transformOrigin={{ vertical: 'top', horizontal: 'right' }}
        PaperProps={{
          sx: {
            p: 0,
            mt: 1.5,
            ml: 0.75,
            width: 180,
            '& .MuiMenuItem-root': {
              typography: 'body2',
              borderRadius: 0.75,
            },
          },
        }}
      >
        <Box sx={{ my: 1.5, px: 2.5 }}>
          <Typography variant="subtitle2" noWrap>
            {sessionStorage.getItem('auth') === 'true' ? user.firstname : 'Guest'}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }} noWrap>
            {sessionStorage.getItem('auth') === 'true' ? user.email : ""}
          </Typography>
        </Box>
        {
          sessionStorage.getItem('auth') === 'true' ?
            <Divider sx={{ borderStyle: 'dashed' }} />
            :
            <Divider sx={{ borderStyle: 'dashed', borderColor: 'white' }} />
        }


        <Stack sx={{ p: 1 }}>
          {sessionStorage.getItem('auth') === 'true' ?
            MENU_OPTIONS.map((option) => (
              <MenuItem key={option.label} onClick={() => { HandleNavigateAuth(option.path) }}>
                {option.label}
              </MenuItem>
            )) :
            MENU_OPTIONS_AUTH.map((option) => (
              <MenuItem key={option.label} onClick={HandleNavigateAuth}>
                {option.label}
              </MenuItem>
            ))

          }
        </Stack>

        {
          sessionStorage.getItem('auth') === 'true' ?
            <Divider sx={{ borderStyle: 'dashed' }} />
            :
            <Divider sx={{ borderStyle: 'dashed', borderColor: 'white' }} />
        }
        {
          sessionStorage.getItem('auth') === 'true' ?
            <MenuItem key={AUTH_OPTIONS[1].path} onClick={() => { HandleAuth(); ShowSnackBar(); }} sx={{ m: 1 }} >
              {AUTH_OPTIONS[1].label}
              {showComponent ? <SnackBar message={SNACK_BAR_OPTIONS[1].label} severity={SNACK_BAR_OPTIONS[1].severity} /> : null}
            </MenuItem>
            :
            <MenuItem key={AUTH_OPTIONS[0].path} onClick={() => { HandleAuth(); ShowSnackBar(); }} sx={{ m: 1 }} >
              {AUTH_OPTIONS[0].label}
              {showComponent ? <SnackBar message={SNACK_BAR_OPTIONS[0].label} severity={SNACK_BAR_OPTIONS[0].severity} /> : null}

            </MenuItem>

        }
      </Popover>
    </>
  );
}
