import { useState } from 'react';
import { useNavigate } from 'react-router';
// @mui
import { Link, Stack, IconButton, InputAdornment, TextField, Checkbox, Typography } from '@mui/material';
import { LoadingButton } from '@mui/lab';
// components
import Iconify from '../../../components/iconify';

// ----------------------------------------------------------------------

export default function LoginForm() {

  const url = 'http://localhost:5000/api/v1/auth/login';

  // get data from the form
  const [email] = useState('');
  const [password] = useState('');
  const [data, setData] = useState({
    email: '',
    password: '',
  });


  const [showPassword, setShowPassword] = useState(false);

  const requestOptions = {
    method: 'POST',
    mode: 'cors',
    body: JSON.stringify(data),
    headers: { 'Content-Type': 'application/json' },
  };

  const HandleSubmit = () => { 
    console.log('clicked');
    fetch(url, requestOptions)
      .then((response) => {
        console.log(response);
      })
  };

  const HandleChange = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  return (
    <>
      <Stack spacing={3}>
        <TextField name="email" value={email} onChange={HandleChange} label="Email address" />

        <TextField
          name="password"
          label="Password"
          value={password}
          onChange={HandleChange}
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
      </Stack>

      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ my: 2 }}>
        <Checkbox name="remember" label="Remember me" />
        <Typography variant='body5' sx={{ ml: -5 }}>Remember Me</Typography>
        <Link variant="subtitle2" underline="hover">
          Forgot password?
        </Link>
      </Stack>

      <LoadingButton fullWidth size="large" type="submit" variant="contained" onClick={HandleSubmit}>
        Login
      </LoadingButton>
    </>
  );
}
