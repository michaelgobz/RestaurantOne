import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { alpha } from '@mui/material/styles';
import { Box, Divider, Typography, Stack, MenuItem, Avatar, IconButton, Popover } from '@mui/material';
// mocks_
import account from '../../../_mock/account';

// ----------------------------------------------------------------------

const MENU_OPTIONS = [
  {
    label: 'Orders',
    icon: 'eva:order-list-fill',
    path: 'customer/orders'
  },
  {
    label: 'Reservations',
    icon: 'eva:calendar-fill',
    path: 'customer/reservations'
  },
  {
    label: 'Account',
    icon: 'eva:person-fill',
    path: 'account'
  },
  {
    label: 'Reviews',
    icon: 'eva:review-fill',
    path: 'customer/reviews'
  },
];
const AUTH_OPTIONS = [
  {
    label: 'Login',
    path: 'auth/login'
  },
  {
    label: 'Logout',
    path: 'auth/logout'
  }
]

const MENU_OPTIONS_AUTH = [

]

// ----------------------------------------------------------------------

export default function AccountPopover() {

  const auth = true;

  const navigator = useNavigate()

  const [open, setOpen] = useState(null);

  const handleOpen = (event) => {
    setOpen(event.currentTarget);
  };

  const handleClose = () => {
    setOpen(null);
  };

  const HandleNavigateAuth = () => {
    console.log('navigate')
    handleClose()
  }
  const HandleAuth = () => {
    if ( !auth ){
      navigator('auth/login')
      handleClose()
    } else {
      navigator('auth/logout')
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
            {account.displayName}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary' }} noWrap>
            {account.email}
          </Typography>
        </Box>
        {
          auth ?
            <Divider sx={{ borderStyle: 'dashed' }} />
            :
            <Divider sx={{ borderStyle: 'dashed', borderColor: 'white' }} />
        }


        <Stack sx={{ p: 1 }}>
          {auth ?
            MENU_OPTIONS.map((option) => (
              <MenuItem key={option.label} onClick={HandleNavigateAuth}>
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
          auth ?
            <Divider sx={{ borderStyle: 'dashed' }} />
            :
            <Divider sx={{ borderStyle: 'dashed', borderColor: 'white' }} />
        }
        {
          auth ?
            <MenuItem key={AUTH_OPTIONS[1].path} onClick={HandleAuth} sx={{ m: 1 }} >
              {AUTH_OPTIONS[1].label}
            </MenuItem>
            :
            <MenuItem key={AUTH_OPTIONS[0].path} onClick={HandleAuth} sx={{ m: 1 }} >
              {AUTH_OPTIONS[0].label}
            </MenuItem>

        }
      </Popover>
    </>
  );
}
