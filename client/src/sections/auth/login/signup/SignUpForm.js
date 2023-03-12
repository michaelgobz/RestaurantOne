import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox ,Typography} from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../../components/iconify';

// ----------------------------------------------------------------------

export default function SignUpForm() {
  const [showPassword, setShowPassword] = useState(false);

  const handleClick = () => {
    window.alert('Sign Up');
  };

  return (
    <>
      <Stack spacing={3}>
        <TextField name="Lirstname" label="First Name" />
        <TextField name="Lastname" label="Last Name" />
        <TextField name="email" label="Email address" />
        <TextField
          name="password"
          label="Password"
          type={showPassword ? 'text' : 'password'}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                  <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
        <TextField
          name="Retype-password"
          label="Retype Password"
          type={showPassword ? 'text' : 'password'}
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                  <Iconify icon={showPassword ? 'eva:eye-fill' : 'eva:eye-off-fill'} />
                </IconButton>
              </InputAdornment>
            ),
          }}
        />
        <TextField name="Phonenumber" label="Phone number" />

      </Stack>

      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ my: 2 }}>
        <Checkbox name="remember" label="Remember me" />
        <Typography> Accept the privacy policy and T&Cs</Typography>
        <Link variant="subtitle2" underline="hover">
          Forgot password?
        </Link>
      </Stack>

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={handleClick}>
        Sign Up
      </LoadingButton>
    </>
  );
};